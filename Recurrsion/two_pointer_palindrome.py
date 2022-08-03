


def is_palindrome_helper(str,l,h):
    
    if (l>=h):
        return True
    
    elif str[l] != str[h]:
        return False
    
    return is_palindrome_helper(str,l+1,h-1)



if __name__ == '__main__':
    str_list = ["car","radar","noon","apple"]
    
    for str in str_list:
        l = 0
        h = len(str) - 1
        result = is_palindrome_helper(str,l,h)
        print(result)