from textSummariser.logging import logger
from textSummariser.components.data_transformation import DataTransformation
from textSummariser.config.configuration import ConfigurationManager


class DataTransformationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()