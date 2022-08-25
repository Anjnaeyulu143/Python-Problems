def insert_list(nums_list,b):
    
    if (len(nums_list) == 0) or (b >= nums_list[len(nums_list)-1]):
        
        nums_list.append(b)
        return
    
    temp = nums_list.pop()
    
    insert_list(nums_list,b)
    
    nums_list.append(temp)



def sort_recursion(nums_list):
    
    if (len(nums_list) <= 1):
        return
    
    b = nums_list.pop()
    
    sort_recursion(nums_list)
    
    insert_list(nums_list,b)




if __name__ == "__main__":
    nums_list = [29,1,10,51,100]
    sort_recursion(nums_list)
    print(nums_list)