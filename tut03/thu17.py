

def main():
    print('Hello World!')
    names = ['Minjie', 'DT', 'HC']
    for name in names:
        print(name)

    # print(num_expo(2))
    s = 'Hello this is Jack'
    print(is_unique(s))

d =  {'Ben': ['COMP1511', 'COMP1531'], 'Anna': ['COMP1521']}
d['Ben']
d.get('Jack', [])

def is_unique(s):
    words = s.split(' ')
    word_dict = dict()
    for word in words:
        if word in word_dict:
            return False
        word_dict[word] = True
    return True



def num_expo(n):
    result = 0
    for exp in range(n):
        result += n ** (exp + 1)
    return result

if __name__ == '__main__':
    main()
