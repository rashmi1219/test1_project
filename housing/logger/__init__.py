import logging
import os
from datetime import datetime
LOG_DIR = "housing_log"
current_time = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_FILE_NAME = f"log_{current_time}.log"
os.makedirs(name=LOG_DIR,exist_ok=True)
file_path = os.path.join(LOG_DIR,LOG_FILE_NAME)
logging.basicConfig(filename=file_path,filemode="w",format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
