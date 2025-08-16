# def reverse_number(num:int)->int:
#     reverse=''
#     while num>0:
#         reminder = num % 10
#         if reminder !=0:
#             reverse += str(reminder)
#         num//=10
#     print(reverse)
#     return int(reverse)

import math
def reverse_number(num:int)->int:
    res = 0
    while num:
        last_digit = int(math.fmod(num,10))
        res = (res * 10) + last_digit
        num //=10
    print(res)
    return res

if __name__ == '__main__':
    reverse_number(84387412)
    reverse_number(43210)