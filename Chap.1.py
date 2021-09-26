import re
import ast
from random import randrange, choice, randint
from itertools import permutations

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

# f = is_multiple(6, 4)
# print(f)

# is_even cannot use the multiplication, modulo, or division operators
def even_noob(k):
    if k == 0:
        return True
    if k < 0:
        k = -k
    while k > 0:
        k -= 2
        if k == 0:
            return True
    return False

def is_even(k):
    if k == 0:
        return True
    elif k > 0:
        return is_even(k-2)
    else:
        if k+2 > 0:
            return False
        else:
            return is_even(k+2)

def is_even2(k):
    if pow(-1, k) == 1:
        return True
    else:
        return False

def is_even3(k):
    if k == 0:
        return True
    if k < 0:
        k = -k
    for i in range(k):
        a, b = i, k-i
        if a == b:
            return True
        elif a > b:
            return False

def minmax(data):
    min = data[0]
    max = data[0]
    for _ in data[1:]:
        if _ > max:
            max = _
        if _ < min:
            min = _
    return min, max

def square_sum(n):
    ite = sum(i*i for i in range(n) if i % 2 == 1)
    return ite

def rand_choice(data):
    return data[randrange(0, len(data)+1, 1)], choice(data)

#C-1.13
def reverse(list1):
    return [x for x in list1[::-1]]

#C-1.15
def distinct(lst):
    if len(set(lst)) == len(lst):
        return "Distinct"
    else: return "Repeated"

#C-1.14
def odd_ele(lst):
    odd_list = []
    pair_list = []
    for _ in lst:
        if _ % 2 == 1:
            odd_list.append(_)
    odd_list = list(set(odd_list))
    for i in odd_list:
        for j in odd_list:
            if i != j and odd_list.index(j) > odd_list.index(i):
                pair_list.append((i, j))
    return pair_list

#C-1.15
def scale(data, factor):
    for j in data:
        j *= factor
    return data

#C-1.18
def second_order(n):
    if n == 0:
        return 0
    else:
        return second_order(n-1) + 2*n

def accu(n):
    return [second_order(i) for i in range(n)]

#C-1.19
def a_z():
    return [chr(_) for _ in range(97, 123)]

#C-1.20
def shuffle(data):
    list1 = []
    while len(data) > 0:
        index = randint(0, len(data)-1)
        list1.append(data[index])
        data.pop(index)
    return list1

#C-1.21
def reversal():
    s = []
    while True:
        try:
            i = input('please enter your line here: ')
            s.append(i)
        except EOFError:
            for _ in s[::-1]:
                print(_)
            exit()

#C-1.22
def dot_product(a, b):
    return list(map(lambda x, y: x*y, a, b))

#C-1.23
def index_check():
    raw = ['fuck', 'your', '%']
    try:
        raw[3] = 'shit'
    except IndexError:
        print('Don\'t try buffer overflow attacks in Python! ')

#C-1.24
def vowel_count():
    count = 0
    test_string = 'aeuio'
    s = input('Enter your string here: ')
    for _ in s:
        if _ in test_string:
            count += 1
    return count

#C-1.25
# Let's''"" try,!- Mike..?
def remove_punctuation():
    sentence = input('Please input your sentence here: ')
    pattern = re.compile(r",|'|\.|:|\?|-|\"|!|;")
    return pattern.sub("", sentence)

#C-1.26
def arithme(a, b, c):
    if a+b==c or a==b-c or a*b==c:
        return True
    else:
        return False

#C-1.27
def factors(n):
    k = 1
    while k*k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k*k == n:
        yield k

def sort_factors(n):
    return sorted(factors(n))

#C-1.28
def norm(v, p=2):
    return pow(sum(pow(x, p) for x in v), 1/p)

#P-1.29
def perm(a):
    perm = permutations(a)
    for _ in perm:
        print(''.join(_))

