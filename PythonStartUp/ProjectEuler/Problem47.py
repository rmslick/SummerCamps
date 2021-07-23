a,b,c,d=1,2,3,4
#a,b,c=1,2,3
def prime(x):
    if x==1:
        return False
    if x==0:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def prime_divisors(x):
    array=[]
    for i in range(2,x):
        if x%i==0 and prime(i):
            array.append(i)
    return array
while True:
    if len(prime_divisors(a))==4:
        if len(prime_divisors(b))==4:
            if len(prime_divisors(c))==4:
                if len(prime_divisors(d))==4:
                    print(a)
                    exit()
    a+=1
    b+=1
    c+=1
    d+=1
'''
while True:
    if len(prime_divisors(a))==3:
        if len(prime_divisors(b))==3:
            if len(prime_divisors(c))==3:
                print(a)
                exit()
    a+=1
    b+=1
    c+=1'''