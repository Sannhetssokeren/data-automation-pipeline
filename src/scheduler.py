import schedule
import time
import subprocess
from .logger import setup_logger

logger = setup_logger('scheduler', 'logs/pipeline.log')

def run_pipeline():
    subprocess.run(["python", "main.py"])
    logger.info("Pipeline executed via scheduler")

def setup_scheduler():
    schedule.every().day.at("10:00").do(run_pipeline)
    while True:
        schedule.run_pending()
        time.sleep(60)