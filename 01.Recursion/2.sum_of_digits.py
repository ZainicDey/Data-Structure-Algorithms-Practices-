
def SumOfDigits(n):
    if n == 0:
        return 0;
    return n%10 + SumOfDigits(int(n/10))

n=input('Enter the number:')
print(SumOfDigits(int(n)))