import os
import psutil
import time
import pandas as pd


def monitor_usage(duration=300, interval=5):
    pid = os.getpid()
    process = psutil.Process(pid)

    print(f"Monitoring resource usage for PID: {pid}")
    print(f"Duration: {duration} seconds, Interval: {interval} seconds")

    start_time = time.time()

    while time.time() - start_time < duration:
        # Get CPU and memory usage
        cpu_usage = process.cpu_percent(interval=interval)
        memory_info = process.memory_info()

        # Print the usage
        print(f"Time: {time.strftime('%H:%M:%S')}")
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_info.rss / (1024 * 1024):.2f} MB")  # RSS in MB
        print("-" * 30)


if __name__ == "__main__":
    monitor_usage()


def test_datafile_memory_usage():
    data = pd.read_csv('../learning_data/spam/spam_1.csv', encoding='latin1')
    print(f"Data shape: {data.shape}")
    print(f"Data memory usage: {data.memory_usage(deep=True).sum() / (1024 * 1024):.2f} MB")
