n = int(input())
arr = (int(i) for i in input().strip().split())
stack = []
count = 0;

l = []
for i in range(n):
    if (arr[i] not in stack):
        stack.append(arr[i])
        count = count+1
        if (len(stack) == 2):
            l.append(stack)
            count = 0;
            stack = []
            
print(len(l))