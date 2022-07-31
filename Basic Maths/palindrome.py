def palindrome(n):
    temp = n
    reverse_digit = 0
    
    while (n>0):
        rem = n%10
        reverse_digit = reverse_digit * 10 + rem
        n //= 10
    if (temp == reverse_digit):
        return True
    else:
        return False
    
if __name__ == '__main__':
    
    n = int(input())

    result = palindrome(n)

    if result:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")
