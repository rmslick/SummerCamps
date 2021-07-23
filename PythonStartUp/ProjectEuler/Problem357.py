sum=0
def divisors(x):
    array=[]
    for i in range(1,x+1):
        if x%i==0:array.append(i)
    return array
def prime(x):
    if x==1:return False
    if x==0:return False
    for i in range(2,x):
        if x%i==0:return False
    return True
for i in range(1,100000001):
    l=0
    a=divisors(i)
    for j in range(len(a)):
        if a[j]+(i/a[j])==int(a[j]+(i/a[j])):
            y=int(a[j]+(i/a[j]))
            if prime(y)==False:
                l=1
                break
    if l==0:
        sum+=i
print(sum)