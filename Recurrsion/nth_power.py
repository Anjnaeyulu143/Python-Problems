def nth_power(m,n):
    if (n==0):
        return 1
    
    temp = nth_power(m,n//2)
    
    if (n%2 != 0):
        return (temp * temp ) * m
    
    else:
        return temp * temp



if __name__ == '__main__':
    
    x = 2
    y = 5 
    
    result = nth_power(x,y)
    print(result)