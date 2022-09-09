arr = input()
count = 0
l =[]
length = len(arr)+2
for i in range(len(arr)):
    if(arr[i]=="<"):
        count = count+1
        l.append(count)
        length = length -1
    else:

        length = length-1
        l.append(length)
if(arr[-1] == ">"):
    l.append(l[-1]-1)
else:
    l.append(l[-1]+1)
print(sum(l))