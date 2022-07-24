import pandas as pd
import HelperFunctions as hf


def ChangeDateColumns(dataFrame : pd.DataFrame):
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['INIT_DATE'], 'INIT_DATE'))
    dataFrame.drop('INIT_DATE', axis=1, inplace=True)
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['END_DATE'], 'END_DATE'))
    dataFrame.drop('END_DATE', axis=1, inplace=True)
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['TX_DATE'], 'TX_DATE'))
    dataFrame.drop('TX_DATE', axis=1, inplace=True)
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['RETXDATE'], 'RETXDATE'))
    dataFrame.drop('RETXDATE', axis=1, inplace=True)
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['PX_STAT_DATE'], 'PX_STAT_DATE'))
    dataFrame.drop('PX_STAT_DATE', axis=1, inplace=True)
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['DISCHARGE_DATE'], 'DISCHARGE_DATE'))
    dataFrame.drop('DISCHARGE_DATE', axis=1, inplace=True)
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['ADMISSION_DATE'], 'ADMISSION_DATE'))
    dataFrame.drop('ADMISSION_DATE', axis=1, inplace=True)
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['REFERRAL_DATE'], 'REFERRAL_DATE'))
    dataFrame.drop('REFERRAL_DATE', axis=1, inplace=True)
    dataFrame = dataFrame.join(hf.CreateSeasonalColumns(dataFrame['ADMIT_DATE_DON'], 'ADMIT_DATE_DON'))
    dataFrame.drop('ADMIT_DATE_DON', axis=1, inplace=True)
    return dataFrame


def ChangeBloodTypeColumns(dataFrame : pd.DataFrame):
    dataFrame = dataFrame.join(hf.CreateBloodTypeCatagoryColumns(dataFrame['ABO']))
    dataFrame.drop('ABO', axis=1, inplace=True)
    return dataFrame


def ChangeBooleanColumns(dataFrame : pd.DataFrame):
    dataFrame['DATA_TRANSPLANT'] = hf.CreateBooleanColumn(dataFrame['DATA_TRANSPLANT'], 'Y', 'N')
    dataFrame['DATA_WAITLIST'] = hf.CreateBooleanColumn(dataFrame['DATA_WAITLIST'], 'Y', 'N')
    dataFrame['GENDER'] = hf.CreateBooleanColumn(dataFrame['GENDER'], 'M', 'F')
    return dataFrame