def decimaltobinary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def binarytodecimal(binary):
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

#Stack Overflow super efficent methods
def decimaltobinary2(decimal):
    binary = bin(decimal)[2:]
    return binary

def binarytodecimal2(binary):
    decimal = int(binary, 2)
    return decimal
