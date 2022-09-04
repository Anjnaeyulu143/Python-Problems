t = int(input())
while(t):
    n = [int(i) for i in input().strip().split()]
    x = n[1]
    ar = [int(i) for i in input().strip().split()]
    ar.sort(reverse=True)
    ans = 0
    count =1
    for i in range(0, len(ar)):
        if ar[i] * count > 2*x:
            ans += 1
            count = 1
        else:
            count += 1
    print(ans)
    t = t-1