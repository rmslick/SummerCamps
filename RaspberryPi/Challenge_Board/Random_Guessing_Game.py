from sense_hat import SenseHat
from time import sleep
import random
sense=SenseHat()
sense.clear()
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
array=[green,yellow,blue,red,pink]
a=random.randint(1,101)
num=2.55
#print(a) #Uncomment for the computer to print the answer immediately after running
while True:
  x=int(input("Enter a number 1-100:"))
  if x>a:
    ans=x-a
    ans=float(ans)
    ans*=num
    ans=int(ans)
    if ans<9:
      ans=9
    sense.clear((ans,0,0))
  elif x<a:
    ans=a-x
    ans=float(ans)
    ans*=num
    ans=int(ans)
    if ans<9:
      ans=9
    sense.clear((0,0,ans))
  else:
    sense.show_message("You got the number!",text_colour=green,back_colour=red)