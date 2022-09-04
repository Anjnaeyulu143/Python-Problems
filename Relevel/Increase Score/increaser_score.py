narr = [int(i)  for i in input().strip().split()]
n=narr[0]
m=narr[1]
k=narr[2]
arr= [int(i)  for i in input().strip().split()]

mynum = arr[k-1]

arr.sort()

if(len(arr)%2!=0):
    median = int((len(arr)+1)/2)
else:
    median = int(len(arr)/2)

midIndex = median-1
medianMark = arr[midIndex]
if(medianMark > mynum):
    print(medianMark)
elif(medianMark < mynum):
    print(m)
else:
    print(median)