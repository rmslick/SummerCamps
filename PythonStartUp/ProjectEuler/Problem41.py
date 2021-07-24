import itertools
array=[]
biggest=[0]

def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

for i in range(4,9):
    for j in range(1,i+1):
        array.append(str(j))
    perms=(list(itertools.permutations(array)))
    for h in range(len(perms)):
        perms[h]=int(''.join(perms[h]))
    for k in range(len(perms)):
        if prime(perms[k]):
            if perms[k]>max(biggest):
                biggest=[perms[k]]
    array=[]
print(max(biggest))