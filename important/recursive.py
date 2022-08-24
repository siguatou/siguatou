# from unittest import result

#
# def factorial(num):
#     # result = 1
#     if num > 1:
#         result = num * factorial(num-1)
#     else:
#         result = 1
#     return result
#
# print(factorial(6))
def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return x * calc_factorial(x-1)

print(calc_factorial(10))