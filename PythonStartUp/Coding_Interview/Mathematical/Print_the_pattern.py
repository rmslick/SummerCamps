import sys
def solve(x):
    c=x
    x+=1
    for a in range(x):
        x-=1
        for i in range(c,0,-1):
            for j in range(x):sys.stdout.write(str(i)+" ")
        if x!=1:sys.stdout.write("$")
solve(3)