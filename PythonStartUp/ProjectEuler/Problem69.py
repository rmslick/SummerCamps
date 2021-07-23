answer=dict()
def factors(n):
    array=[]
    for i in range(2,n+1):
        if n%i==0:
            array.append(i)
    return array

def common(x):
    relPrime=[1]
    for i in range(2,x):
        b=0
        for j in range(len(factors(i))):
            if factors(i)[j] in factors(x):
                b=-1
                break
        if b==0:
            relPrime.append(i)
    num_of_rp=len(relPrime)
    final=x/num_of_rp
    answer[x]=final

for i in range(2,1000001):
    common(i)

print(answer)
max_key=max(answer,key=answer.get)
print(max_key)