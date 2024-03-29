import os
from datetime import datetime

# Common constant
TIME_STAMP = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
TARGET_COLUMN = "Churn"
PIPELINE_NAME: str = "training_pipeline"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "training_data.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

# App constant
APP_HOST = "0.0.0.0"
APP_PORT = 8080

# Database constant
MONGODB_URL_KEY = "mongodb+srv://karaleguddi2:9579774398@mohinikarale.fgsd8ge.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = 'db-customer-churn'

# Data ingestion constant
DATA_INGESTION_COLLECTION_NAME: str = "telco-customer-churn"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2

# Data EDA constant

# Data transformation constant

# Model training constant

# Model evaluation constant

# Model push constant