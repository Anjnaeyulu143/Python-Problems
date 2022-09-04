
def solve(nums_arr,k):
      
    i = cur_sum = max_sum = 0
    n = len(nums_arr)
    
    for j in range(n):
        
        cur_sum += nums_arr[j]
        max_sum = max(max_sum,cur_sum)
        
        if (j-i+1) == k :            
            cur_sum -= nums_arr[i]
            
            i +=1
            
    print(max_sum)
    





if __name__ == "__main__":
    nums_arr = [10,3,0,4,15]
    
    k =3
    
    solve(nums_arr,k) 