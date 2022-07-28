def is_prime(n):
    
    boolean_prime_list = [True for i in range(n+1)]
    a = 2
    
    while (a*a <= n):
        if (boolean_prime_list[a] == True): 
            
            for i in range(a*a,n+1,a):
                boolean_prime_list[i] = False
    
        a += 1
    
    for i in range (2,n+1):
        if boolean_prime_list[i] == True:
            print(i)
    
n = int(input())
is_prime(n)
