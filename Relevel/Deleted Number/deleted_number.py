x = [int(i) for i in input().strip().split()]
n = x[0]
o = x[1]
m = x[1]
l = x[1]
arr = [int(i) for i in input().strip().split()]

while(m in arr):
    m=m+1

while(l in arr):
    l=l-1

if(m-o < o-l):
    print(m)
else:
    print(l)