from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, mean_squared_error
from .logger import setup_logger

logger = setup_logger('ml_model', 'logs/pipeline.log')

def train_regression_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    # rmse = mean_squared_error(y_test, y_pred, squared=False)  # ❌ Устаревший способ
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5  # ✅ Новый способ
    logger.info(f"Regression model trained. RMSE: {rmse}")
    return model, rmse

def train_classification_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted')
    rec = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    logger.info(f"Classification model trained. Accuracy: {acc}, Precision: {prec}, Recall: {rec}, F1: {f1}")
    return model, acc, prec, rec, f1