from textSummariser.logging import logger
from textSummariser.components.data_validation import DataValidation
from textSummariser.config.configuration import ConfigurationManager

class DataValidationTrainingPipeline:
    
    def __inint__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_cofig = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_cofig)
        validation_result = data_validation.validate_all_files_exist()