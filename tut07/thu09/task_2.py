# Read input
def read_number(msg):
    return float(input(msg))

def read_int(msg):
    return int(read_number(msg))

# Compute
def expo(num, exponent):
    answer = pow(num, exponent)
    return answer

num = read_int("Enter in a number: ")
exponent = read_int("Raise the number to the power of: ")
# output
print(expo(num, exponent))
