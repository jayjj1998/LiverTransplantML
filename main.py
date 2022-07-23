from configparser import ConfigParser
import HelperFunctions as hp
import pandas as pd
import Preprocessor as prep

def main():
    config = ConfigParser()
    config.read('Config.ini')
    liverDoc = pd.read_csv(config['FilePaths']['LiverCSV'], low_memory=False)
    print(len(liverDoc.columns))
    liverDoc = hp.DropColumns(liverDoc, float(config['Constants']['MissingDataPercentage']))
    print(len(liverDoc.columns))
    liverDoc.to_csv(config['FilePaths']['SaveAlteredCSV'], index=False)

if __name__ == '__main__':
    main()