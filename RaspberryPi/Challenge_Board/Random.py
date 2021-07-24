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
array=[red,green,blue,yellow]
while True:
  sleep(0.5)
  for i in range(8):
    for j in range(8):
      sense.set_pixel(i,j,random.choice(array))