import json

def GetListOfMissingOrUnknownDataColumns(dataFrame, missingDataDecimal):
    listOfMissingOrUnknownDataColumns = []
    for (columnName, columnData) in dataFrame.iteritems():
        sumOfMissingData = (columnData.isna().sum() + columnData.isin(['U', 'Unknown']).sum())
        if ((columnData.count() == 0) or sumOfMissingData/columnData.count() > missingDataDecimal):
            listOfMissingOrUnknownDataColumns.append(columnName)
    return listOfMissingOrUnknownDataColumns

def DropColumns(dataFrame, missingDataDecimal):
    jsonFile = open('ManuallyDroppedColumns.json', 'r')
    data = json.load(jsonFile)
    jsonFile.close()
    columnsToBeDropped = list(set(data['ColumnNames'] + GetListOfMissingOrUnknownDataColumns(dataFrame, missingDataDecimal)))
    dataFrame.drop(columnsToBeDropped, axis=1, inplace=True)
    return dataFrame
