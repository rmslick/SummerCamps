n=3
ans=0
def ds(x):
    y=str(x)
    y=list(y)
    for i in range(len(y)):
        y[i]=int(y[i])
    for i in range(len(y)):
        a=y.copy()
        b=y
        del a[i]
        if b[i]==sum(a):
            return True
for i in range(10,10**n):
    if ds(i):
        ans+=i
print(ans)