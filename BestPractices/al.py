
def is_reptitative_sum (n,temp):
    if n == 0:
        return temp
    temp = temp + n%10
    return is_reptitative_sum(n//10,temp)
n = int(input())
temp = 0
result = is_reptitative_sum(n,temp)
while result > 9:
    result = is_reptitative_sum(result,temp) 
if result == 1:
    print(1)
else:
    print(0)