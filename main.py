
from src.data_loader import load_csv, load_from_api
from src.data_validator import validate_duplicates, validate_missing_values, detect_outliers_iqr
from src.data_cleaner import handle_missing_values, remove_duplicates, encode_categorical
from src.data_analyzer import calculate_basic_stats
from src.ml_model import train_regression_model
from src.report_generator import generate_visualizations, generate_pdf_report, send_email_with_attachment
import json
import os
import os

def main():
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    os.makedirs('logs', exist_ok=True)

    with open('config/config.json') as f:
        config = json.load(f)

    csv_path = config['data_sources']['csv_file']
    if not os.path.exists(csv_path):
        print(f"Файл {csv_path} не найден. Создаю тестовый файл...")
        import pandas as pd
        test_df = pd.DataFrame({
            'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'category': ['tech', 'finance', 'tech'],
            'score': [8.5, 7.2, 9.1],
            'target': [1, 0, 1]
        })
        test_df.to_csv(csv_path, index=False)
        print(f"Тестовый файл {csv_path} создан.")

    # 1. Загрузка данных
    df = load_csv(csv_path)  # Используем переменную csv_path

    # 1. Загрузка данных
    df = load_csv(config['data_sources']['csv_file'])
    # df_api = load_from_api(config['data_sources']['api_url'])

    # 2. Валидация
    validate_duplicates(df)
    validate_missing_values(df)
    detect_outliers_iqr(df, df.select_dtypes(include=['number']).columns[0])

    # 3. Очистка
    df = handle_missing_values(df, strategy='median')
    df = remove_duplicates(df)
    df = encode_categorical(df, ['category'], method='onehot')

    # 4. Анализ
    stats = calculate_basic_stats(df)
    print(stats)

    # 5. ML
    X = df.select_dtypes(include=['number']).drop(columns=['target'], errors='ignore')
    y = df['target'] if 'target' in df.columns else df.iloc[:, 0]
    if len(X.columns) > 0:
        model, rmse = train_regression_model(X, y)

    # 6. Отчет
    generate_visualizations(df)
    generate_pdf_report()
    # send_email_with_attachment(config, 'reports/report.pdf')

if __name__ == "__main__":
    main()