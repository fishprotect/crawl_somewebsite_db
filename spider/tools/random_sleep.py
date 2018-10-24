import random
import time

def random_sleep_time():
    x = random.randint(5,15)
    x = x*0.1
    time.sleep(x)
