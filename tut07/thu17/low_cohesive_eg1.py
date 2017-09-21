def get_num():
    return int(input("Enter a number: "))


def add(num_1, num_2):
    return num_1 + num_2


num_1 = get_num()
num_2 = get_num()
result = add(num_1, num_2)
print ("The sum of the numbers is: %d" % (result))
