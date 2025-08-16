def arm_number (num:int)-> int:
    given_number = num
    res = 0
    while num >0 :
        last_cube = int(num % 10) ** 3
        res += last_cube
        num //=10
    print(res)
    return res== given_number

if __name__=='__main__':
    arm_number(153)
    arm_number(45)
