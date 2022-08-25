# Time Complexity O(N)


def solve(n,k):
    
    N = len(n)
    pointer1=pointer2=cnt=0
    product = 1
    
    
    while pointer2 < N:
        
        product*=n[pointer2]
        
        while pointer1 < pointer2 and product >= k:
            product/=n[pointer1]
            pointer1+=1
 

        length = pointer2-pointer1 + 1
        
        cnt+=length
        
        pointer2+=1
    print(cnt)

if __name__ == '__main__':
    n = [1,2,3,4,5]
    k = 30
    solve(n,k)