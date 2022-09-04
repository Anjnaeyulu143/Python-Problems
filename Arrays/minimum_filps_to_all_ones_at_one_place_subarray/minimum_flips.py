def solve(n):
    N = len(n)
    
    cnt = 0
    ones_cnt = 0 
    min_ones_cnt = N
    
    for i in range(N):
        
        if n[i] == 1:
            ones_cnt+=n[i]
           
        
    # print(ones_cnt)
    pointer1=pointer2=0
    
    
    while pointer2 < N:
        
        while pointer2 < N and pointer2-pointer1 < ones_cnt:
            # print(pointer2,ones_cnt)
            if n[pointer2] == 0:
                cnt += 1
                # print('pointer-2',cnt,pointer2,min_ones_cnt)
            pointer2 += 1
        
        min_ones_cnt = min(min_ones_cnt,cnt)
                    
        
        if n[pointer1] == 0:
            
            cnt -= 1
            # print('pointer-1',cnt)
        pointer1 += 1  
        
        # min_ones_cnt = min(min_ones_cnt,cnt)
    print(min_ones_cnt)
    
if __name__ == '__main__':
    n = [1,1,1,1,1,1,1,0,1]
    
    solve(n)