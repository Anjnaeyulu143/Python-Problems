def trailing_zeros(n):
    num_zeros = 0
    i = 5
    
    while (i <= n):
        num_zeros = num_zeros + n//i 
        i *= 5
   
    return num_zeros


if __name__ == '__main__':
    n = int(input())

    result = trailing_zeros(n)
    print(result)