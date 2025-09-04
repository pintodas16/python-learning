# lamda arguments:expression

# Using lambda with filter() to get even numbers from a list 
my_list = [1,2,3,4,5,6]
even_numbers = list(filter(lambda x: x%2==0,my_list))
print(even_numbers)

# # create all the even number 1 to n using lambda
# x = 50 
# odd_numbers = [lambda i: i in range x and i%2 !=0]

# Write a lambda function to add two numbers.
x=5
y=10
sum_func = lambda x,y:x+y

print(sum_func(x,y))

# Find all strings in a list that start with a specific letter using filter and a lambda.
strings_arr = ['Pinto','Das',"Ratul","Das"]
ch = 'd'

targeted_list = list(filter(lambda str: ch in str.lower() ,strings_arr))
print(targeted_list)


# Multiply each number in a list by 3 using map and a lambda.

number= 30
multiply_by_three = list(map(lambda num: num * 3,range(1,number+1)))
print(multiply_by_three)


# Use a lambda to check if a number is divisible by 7.
number_two = 50
is_divisible_by_seven = lambda num: num%7==0
print(is_divisible_by_seven(number_two))

# Raise each number in a list to the power of 2 using a lambda.
number_three = 10
power_of_two = list(map(lambda x: x*x, range(1,number_three + 1)))
print(power_of_two)