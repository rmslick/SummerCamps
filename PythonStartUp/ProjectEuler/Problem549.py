import math as m
i=2
n=2
ans=0
end=10**8
while True:
    if n==end+1:
        break
    if m.factorial(i)%n==0:
        ans+=i
        n+=1
        i=2
    else:
        i+=1
print(ans)