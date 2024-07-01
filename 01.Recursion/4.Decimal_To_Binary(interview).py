def decimalToBinary(n):
    if n==0:
        return 0
    return 10*decimalToBinary(int(n/2))+n%2

n = input('Enter the decimal number:')
print(decimalToBinary(int(n)))