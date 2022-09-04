t = int(input())
while(t):
    n = int(input())
    arr = [int(i) for i in input().strip().split()]
    mini = min(arr)
    maxx = max(arr)
    print(maxx-mini)
    t = t- 1