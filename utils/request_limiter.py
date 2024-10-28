import os
import threading

from dotenv import load_dotenv

load_dotenv()


class RequestLimiter:
    def __init__(self):
        self.max_requests = int(os.environ.get('MAX_REQUEST_COUNT') or 80)
        self.time_frame = int(os.environ.get('REQUESTS_TIME_FRAME') or 900)
        self.request_count = 0
        self.timer = None
        self.requests_blocked = False

        self.start_timer()

    def start_timer(self):
        print('starting timer')
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.time_frame, self.reset_counter)
        self.timer.start()

    def reset_counter(self):
        print('resetting counter')
        self.request_count = 0
        self.requests_blocked = False
        self.start_timer()

    def start_timeout(self):
        self.requests_blocked = True
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.time_frame, self.reset_counter)
        self.timer.start()

    # return True if Blocked, Block if limit reached, or return False if limit not reached
    def check_handle_limit_reached(self):
        if self.requests_blocked:
            return True

        self.request_count += 1
        print(self.request_count)
        if self.request_count == self.max_requests:
            print('maximum requests reached')
            self.start_timeout()
            return True

        else:
            return False
