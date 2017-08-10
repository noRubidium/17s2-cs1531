print('Hello World!')
"""
    scripting langauge
"""
"""
l = list()
l = [1, 3, 4, 5]
l.append(3)

if 2 in l:
    print('Something went wrong!')
else:
    d = {'Ben': ['COMP1511', 'COMP1531'], 'Anna': ['COMP1511', 'COMP1531', 'COMP2041']}

    print('Anna enrolled in: ', ', '.join(d['Anna']))
"""


# def sum_expo(n):
#     """
#         :param n int, number we summing the exponetials on
#     """
#     result = 0
#     for v in range(n):
#         result += n ** (v + 1)
#     return result
#
# import sys
# s = sys.stdin.read()
# num = int(s)
# print(sum_expo(num))


# def is_unique(s):
#     words = s.split(' ')
#     print(words)
#     while len(words) != 0:
#         word = words.pop()
#         if word in words:
#             return False
#     return True

'Johnson is eating a cake'
'cake'
'stone'

def find_and_replace(text, old_word, new_word):
    words = text.split(' ')
    new_s = []
    for word in words:
        if word == old_word:
            new_s.append(new_word)
        else:
            new_s.append(word)
    return ' '.join(new_s)
    # return new_word.join(text.split(old_word))

import sys
s = sys.stdin.readline().rstrip()
print(find_and_replace('Johnson is eating a cake', 'John', 'Jack'))
