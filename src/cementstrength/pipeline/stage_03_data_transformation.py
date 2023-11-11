from cementstrength.config.configuration import ConfigurationManager
from cementstrength.components.data_transformation import DataTransformation
from cementstrength import logger
from pathlib import Path
STAGE_NAME = "Data Transformation stage"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1]
            if status =="True":
                config= ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("your data schema is not vaid")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
