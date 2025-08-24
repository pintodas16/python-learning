# def reverse_number(num:int)->int:
#     reverse=''
#     while num>0:
#         reminder = num % 10
#         if reminder !=0:
#             reverse += str(reminder)
#         num//=10
#     print(reverse)
#     return int(reverse)

# import math
# def reverse_number(num:int)->int:
#     res = 0
#     while num:
#         last_digit = int(math.fmod(num,10))
#         res = (res * 10) + last_digit
#         num //=10
#     print(res)
#     return res

# if __name__ == '__main__':
#     reverse_number(84387412)
#     reverse_number(43210)



# check prime number 
def check_prime_number(number:int):
    count = 0
    for i in range(1,number+1):
        # print(i)
        if number % i == 0:
            count +=1
    if count == 2:
        print(f"{number} is a prime number !")
        return False
    else:
        print(f"{number} is not a prime number !")
        return True
    
if __name__ == '__main__':
    check_prime_number(2)
    check_prime_number(1)
    check_prime_number(35)
    check_prime_number(37)
    check_prime_number(13)
    check_prime_number(17)
    check_prime_number(12)
