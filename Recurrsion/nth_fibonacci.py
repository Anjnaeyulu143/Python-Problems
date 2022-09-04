def nth_fibonacci(n):
    if (n <= 1):
        return n
    
    partial_ans1 = nth_fibonacci(n-1)
    partial_ans2 = nth_fibonacci(n-2)
    
    return partial_ans1 + partial_ans2



if __name__ == '__main__':
    n = 6 
    result = nth_fibonacci(n)
    print(result)