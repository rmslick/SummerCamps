import math as m
lower=5
upper=100
ans=0
def prime(x):
    for i in range(2,int(x/2)+1):
        if x%2==0:
            return False
    return True
for p in range(lower,upper):
    if prime(p):
        ans+=(m.factorial(p-1)+m.factorial(p-2)+m.factorial(p-3)+m.factorial(p-4)+m.factorial(p-5))%p
print("S(p) = "+str(ans)+" for "+str(lower)+" ≤ p < "+str(upper))