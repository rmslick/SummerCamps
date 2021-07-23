def sub(x):
    x=str(x)
    array=[]
    mini=[]
    for i in range(len(x)):
        for j in range(len(x),i,-1):
            array.append(x[i:j])
    for i in range(len(array)):
        array[i]=int(array[i])
    for i in range(len(array)):
        if array[i]%3==0:
            mini.append(array[i])
    if len(mini)%3==0:
        return True
    else:
        return False
counter=-1
d=2
for i in range(10**(d-1),(10**d)+1):
    if sub(i):
        counter+=1
print(counter)