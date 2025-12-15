import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from .logger import setup_logger

logger = setup_logger('data_analyzer', 'logs/pipeline.log')

def calculate_basic_stats(df):
    stats = df.describe()
    logger.info("Basic statistics calculated")
    return stats

def analyze_time_series(df, date_col, value_col):
    df.set_index(date_col, inplace=True)
    decomposition = seasonal_decompose(df[value_col], model='additive', period=12)
    logger.info("Time series decomposition completed")
    return decomposition

def detect_anomalies(df, column, method='iqr'):
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        anomalies = df[(df[column] < lower) | (df[column] > upper)]
    elif method == 'zscore':
        from scipy import stats
        z = np.abs(stats.zscore(df[column]))
        anomalies = df[z > 3]
    logger.info(f"Anomalies detected in {column} using {method}: {len(anomalies)}")
    return anomalies