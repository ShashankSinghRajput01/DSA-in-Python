def gcd(a, b):
    while b!=0:
        a, b = b, a % b
    return a


num1 = 60
num2 = 48
print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")