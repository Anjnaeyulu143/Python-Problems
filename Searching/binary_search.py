# Binary Search T.C is O(log n)


def binary_serach(arr,n):
    
    start_index = 0
    end_index = len(arr) - 1
    mid = start_index + (end_index - start_index)//2
    
    while (start_index <= end_index):
        
        if (arr[mid] == n):
            return mid
        
        elif (arr[mid] > n):
            end_index = mid-1
        
        elif (arr[mid] < n):
            start_index = mid+1
        
        mid = start_index + (end_index - start_index)//2
        
    return -1
        

if __name__ == '__main__':

    even_nums_list = [2,4,5,6,17,20]

    odd_nums_list = [17,18,20,22,25]

    n = int(input())

    result = binary_serach(odd_nums_list,n)

    print(result)