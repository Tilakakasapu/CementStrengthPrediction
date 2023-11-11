import pandas as pd
from  cementstrength import logger
from sklearn.ensemble import GradientBoostingRegressor
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
from cementstrength.entity.config_entity import ModelTrainerConfig
import os
from sklearn.pipeline import make_pipeline


class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig):
        self.config = config
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)
        train_x = train_data.drop(([self.config.target_column]),axis=1)
        test_x = test_data.drop([self.config.target_column],axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]
        logger.info("data sets seperated to x_train,x_test and y_train,y_test")
        # preprocessor_01 = make_pipeline(StandardScaler())
        scaler = StandardScaler()
        scaler.fit_transform(train_x)
        scaler.transform(test_x)

        # lr = ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio,random_state=42)
        # lr.fit(train_x,train_y)
        gb_rg = GradientBoostingRegressor(learning_rate= self.config.learning_rate,max_depth= self.config.max_depth,min_samples_leaf= self.config.min_samples_leaf,min_samples_split= self.config.min_samples_split,n_estimators= self.config.n_estimators)
        gb_rg.fit(train_x,train_y)
        logger.info("training of the model is going to done saving files......")
        joblib.dump(gb_rg,os.path.join(self.config.root_dir,self.config.model_name))
        joblib.dump(scaler,os.path.join(self.config.root_dir,"scaler"))