import os
import threading
import atexit

from dotenv import load_dotenv

load_dotenv()

# Dependency class to unload the huge learning_data object from memory
# if no requests are sent within a time frame.
class MemoryUnloader:
    def __init__(self, app):
        self.time_frame = int(os.environ.get("MEMORY_DROP_TIME_FRAME") or 900)
        self.timer = None
        self.app = app

    def reset_timer(self):
        print("Memory Unloader: resetting timer")
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.time_frame, self.unload)
        self.timer.start()

    def unload(self):
        print("Memory Unloader: unload memory")
        # with self.app.app_context():
        unload = self.app.config['unload_learning_data'];
        threading.Thread(target=unload).start()
        self.reset_timer()

    def stop_timer(self):
        if self.timer:
            self.timer.cancel()

    atexit.register(stop_timer)