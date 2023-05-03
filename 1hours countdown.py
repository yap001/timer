import time
import winsound

def countdown_timer(seconds):
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timer = "{:2d}:{:2d}".format(m, s)
        print("Time remaining: " + timer, end="\r")
        time.sleep(1)
        seconds -= 1

    winsound.Beep(1000, 1000) # Beep sound when timer ends
    print("\nTime's up!")

if __name__ == '__main__':
    seconds = 60 * 60  # set the number of seconds for an hour
    countdown_timer(seconds)
