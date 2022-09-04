

def solve(string,substring):
    
    dict_anagrams = dict()
    n = len(string)
    
    for i in substring:
        dict_anagrams[i] = dict_anagrams.get(i,0) + 1

    cnt = len(dict_anagrams)
    
    i = j = ans = 0
    
    while j < n:
        
        if string[j] in dict_anagrams:
            dict_anagrams[string[j]] -= 1;
            if dict_anagrams[string[j]] == 0:
                cnt -= 1

        if (j-i+1) < len(sub_string):
            j += 1
        
        elif (j-i+1) == len(substring):  
            if cnt == 0:
                ans += 1
            if string[i] in dict_anagrams:
                dict_anagrams[string[i]] += 1
                if dict_anagrams[string[i]] == 1:
                    cnt += 1
            
            i += 1
            j += 1
          
    print(ans)


if __name__ == "__main__":
    string = "aaababaaba"
    
    sub_string = "aaba"
    solve(string,sub_string)