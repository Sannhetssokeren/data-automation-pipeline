Автоматизация обработки данных

01 Описание

Этот проект представляет собой **модуль автоматизации обработки данных**, написанный на Python. Он позволяет:

- Загружать данные из различных источников (CSV, Excel, API, PostgreSQL).
- Проверять и валидировать данные (дубликаты, пропуски, выбросы).
- Очищать и предварительно обрабатывать данные (кодирование, масштабирование, работа с датами).
- Выполнять базовый анализ (статистики, тренды, аномалии).
- Строить и обучать простые модели машинного обучения (регрессия, классификация).
- Генерировать отчеты (PDF, Excel) и визуализации (Matplotlib, Seaborn, Plotly).
- Автоматически отправлять отчеты по email.
- Планировать регулярный запуск с помощью планировщика задач.
- Вести логирование всех этапов обработки.
- Интегрироваться с внешними системами и сохранять результаты в БД.
- Иметь полную документацию и юнит-тесты.

02 Назначение файлов

- `main.py`: Точка входа в проект. Запускает полный цикл обработки: загрузка → валидация → очистка → анализ → ML → отчетность.
- `src/data_loader.py`: Содержит функции `load_csv`, `load_excel`, `load_from_api`, `load_from_db` для загрузки данных из разных источников.
- `src/data_validator.py`: Содержит функции `validate_duplicates`, `validate_missing_values`, `detect_outliers_iqr`, `detect_outliers_zscore` для проверки данных.
- `src/data_cleaner.py`: Содержит функции `handle_missing_values`, `remove_duplicates`, `encode_categorical`, `scale_features`, `convert_date_column` для очистки и преобразования данных.
- `src/data_analyzer.py`: Содержит функции `calculate_basic_stats`, `analyze_time_series`, `detect_anomalies` для анализа данных.
- `src/ml_model.py`: Содержит функции `train_regression_model`, `train_classification_model` для построения и оценки моделей.
- `src/report_generator.py`: Содержит функции `generate_visualizations`, `generate_pdf_report`, `send_email_with_attachment` для отчетности.
- `src/scheduler.py`: Содержит функции для настройки регулярного запуска `run_pipeline` через `schedule`.
- `src/logger.py`: Содержит функцию `setup_logger` для настройки логирования в файл.
- `tests/*.py`: Содержат юнит-тесты для ключевых компонентов.
- `config/config.json`: Хранит настройки подключений к БД, API, email и другим внешним сервисам.
- `requirements.txt`: Список всех необходимых Python-библиотек для установки.
- `README.md`: Файл с описанием проекта, структурой и инструкциями по запуску.

03 Зависимости

- Python 3.8+
- pandas
- numpy
- requests
- openpyxl
- sqlalchemy
- psycopg2-binary
- scikit-learn
- matplotlib
- seaborn
- plotly
- reportlab
- pytest
- statsmodels

04 Установка и запуск

Для запуска проекта необходим Python 3.8+ и установленные зависимости из `requirements.txt`.

05 Установка зависимостей:

1. Откройте терминал в папке проекта (где лежит `main.py`).
2. (Рекомендуется) Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   # Активация (Windows):
   venv\Scripts\activate
   # Активация (macOS/Linux):
   # source venv/bin/activate
   ```

   06 Установите зависимости:
   pip install -r requirements.txt

   07 Запуск проекта:
   python main.py

   08 Запуск тестов:
   pytest
  
   
   
