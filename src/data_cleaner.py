import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from .logger import setup_logger

logger = setup_logger('data_cleaner', 'logs/pipeline.log')

def handle_missing_values(df, strategy='mean'):
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            if strategy == 'mean':
                df[col] = df[col].fillna(df[col].mean())
            elif strategy == 'median':
                df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    logger.info(f"Missing values handled with strategy: {strategy}")
    return df

def remove_duplicates(df):
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    removed_count = initial_count - len(df)
    logger.info(f"Duplicates removed: {removed_count}")
    return df

def encode_categorical(df, columns, method='onehot'):
    if method == 'onehot':
        df = pd.get_dummies(df, columns=columns, drop_first=True)
    elif method == 'label':
        le = LabelEncoder()
        for col in columns:
            df[col] = le.fit_transform(df[col].astype(str))
    logger.info(f"Categorical columns encoded: {columns} with method: {method}")
    return df

def scale_features(df, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    logger.info(f"Features scaled: {columns}")
    return df

def convert_date_column(df, column):
    df[column] = pd.to_datetime(df[column])
    logger.info(f"Date column converted: {column}")
    return df