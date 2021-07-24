from sense_hat import SenseHat
from time import sleep
import random
from datetime import datetime
sense=SenseHat()
sense.clear()
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,165,0)
white=(255,255,255)
time=datetime.now()
current_time=time.strftime("%H:%M:%S")
sense.show_message(str(time))