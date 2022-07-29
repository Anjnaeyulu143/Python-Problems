def gcd(a,b):
    if (b == 0):
        return a
    return gcd(b,a%b)

n = int(input())
m = int(input())

result = gcd(n,m)

lcm = (n*m)//result

print("LCM OF THE GIVEN NUMBERS: ",lcm)
print("GCD OF THE GIVEN NUMBERS: ", result)