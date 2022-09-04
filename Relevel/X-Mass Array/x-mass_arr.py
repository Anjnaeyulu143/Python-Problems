testC = int(input())
while(testC):
  count=0;
  narr = [int(i) for i in input().strip().split()]
  arr =  [int(i) for i in input().strip().split()]
  n = narr[0]
  x = narr[1]
  c=[]
  j=0
  for i in range(n-1):
    if(arr[i]+arr[i+1] > x ):
      j=(arr[i]+arr[i+1] - x)
      arr[i+1] = arr[i+1] -j ;
      count=count+1
      c.append(j)
  print(sum(c))
  testC= testC-1 