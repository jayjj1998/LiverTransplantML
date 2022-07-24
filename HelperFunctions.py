import json
import pandas as pd
import traceback
from datetime import datetime


def GetListOfMissingOrUnknownDataColumns(dataFrame : pd.DataFrame, missingDataDecimal : float):
    listOfMissingOrUnknownDataColumns = []
    for (columnName, columnData) in dataFrame.iteritems():
        sumOfMissingData = (columnData.isna().sum() + columnData.isin(['U', 'Unknown']).sum())
        if (columnData.count() == 0) or sumOfMissingData / columnData.count() > missingDataDecimal:
            listOfMissingOrUnknownDataColumns.append(columnName)
    return listOfMissingOrUnknownDataColumns


def DropColumns(dataFrame : pd.DataFrame, missingDataDecimal : float):
    jsonFile = open('ManuallyDroppedColumns.json', 'r')
    data = json.load(jsonFile)
    jsonFile.close()
    jsonFile = open('ManuallyInsertedColumns.json', 'r')
    listOfManuallyInsertedColumns = json.load(jsonFile)
    jsonFile.close()
    columnsToBeDropped = list(
        set(data['ColumnNames'] + GetListOfMissingOrUnknownDataColumns(dataFrame, missingDataDecimal)))
    columnsToBeDropped = [x for x in columnsToBeDropped if x not in listOfManuallyInsertedColumns['ColumnNames']]
    dataFrame.drop(columnsToBeDropped, axis=1, inplace=True)
    return dataFrame


def CreateSeasonalColumns(dataSeries : pd.Series, newColumnName : str):
    columnList = [newColumnName + '_JANFEBMAR', newColumnName + '_APRMAYJUN',
                   newColumnName + '_JULAUGSEP', newColumnName + '_OCTNOVDEC',
                   newColumnName + '_UNKNOWN']
    newDataFrame = pd.DataFrame(columns=columnList)
    row_JANFEBMAR = pd.DataFrame([[1, 0, 0, 0, 0]], columns=columnList)
    row_APRMAYJUN = pd.DataFrame([[0, 1, 0, 0, 0]], columns=columnList)
    row_JULAUGSEP = pd.DataFrame([[0, 0, 1, 0, 0]], columns=columnList)
    row_OCTNOVDEC = pd.DataFrame([[0, 0, 0, 1, 0]], columns=columnList)
    row_UNKNOWN = pd.DataFrame([[0, 0, 0, 0, 1]], columns=columnList)
    for (rowNum, rowData) in enumerate(dataSeries):
        if rowData is not None and not pd.isna(rowData):
            try:
                dt = datetime.strptime(rowData, '%Y-%m-%d')
                dtMonth = dt.month
                if (dtMonth > 0 and dtMonth <= 3):
                    newDataFrame = pd.concat([newDataFrame, row_JANFEBMAR], axis=0, ignore_index=True)
                elif (dtMonth > 3 and dtMonth <= 6):
                    newDataFrame = pd.concat([newDataFrame, row_APRMAYJUN], axis=0, ignore_index=True)
                elif (dtMonth > 6 and dtMonth <= 9):
                    newDataFrame = pd.concat([newDataFrame, row_JULAUGSEP], axis=0, ignore_index=True)
                elif (dtMonth > 9 and dtMonth <= 12):
                    newDataFrame = pd.concat([newDataFrame, row_OCTNOVDEC], axis=0, ignore_index=True)
            except Exception as err:
                print(f'Error occurred with row number {rowNum}\n {err}')
                traceback.print_exc()
        else:
            newDataFrame = pd.concat([newDataFrame, row_UNKNOWN], axis=0, ignore_index=True)
    print('DONE')
    return newDataFrame

def CreateBloodTypeCatagoryColumns(dataSeries : pd.Series):
    columnList = ['IS_BLOOD-TYPE_A', 'IS_BLOOD-TYPE_B', 'IS_BLOOD-TYPE_O', 'IS_BLOOD-TYPE_AB']
    newDataFrame = pd.DataFrame(columns=columnList)
    row_A = pd.DataFrame([[1, 0, 0, 0]], columns=columnList)
    row_B = pd.DataFrame([[0, 1, 0, 0]], columns=columnList)
    row_O = pd.DataFrame([[0, 0, 1, 0]], columns=columnList)
    row_AB = pd.DataFrame([[0, 0, 0, 1]], columns=columnList)
    for (rowNum, rowData) in enumerate(dataSeries):
        if rowData is not None and not pd.isna(rowData):
            try:
                if (rowData == 'A'):
                    newDataFrame = pd.concat([newDataFrame, row_A], axis=0, ignore_index=True)
                elif (rowData == 'B'):
                    newDataFrame = pd.concat([newDataFrame, row_B], axis=0, ignore_index=True)
                elif (rowData == 'O'):
                    newDataFrame = pd.concat([newDataFrame, row_O], axis=0, ignore_index=True)
                elif (rowData == 'AB'):
                    newDataFrame = pd.concat([newDataFrame, row_AB], axis=0, ignore_index=True)
            except Exception as err:
                print(f'Error occurred with row number {rowNum}\n {err}')
                traceback.print_exc()
        else:
            print('WOAH')
    print('DONE')
    return newDataFrame


def CreateBooleanColumn(dataSereies : pd.Series, oneString : str, zeroString : str):
    newDataSeries = dataSereies.copy()
    try:
        for (rowNum, rowData) in enumerate(dataSereies):
            if str(rowData) == oneString:
                newDataSeries[rowNum] = 1
            elif str(rowData) == zeroString:
                newDataSeries[rowNum] = 0
            else:
                newDataSeries[rowNum] = 0.5
    except Exception as err:
        print(f'Error occurred with row number {rowNum}\n {err}')
        traceback.print_exc()
    return newDataSeries


def Normalize(dataSeries : pd.Series):
    result = dataSeries.copy()
    max_value = result.max()
    min_value = result.min()
    result = (result - min_value) / (max_value - min_value)
    return result


def GetModeValue(dataSeries : pd.Series, numOfBins : int):
    listOfValues = dataSeries.tolist()
    minValue = min(listOfValues)
    maxValue = max(listOfValues)
    binSize = (maxValue - minValue) / numOfBins
    largestBin = 0
    elementsInLargestBin = 0
    for binNum in range(1, numOfBins + 1):
        count = 0
        lowerBinBound = binNum * binSize
        upperBinBound = (binNum + 1) * binSize
        for rowData in dataSeries:
            if rowData > lowerBinBound and rowData < upperBinBound:
                count += 1
        if count > elementsInLargestBin:
            largestBin = binNum
            elementsInLargestBin = count
    return (((largestBin * binSize)*2)+binSize)/2 + minValue
