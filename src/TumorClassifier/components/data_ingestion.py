import os
import zipfile
import gdown
from TumorClassifier import logger
from TumorClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__ (self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self)->str:
        
        """
        To fetch data from URL
        """
        
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok= True)
            logger.info(f"Downloading data from {dataset_url} into file")
            
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_dir)
            
            logger.info(f"Downloaed data from {dataset_url}")
            
        except Exception as e:
            raise e
        
        
    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)