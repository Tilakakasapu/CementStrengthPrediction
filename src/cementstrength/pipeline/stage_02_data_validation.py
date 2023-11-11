from cementstrength.config.configuration import ConfigurationManager
from cementstrength.components.data_validation import DataValidation
from cementstrength import logger
STAGE_NAME = "Data validation stage"
class DatavalidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = DatavalidationTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
