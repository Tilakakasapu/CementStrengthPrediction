from src.cementstrength.config.configuration import ConfigurationManager
from src.cementstrength.components.data_ingestion import DataIngestion
from cementstrength import *
STAGE_NAME ="Data ingestion"
class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        Dataingestion = DataIngestion(data_ingestion_config)
    
if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e