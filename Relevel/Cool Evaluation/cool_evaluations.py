def cool_number(i,maximum):
    x=y=1
    while x<maximum:
        while y<maximum:
            summation = 3*x*y+2*y+y
            if (summation == i):
                return True
            elif (summation < i):
                y+=1
            
            if (y==1 and summation > i):
                return False
            else:
                break

n = int(input())

for i in range(n):
    m = int(input())
    a = [int(i) for i in input().strip().split()]
    maximum = max(a)
    cnt = 0
    for i in a:
        is_cool = cool_number(i,maximum)
        if is_cool:
            cnt += 1
    print(cnt)