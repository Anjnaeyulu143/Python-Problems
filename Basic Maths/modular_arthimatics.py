# Modular arthimatics


n = int(input())
m = int(input())
b = int(input())


res = 1 

while (m>0):
    if (m%2 != 0):
        res = (res * (n % b))%b 
    
    n = ((n%b)*(n%b))%b
    m = m//2
print(res)
