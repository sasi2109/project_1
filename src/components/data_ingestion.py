from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os
import sys

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw_data.csv')

class dataingestion:
    try:
        def __init__(self):
            self.dataconfig = DataIngestionConfig()

        def initiate_dataingestion(self):
            os.makedirs(os.path.dirname(self.dataconfig.train_data_path),exist_ok=True)

            logging.info("Reading Input Data")
            df = pd.read_csv(r'src\notebooks\input_data\input_data.csv')
            logging.info("Reading Input Data Susscessful")

            train_data,test_data = train_test_split(df,test_size=0.2,random_state=40)

            train_data.to_csv(self.dataconfig.train_data_path)
            test_data.to_csv(self.dataconfig.test_data_path)
            df.to_csv(self.dataconfig.raw_data_path,index=False,header=True)

            return (self.dataconfig.train_data_path,self.dataconfig.test_data_path)
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__=="__main__":
    obj = dataingestion()
    obj.initiate_dataingestion()

