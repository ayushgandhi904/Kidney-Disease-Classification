from TumorClassifier.config.configuration import ConfigurationManager
from TumorClassifier.components.model_evaluation import Evaluation
from TumorClassifier import logger

STAGE_NAME = "Model Evaluation"

class ModelEvauationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()
        
if __name__ == "__main__":
    try:
        logger.info(f"---{STAGE_NAME} started---")
        obj = ModelEvauationPipeline()
        obj.main()
        logger.info(f"---{STAGE_NAME} completed ---")
    
    except Exception as e:
        logger.exception(e)
        raise e