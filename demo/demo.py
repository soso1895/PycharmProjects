# print('hello,world')


# a = input('please enter an integer :')
#
# a = int(a)
#
# b = hex(a)
# # b = str(b)
#
# print('你输入的数字的十六进制的表示为：%s' % b)


# import math
#
#
# def quadratic(a, b, c):
#
#     x1 = (-b+math.sqrt(b * b - 4ac))/2a
#     x2 = (-b-math.sqrt(b * b - 4ac))/2a
#     return x1, x2
#
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
#
# L = []
# n = 1
# while n <= 99:
#     L.append(n)
#     n = n + 2
# print(L)

# a = 1
# b = 1
#
# while a <= 9:
#     while b <= a:
#         print('%s*%s=%s' % (a, b, a * b), end=' ')
#         b += 1
#     a += 1
#     b = 1
#     print('')
#
# numbers = '123456789'
# temp = numbers[-1::-2]
# print(temp)

# a = [1, 2, 3]
# b = [3, 4, 5]
# c = a + b
# print(c)
# d = a[-2:-1]
# print(d)

# a = [3, 5, 2, 9, 6, 5]
#
# b = sorted(a)
# print(b)

#
# print(list('hello world'))

# Hello World program in Python
#
# def greet(text):
#     print('='*20)
#     print(text)
#     print('='*20)
#
#
# greet(18)
# a = [1, 2, 3, 4, 5, 6, 7, 8]
#
# result = map(lambda x: x*10, a)
#
# print(result)
#
# for x in result:
#     print(x)

from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8]

result = reduce(lambda x, y: x * y, a)
print(result)




