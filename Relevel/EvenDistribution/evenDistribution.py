def evenDistribution(m,arr):
    length = len(arr)-1
    
    if ((length+1)%m != 0):
        print("NO")
        return
        
    i = 0

    while i <= length:
        if ((arr[i] + arr[i+1]) % m == 1):
            print('NO')
            return
        i += 2
        
    print('YES')
    


n = int(input())


for i in range(n):
    m = int(input())
    arr = list(map(int,input().split()))
    evenDistribution(m,arr)