import time
import webbrowser

# Countdown for 30 seconds
for i in range(1, 31):
    print(f"{i} seconds passed")
    time.sleep(1)

# Wait for another 30 seconds
time.sleep(30)

# Open web browser and search for youtube.com
webbrowser.open("https://www.youtube.com/")
