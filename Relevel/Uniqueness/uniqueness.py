testCase = int(input())
while(testCase):
    n= int(input())
    arr = [int(i) for i in input().strip().split()]
    mini =0
    count = 0
    if(len(set(arr)) == len(arr)):
        print(count,min(arr))
    else:
          while(len(set(arr)) != len(arr)) :
              minx =min(arr)
              maxx =max(arr)
              arr.remove(maxx)
              mini = minx-maxx
              count = count +1
          print(count,mini)
    testCase=testCase-1