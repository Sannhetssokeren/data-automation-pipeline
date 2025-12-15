import pandas as pd
import requests
from sqlalchemy import create_engine
import json
import os
from .logger import setup_logger

logger = setup_logger('data_loader', 'logs/pipeline.log')

def load_csv(file_path):
    df = pd.read_csv(file_path)
    logger.info(f"CSV loaded: {file_path}, shape: {df.shape}")
    return df

def load_excel(file_path):
    df = pd.read_excel(file_path)
    logger.info(f"Excel loaded: {file_path}, shape: {df.shape}")
    return df

def load_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        logger.info(f"API data loaded: {url}, shape: {df.shape}")
        return df
    else:
        logger.error(f"Failed to load from API: {url}")
        return pd.DataFrame()

def load_from_db(connection_string, query):
    engine = create_engine(connection_string)
    df = pd.read_sql_query(query, engine)
    logger.info(f"DB query executed, shape: {df.shape}")
    return df