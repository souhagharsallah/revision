import math
t=int(input())
for i in range(t):
    s=0
    n=int(input())
    a= list(map(int, input().split()))
    for i in range(n):
        s=s+a[i]
    m=math.sqrt(s)
    if int (m) * int (m)==s:
        print("YES")
    else:
        print("NO") 
a=0


print ("hello sousou")
print ("hello ")