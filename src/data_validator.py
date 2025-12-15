import pandas as pd
import numpy as np
from scipy import stats
from .logger import setup_logger

logger = setup_logger('data_validator', 'logs/pipeline.log')

def validate_duplicates(df):
    duplicates = df.duplicated().sum()
    logger.info(f"Duplicates found: {duplicates}")
    return duplicates

def validate_missing_values(df):
    missing = df.isnull().sum()
    logger.info(f"Missing values:\n{missing}")
    return missing

def validate_data_types(df):
    dtypes = df.dtypes
    logger.info(f"Data types:\n{dtypes}")
    return dtypes

def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    logger.info(f"Outliers in {column} (IQR): {len(outliers)}")
    return outliers

def detect_outliers_zscore(df, column, threshold=3):
    z_scores = np.abs(stats.zscore(df[column].dropna()))
    outliers = df[z_scores > threshold]
    logger.info(f"Outliers in {column} (Z-score): {len(outliers)}")
    return outliers