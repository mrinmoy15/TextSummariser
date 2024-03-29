from textSummariser.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummariser.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummariser.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummariser.pipeline.stage_04_model_training import ModelTrainingPipeline
from textSummariser.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from textSummariser.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    model_training = ModelEvaluationPipeline()
    model_training.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    raise e

