import math
def check_prime_number(number):
    divisor_count = 0
    square_root_number = int(math.sqrt(number))
    for i in range (1,square_root_number+1):
        # print(i,square_root_number)
        if number % i == 0 :
            divisor_count +=1
            if number // i != i :
                divisor_count +=1
    # print(divisor_count)
    if divisor_count == 2 :
        print(f'{number} is a prime number.') 
        return True
    else :
        print(f'{number} is not prime number.') 
        return False


if __name__ == '__main__':
    check_prime_number(40)
    check_prime_number(17)
    check_prime_number(4098300)
    check_prime_number(2)
    check_prime_number(1)