def perm1(a1):
    # a1 = [c, a, t]
    if len(a1) <= 1:
        yield a1
    else:
        """ permutation(n) = n*permutation(n-1), insert the nth element into position before ith (i=1,2,3,...n-1)
            element of each instance of permutation(n-1) as well as position after the (n-1)th element 
        """
        # perm ∈ [[a, t], [t, a]]
        # the order of two for loops could be altered to re-arrange the result
        for perm in perm1(a1[1:]):
            # [a , t] / [t, a]
            for i in range(len(a1)):
                """ 
                    perm = [a, t]
                    i = 0, [] + [c] + [a, t]
                    i = 1  [a] + [c] + [t]
                    i = 2 [a, t] + [c] + [] 
                """
                yield perm[:i] + a1[0:1] + perm[i:]

#P-1.30
def count2(n):
    i = 0
    if n < 2:
        print('n must greater than 2')
    while n >= 2:
        n = n/2
        i += 1
    return i

#P-1.31
def change(given, charged):
    exchange = given - charged
    mou = divmod(exchange, 100)
    half_mou = divmod(mou[-1], 50)
    twenty = divmod(half_mou[-1], 20)
    ten = divmod(twenty[-1], 10)
    yuan5 = divmod(ten[-1], 5)
    yuan = yuan5[-1]
    # lis = [mou[0], half_mou[0], twenty[0], ten[0], yuan5[0], yuan]
    return str(mou[0]) + '百' + str(half_mou[0]) + str('五十') + str(twenty[0]) + '二十' + str(ten[0]) + '十' + str(yuan5[0]) + '五' + str(yuan) +'块'

#P-1.32
def calculator():
    x1 = input(':')
    operator = input()
    x2 = input()
    switcher = {
        '+':1,
        '-':2,
        '*':3,
        '/':4
    }
    operator = switcher.get(operator)
    if operator == 1:
        return float(x1) + float(x2)
    elif operator == 2:
        return float(x1) - float(x2)
    elif operator == 3:
        return float(x1)*float(x2)
    elif operator == 4:
        return float(x1)/float(x2)
    else:
        return 'function not supported yet'

# for python 3.10 and above
# def calculatornew():
#     x1 = input(':')
#     operator = input()
#     x2 = input()
#     match operator:
#         case '+': return float(x1) + float(x2)
#         case '-': return float(x1) - float(x2)
#         case '*': return float(x1)*float(x2)
#         case '/': return float(x1)/float(x2)

#P-1.33
# def handheld():
# use ast ?

#P-1.34
def sentence():
    ra = 'I will never spam my friends again'
    randline = [randint(0, 99) for x in range(8) ]
    for i in range(100):
        if i not in randline:
            print('{}.{}'.format(i+1, ra))
        else:
            randerror = chr(randint(97, 122))
            ral = list(ra)
            randindex = randint(0, len(ra)-1)
            if ral[randindex] == ' ':
                ral[randindex+1] = randerror
            else:
                ral[randindex] = randerror
            print('{:3d}.{}'.format(i+1, ''.join(ral)))

#P-1.35
def birthday(n, sample=10000):
    conflict = 0
    for i in range(sample):
        dayrange = [randint(1, 365) for x in range(n)]
        if len(set(dayrange)) != len(dayrange):
            conflict += 1
    return 'Probability of Conflict is {}%.'.format(100*conflict/sample)

#P-1.36
def duplicate():
    origin = input('Input words list: ')
    middle = origin.split(" ")
    result = {}
    keys = set(middle)
    for key in keys:
        # count = 0
        # for _ in middle:
        #     if key == _:
        #         count += 1
        value = middle.count(key)
        # value = count
        result.update({key:value})
    return result

def duplicate_prototype():
    origin = input('Input words list: ')
    middle = origin.split(" ")
    result = {middle[0]:1}
    for _ in middle[1:]:
        if _ in result:
            result[_] += 1
        else:
            result.update({_:1})
    return result

