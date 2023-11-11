from cementstrength.config.configuration import ConfigurationManager
from cementstrength.components.model_trainer import ModelTrainer
from cementstrength import logger
STAGE_NAME = "model training stage"
class ModeltrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = ModeltrainerTrainingPipeline()
        obj.main()
        logger.info(f">>stage {STAGE_NAME} completed <<<<< \n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e
