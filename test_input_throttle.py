import requests
import time
from signal import signal, SIGINT
from sys import exit

throttle_speed = 0.05

url = '5001/api/manual_drive'
man_drive_init = {
  "angle": 0.0,
  "throttle": 0.0,
  "max_speed": 0
}

man_drive_throttle = {
  "angle": 0.0,
  "throttle": throttle_speed,
  "max_speed": 0
}

def end_handler(signal_received, frame):
    # Handle any cleanup here
    print('CTRL-C detected. Exiting throttle test.')
    exit(0)

if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is received
    signal(SIGINT, end_handler)

    print('Running. Press CTRL-C to exit.')
    while True:
      # this is meant to be if key is up arrow
      if input() == '^[[A':
        x = requests.post(url, json = man_drive_throttle)
        print('Set throttle to {throttle_speed}.')
        time.sleep(0.1)
      else:
        x = requests.post(url, json = man_drive_init)  
        print('Set fields to zero.')


