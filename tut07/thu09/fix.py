# Read input
def read_number(msg):
    return float(input(msg))

def read_int(msg):
    return int(read_number(msg))

# compute output
def add(num_1, num_2):
    addition = num_1 + num_2
    return addition

num_1 = read_int("Enter number one: ")
num_2 = read_int("Enter number two: ")
print("Sum: " + str(add(num1, num2)))
