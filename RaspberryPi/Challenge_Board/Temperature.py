from sense_hat import SenseHat
from time import sleep
import random
sense=SenseHat()
sense.clear()
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,165,0)
white=(255,255,255)
temp=sense.get_temperature()
a=(temp*1.8)+32
a=round(a,1)
if a>=70:
  sense.show_message(str(a),back_colour=red)
else:
  sense.show_message(str(a),back_colour=red)