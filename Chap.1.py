from random import randrange, choice, randint
import re


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



