# Delete mid element from the array using recurrsion .


# Explanation..

# Through BHI method 

# Base Condition >> Hypothesis >> Induction 


# Base Condition :  --  if k == 1 then we remove that element from the stack 


# Hypothesis : -- We need to remove last element and decreament k..


def delete(nums_arr,k):
    
    if (k == 1):
        nums_arr.pop()
        return
    
    temp = nums_arr.pop()
    
    delete(nums_arr,k-1)
    
    nums_arr.append(temp)



def middle(nums_arr):
    mid = (len(nums_arr)//2 )+ 1

    delete(nums_arr,mid)




if __name__ == "__main__":
    nums_arr = [1,10,-1,25,3]
    
    middle(nums_arr)
    
    print(nums_arr)