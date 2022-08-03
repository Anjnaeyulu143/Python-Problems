def find_factors(n):
    if (n==1):
        return n
    
    partial_ans = find_factors(n-1)
    
    return n * partial_ans



if __name__ == '__main__':
    n = 5 
    result = find_factors(n)
    print(result)