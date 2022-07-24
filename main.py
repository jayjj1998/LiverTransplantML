from configparser import ConfigParser
import HelperFunctions as hf
import pandas as pd
import Preprocessor as prep


def main():
    config = ConfigParser()
    config.read('Config.ini')
    liver_doc = pd.read_csv(config['FilePaths']['LiverCSV'], low_memory=False, index_col=0).head(2000)
    print(len(liver_doc.columns))
    liver_doc = hf.DropColumns(liver_doc, float(config['Constants']['MissingDataPercentage']))
    print(len(liver_doc.columns))
    liver_doc = prep.ChangeDateColumns(liver_doc)
    liver_doc = prep.ChangeBloodTypeColumns(liver_doc)
    liver_doc = prep.ChangeBooleanColumns(liver_doc)
    liver_doc.to_csv(config['FilePaths']['SaveAlteredCSV'], index=False)


if __name__ == '__main__':
    main()
