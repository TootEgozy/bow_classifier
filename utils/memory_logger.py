import os
import psutil
from dotenv import load_dotenv

def log_memory():
    load_dotenv()
    include_memory_logs = os.getenv("INCLUDE_MEMORY_LOGS", "False") == "True"
    if include_memory_logs:
        process = psutil.Process(os.getpid())
        print(f"Memory usage: {process.memory_info().rss / 1024 ** 2:.2f} MB")