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
brown=(139,69,19)
weird=(0,0,9)
sense.clear(weird)
a=1
for i in range(1,6):
  for j in range(1,6):
    if j==4:
      sense.set_pixel(i,j,white)
    elif j==5:
      sense.set_pixel(i,j,brown)     
    else:
      sense.set_pixel(i,j,yellow)
sense.set_pixel(3,4,red)
sense.set_pixel(4,6,yellow)
sense.set_pixel(4,7,yellow)
sense.set_pixel(2,6,yellow)
sense.set_pixel(2,7,yellow)
sense.set_pixel(2,2,white)
sense.set_pixel(4,2,white)
sense.set_pixel(6,3,yellow)
sense.set_pixel(7,3,yellow)
sense.set_pixel(0,3,yellow)
sleep(0.5)
while True:
  a+=1
  if a%2==0:
    sense.set_pixel(5,6,yellow)
    sense.set_pixel(4,7,weird)
    sense.set_pixel(7,2,yellow)
    sense.set_pixel(7,3,weird)
    sense.set_pixel(7,4,weird)
    sense.set_pixel(2,2,white)
    sleep(0.5)
    sense.set_pixel(5,6,weird)
    sense.set_pixel(4,7,yellow)
    sense.set_pixel(7,2,weird)
    sense.set_pixel(7,4,yellow)
    sense.set_pixel(2,2,yellow)
    sleep(0.5)
  else: 
    sense.set_pixel(1,6,yellow)
    sense.set_pixel(2,7,weird)
    sense.set_pixel(7,2,yellow)
    sense.set_pixel(7,3,weird)
    sense.set_pixel(7,4,weird)
    sense.set_pixel(2,2,white)
    sleep(0.5)
    sense.set_pixel(1,6,weird)
    sense.set_pixel(2,7,yellow)
    sense.set_pixel(7,2,weird)
    sense.set_pixel(7,4,yellow)
    sense.set_pixel(2,2,yellow)
    sleep(0.5)