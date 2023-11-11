from cementstrength.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from cementstrength import *
from cementstrength.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline
from cementstrength.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from cementstrength.pipeline.stage_04_model_tainer import ModeltrainerTrainingPipeline
STAGE_NAME = "DataIngestion"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "Data validation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DatavalidationTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    raise e
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e
STAGE_NAME = "model training stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj = ModeltrainerTrainingPipeline()
    obj.main()
    logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e