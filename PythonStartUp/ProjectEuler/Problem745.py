from math import sqrt
array=[]
n=100
for i in range(1,n+1):
    for j in range(i,0,-1):
        if sqrt(j)==float(int(sqrt(j))):
            if i%j==0:
                array.append(j)
                #print("n: ",i,"ans: ",j)
                break
print("S("+str(n)+") = "+str(sum(array)))