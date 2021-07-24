#Given non-zero two integers N and M. The problem is to find the number closest to N and divisible by M. If there are more than one such number, then output the one having maximum absolute value.

def closestNumber(n,m):
  #q quotient; n and m are the integers needed
  q = int(n/m)

  numOne = m * q
  #numbers cannot be = to zero, greater than only
  if((n * m) > 0):
    numTwo = (m * (q + 1))
  else:
    numTwo = (m * (q - 1))
  #abs = absolute value? 
  if(abs(n - numOne) < abs(n - numTwo)):
    return numOne

n = 100; m = 9
#print the function
print(closestNumber(n, m))
