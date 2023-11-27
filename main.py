from src.TumorClassifier import logger
from TumorClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from TumorClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from TumorClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"---{STAGE_NAME} started---")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"---{STAGE_NAME} completed ---")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"---{STAGE_NAME} started---")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"---{STAGE_NAME} completed ---")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"
try:
    logger.info(f"---{STAGE_NAME} started---")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"---{STAGE_NAME} completed ---")
except Exception as e:
    logger.exception(e)
    raise e