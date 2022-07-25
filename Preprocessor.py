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
    print("Staring Change boolean column data DATA_TRANSPLANT")
    dataFrame['DATA_TRANSPLANT'] = hf.CreateBooleanColumn(dataFrame['DATA_TRANSPLANT'], 'Y', 'N')
    print("Staring Change boolean column data DATA_WAITLIST")
    dataFrame['DATA_WAITLIST'] = hf.CreateBooleanColumn(dataFrame['DATA_WAITLIST'], 'Y', 'N')
    print("Staring Change boolean column data GENDER")
    dataFrame['GENDER'] = hf.CreateBooleanColumn(dataFrame['GENDER'], 'M', 'F')
    print("Staring Change boolean column data LIFE_SUP_TCR")
    dataFrame['LIFE_SUP_TCR'] = hf.CreateBooleanColumn(dataFrame['LIFE_SUP_TCR'], 'Y', 'N')
    print("Staring Change boolean column data VENTILATOR_TCR")
    dataFrame['VENTILATOR_TCR'] = hf.CreateBooleanColumn(dataFrame['VENTILATOR_TCR'], '1', '0')
    print("Staring Change boolean column data OTH_LIFE_SUP_TCR")
    dataFrame['OTH_LIFE_SUP_TCR'] = hf.CreateBooleanColumn(dataFrame['OTH_LIFE_SUP_TCR'], '1', '0')
    print("FINISHED")
    return dataFrame


def ChangeFloatColumns(dataFrame : pd.DataFrame):
    print("Starting Float Column WGT_KG_TCR")
    dataFrame['WGT_KG_TCR'] = hf.FillMissingFloatData(dataFrame['WGT_KG_TCR'])
    dataFrame['HGT_CM_TCR'] = hf.FillMissingFloatData(dataFrame['HGT_CM_TCR'])
    dataFrame['BMI_TCR'] = hf.FillMissingFloatData(dataFrame['BMI_TCR'])
    dataFrame['INIT_WGT_KG'] = hf.FillMissingFloatData(dataFrame['INIT_WGT_KG'])
    dataFrame['INIT_HGT_CM'] = hf.FillMissingFloatData(dataFrame['INIT_HGT_CM'])
    dataFrame['REM_CD'] = hf.FillMissingFloatData(dataFrame['REM_CD'])
    dataFrame['DAYSWAIT_CHRON'] = hf.FillMissingFloatData(dataFrame['DAYSWAIT_CHRON'])
    print("Finished")
    return dataFrame
