x,y=map(int,input().split())
s=((x*1)+(y*2))
if x==0 and y%2==0:
    print("YES")
elif(x==0 and y%2!=0):
    print("NO")
elif s%2==0:
    print("YES")
else:
    print("NO")