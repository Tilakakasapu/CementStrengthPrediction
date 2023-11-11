import os
from cementstrength import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from cementstrength.config.configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config

# here you can do all EDA and other PCA in here i am doing it coz it is already cleaned up
    
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        data.drop(['Unnamed: 0'],axis=1,inplace=True)
        data.drop_duplicates(keep='first',inplace=True)
        data.reset_index(drop = True,inplace=True)
        outliers = ['Blast',"Water", "Superplasticizer", 'Fine', 'Age']
        def outlier_capping(dataframe: pd.DataFrame,outliers: list):
            df = dataframe.copy()
            for i in outliers:
                q1 = df[i].quantile(0.25)
                q2 = df[i].quantile(0.75)
                iqr = q2 - q1
                upper_limit = q2 + 1.5*iqr
                lower_limit = q2-1.5*iqr
                df.loc[df[i]>upper_limit,i]=upper_limit
                df.loc[df[i]<lower_limit,i]=lower_limit
            return df
        data = outlier_capping(dataframe=data,outliers=outliers)
        train,test = train_test_split(data,test_size=0.3,random_state=42)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        logger.info("splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        print(train.shape)
        print(test.shape)
        
