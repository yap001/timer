import time

timer = 0

while timer < 9000:
    print("Timer:", timer, "seconds")
    time.sleep(1) # wait for 1 second
    timer += 300 # add 5 minutes to the timer (300 seconds)
    
print("Timer reached 9000 seconds")
