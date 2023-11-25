from src.TumorClassifier import logger
from TumorClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"---{STAGE_NAME} started---")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"---{STAGE_NAME} completed ---")
except Exception as e:
    logger.exception(e)
    raise e