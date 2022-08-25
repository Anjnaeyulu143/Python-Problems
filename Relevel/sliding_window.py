def cal_max_sub(arr,k):
    max_sum = cur_sum = 0
    
    for i in range (k):
        cur_sum += arr[i]
        
        max_sum = cur_sum
    
    for j in range (k, len(arr)):
        cur_sum = cur_sum - arr[j-k] + arr[j]
        
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum
    
    
    # for i in range(len(arr)):
    #     cur_sum += arr[i]
    #     max_sum = max(cur_sum,max_sum)
        
    #     if cur_sum < 0:
    #         cur_sum = 0
    
    # return max_sum

if __name__ == "__main__":
    nums_arr = [5,2,-1,6,-2,7,3]
    k = 3
    result = cal_max_sub(nums_arr,k)
    print(result)