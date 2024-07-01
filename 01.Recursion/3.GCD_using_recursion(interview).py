#We are using the Euclidean algorithm to find the Greatest Common Divisor of two number..
def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

a=input('num1:')
b=input('num2:')

print(GCD(int(a), int(b)))