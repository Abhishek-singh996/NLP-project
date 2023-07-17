from textSummarizer.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME  = 'Data Ingestion stage'
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x===========x')
except Exception as e:
    logger.error(e)
    raise e


STAGE_NAME  = 'Data Validation stage'
try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n x===========x')
except Exception as e:
    logger.error(e)
    raise e