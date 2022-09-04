
def solve(nums_arr,k):
    max_nums_list = []
    
    for i in range(k):
        while len(max_nums_list) != 0 and nums_arr[i] > max_nums_list[0]:
            max_nums_list.pop(0)
        
        max_nums_list.append(nums_arr[i])
        # print(i)
        # k = 2
        
        # while len(max_nums_list) > 1 and k < len(max_nums_list):
        #     print(max_nums_list)
        #     print(len(max_nums_list))
        #     if (max_nums_list[k-1]) > (max_nums_list[k]):
        #         max_nums_list[k],max_nums_list[k-1] = max_nums_list[k-1],max_nums_list[k]
        #     k += 1
            
        
    res = [max_nums_list[0]]

    for j in range(k,len(nums_arr)):
        if (nums_arr[j-k]) == (max_nums_list[0]):
            max_nums_list.pop(0)
            
        while len(max_nums_list) != 0 and max_nums_list[0] < nums_arr[j]:
            max_nums_list.pop(0)
        max_nums_list.append(nums_arr[j])
        
        # k = 2
        
        # while len(max_nums_list) > 1 and k < len(max_nums_list):
        #     if (max_nums_list[k-1]) > (max_nums_list[k]):
        #         max_nums_list[k],max_nums_list[k-1] = max_nums_list[k-1],max_nums_list[k]
        #     k += 1
        
        res.append(max_nums_list[0])
        
    print(res)
        
if __name__ == '__main__':
    nums_arr = [1,2,3,1,4,5,2,3,6]
    k = 3
    
    solve(nums_arr,k)
    