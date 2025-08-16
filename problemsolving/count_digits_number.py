# number = '7985'

# number = int(number)
# count = 0 
# while number>0 : 
#     number //=10
#     count +=1
# print(count ) #time complexity O(log(n))

# now reduce the time complexity 
import math


def count_number(n:int)->int:
    power = int(math.log10(n))
    return power + 1

if __name__ == '__main__':
    print(count_number(7980))
    print(count_number(79855))






