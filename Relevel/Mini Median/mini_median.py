n  = int(input())
arr =[int(i) for i in input().strip().split()]
arr.sort()
md1 = arr[int(n/2)-1]
md2 = arr[int(n/2)]

print(min(md1,md2))