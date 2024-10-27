# limit: 80 requests per 15 minutes

"""
write an internal state for the backend which is consisted of:

request_counter: a variable to count requests
max_requests: adjustable from the process env
requests_timer: a counter of 15 minutes
requests_blocked: a boolean variable

on app starts, start the 15 minutes counter.
on each request, call the check_update_requests_limit function.

check_update_request_limit():
check if timer is still counting down and add 1 to request_counter, then check if it's below minimum.
if so, proceed.
if the counter is done but request is below minimum, restart the timer and the request counter to 1, proceed.
if the
"""


import os
import threading
import time

from dotenv import load_dotenv

load_dotenv()

max_requests = int(os.environ.get('MAX_REQUEST_COUNT') or 80)
time_frame = int(os.environ.get('REQUESTS_TIME_FRAME') or 900)

requests_count = 0
timer = 0
requests_blocked = False

def reset_counter():
    global request_count
    print("timeframe window ended, Request count reset")
    request_count = 0
    start_timer()

def start_timer():
    global timer
    timer = threading.Timer(time_frame, reset_counter)
    timer.start()

def handle_request():
    global max_requests
    global request_count
    global timer
    global requests_blocked

    request_count += 1
    if request_count == max_requests:
        print('limit reached')

start_timer()