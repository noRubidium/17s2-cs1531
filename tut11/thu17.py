"""
Exception
"""
# try:
#     j = int(input("Give me a number: "))
# except ValueError:
#     print("invalid input")
#     exit()
# #
# try:
#     i = 5 / j
# #     i = 5 / (j + 1)
#     print("5 / %f is: %f\n" % (j, i))
# except ZeroDivisionError as e:
#     print("division by zero")
#
# f = open("DOESNT_EXIST_!", "r")
# IOError
#     - FileNotFoundError
# ImportError
# ValueError
# EOFError
# try:
#     while True:
#         input()
# except EOFError:
#     print("End of input")
# AssertionError


# class AssertEqualError(Exception):
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b
#
#     def __str__(self):
#         return ("Test failed: Expected: %s, got %s" %
#             (str(self.__b), str(self.__a)))
#
#
# def add(a, b):
#     return 8
#
# def assertEqual(a, b):
#     try:
#         assert a == b
#     except AssertionError as e:
#         raise AssertEqualError(a, b)
#
# assertEqual(add(5, 3), 8)
# assertEqual(add(3, 3), 6)
# print("All test passed, you are awesome!")
#
# def f():
#     try:
#         f = open("input_file", "r")
#         numerator = int(f.readline())
#         denominator = int(f.readline())
#         result = numerator / denominator
#     except FileNotFoundError:
#         print("File input_file doesn't exist")
#     except ValueError:
#         print("file needs to contain two numbers")
#     except EOFError:
#         print("Not enough numbers")
#     except ZeroDivisionError:
#         print("division by zero is not possible")
#     else:
#         print("The result is %f" % result)

# try:
#     f()
# except ZeroDivisionError:
#     print("Division by zero")
# while True:
#     try:
#         """"""
#         input()
#     except:
#         print("HI!")
"""
Testing
Quote of the day fromDijkstra:
Program testing can be used to show the presence
 of bugs, but never to show their absence!
"""
import unittest

class InterestRateTooLowError(Exception):
    pass

def calculate_interest(p, n, r):
    if r < 5:
        raise InterestRateTooLowError
    return p * n * r / 100
#
# def assertEqual(a, b):
#     try:
#         assert (a == b)
#     except AssertionError:
#         print("See value: " + str(a) + " expected: " + str(b))
#         exit()
#
def assertException(a, exception_class):
    try:
        a()
    except exception_class:
        pass
    else:
        print("Expected exception: " + str(exception_class.__name__))
        exit()
#
# def test_fun():
#     calculate_interest(1000, 5, 4)
#
# assertEqual(calculate_interest(1000, 5, 5), 250)
# assertException(test_fun, InterestRateTooLowError)
#
# # print("All tests passed you are awesome!")
# import unittest
#
class TestInvestment(unittest.TestCase):
    def setUp(self):
        self.principal = 1000
        self.interest = 5
        self.years = 5

    def test_function_calc_interest(self):
        self.assertEqual(calculate_interest(self.principal, self.years, self.interest), 250)

    def test_exception(self):
        with self.assertRaises(InterestRateTooLowError):
            calculate_interest(self.principal, self.years, 4)

if __name__ == '__main__':
    unittest.main()

"""
Testing with Exception
"""
