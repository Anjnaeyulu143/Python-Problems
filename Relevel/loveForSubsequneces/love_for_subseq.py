n = int(input());
arr = [int(i) for i in input().strip().split()]
a=[]
def subs(arr,index,subarr):
    if(index == len(arr)):
        if(len(subarr) != 0):
            if(sum(subarr) %2 == 0):
                a.append(sum(subarr))
    else:
        subs(arr,index+1,subarr)
        subs(arr,index+1,subarr+[arr[index]])
    return
subs(arr,0,[])
print(max(a))