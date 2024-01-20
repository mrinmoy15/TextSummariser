from textSummariser.logging import logger
from textSummariser.components.model_trainer import ModelTrainer
from textSummariser.config.configuration import ConfigurationManager

class ModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config) 
        model_trainer.train()

