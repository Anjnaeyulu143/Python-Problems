def sum_of_n(n):
    if (n==1):
        return n 
    
    partial_ans = sum_of_n(n-1)
    
    return n + partial_ans



if __name__ == '__main__':
    n = 5
    result = sum_of_n(n)
    print(result)