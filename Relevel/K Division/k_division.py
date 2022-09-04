narr = [int(i) for i in input().strip().split()]
n = narr[0]
k = narr[1]
arr =[int(i) for i in input().strip().split()]
count=0
rcount=-1

arr.sort()
summ=0
while(count<k):
    summ =summ+arr[rcount]-arr[count]
    rcount=rcount-1
    count=count+1
print(summ)