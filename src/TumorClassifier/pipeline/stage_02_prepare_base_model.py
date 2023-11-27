from TumorClassifier.config.configuration import ConfigurationManager
from TumorClassifier.components.prepare_base_model import PrepareBaseModel
from TumorClassifier import logger

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
        
if __name__ == "__main__":
    try:
        logger.info(f"---{STAGE_NAME} started---")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"---{STAGE_NAME} completed ---")
    
    except Exception as e:
        logger.exception(e)
        raise e