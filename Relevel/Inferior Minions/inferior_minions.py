n = int(input())
arr = [int(i) for i in input().strip().split()]
newarr = []
mini = arr[0]

for i in range(len(arr)):
    if(mini>arr[i]):
        newarr.append(mini-arr[i])
print(sum(newarr))