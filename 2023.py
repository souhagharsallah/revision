t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    p=1
    l1=list()
    for i in l:
        p=p*i
    if (2023%p!=0):
        print("NO")  
    else:
         print('yes')
         j=2023//p   
         l1.append(j)
         for k in range(k-1):
             l1.append(1)
    for i in l1:
        print(i,"",end="")         