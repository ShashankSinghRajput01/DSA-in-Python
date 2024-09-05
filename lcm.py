def gcd(a, b):
    while b!=0:
        a, b = b, a % b
    return a
def lcm(a,b):
    lcm=(a*b)//gcd(a,b)
    return lcm

a=20
b=16
print(f"Lcm of {a} and {b} is: {lcm(a,b)} ")
