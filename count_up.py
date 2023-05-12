import time

def clock():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        print(f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
        time.sleep(1)
