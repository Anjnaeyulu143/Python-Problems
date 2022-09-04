def solve(A):
    N = len(A)
    
    cnt = min_l = 0 
    i = 0
    
    for i in range(N):
        if i==0:
            cnt+=1
            min_l+=cnt
        elif(i==N-1):
            if(A[i]>A[i-1]):
                cnt+=1
                min_l+=cnt
            else:
                cnt =1
                min_l+=cnt  
            
        elif (A[i]>A[i+1] or A[i]>A[i-1]):
            cnt+=1  
            min_l+=cnt
        elif(A[i]<A[i+1] and A[i]<A[i-1]):
            cnt=1
            min_l+=cnt
    print(min_l)

n = [int(i) for i in input().split()]
solve(n)
         