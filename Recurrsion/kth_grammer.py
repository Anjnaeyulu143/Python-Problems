def grammer(n,k):
    
    if (k==1 and n==1):
        return 0 
    
    a = k%2 
    
    if ( a == 0):
        return grammer(n-1, k//2)
    
    else:
        
        result = grammer(n-1,(k+1)//2)
        if result == 0:
            return 1
        else:
            return 0
        
    
    # power = 2 ** (n-1)
    
    # mid = power//2
    # print('POWER', power)
    
    # print('MID',mid)
    
    # if (k <= mid):
    #     return grammer(n-1,k)
    
    # else:
    #     result = grammer(n,k-mid)
        
    
if __name__ == "__main__":
    
    n = 4
    k = 7
    
    result = grammer(n,k)
    if(result == 0):
        print(1)
    else:
        print(0)