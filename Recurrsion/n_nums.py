def n_nums(n):
    if (n == 1):
        print(1)
        return
        
    print(n)    
        
    n_nums(n-1)
    
    print(n)



if __name__ == "__main__":
    n = 5
    n_nums(n)