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


# Sort a list of tuples based on the second element using sorted and a lambda.

li = [(1,3,5),(3,4,2),(2,1),(3,5),(1,2)]
sorted_list = sorted(li,key=lambda num: num[1])
print(sorted_list)


# Sort a list of words by their length using sorted and a lambda.
words = ["Bangladesh","Germany","UK","The Great Bratian","Dutchland"]
sorted_words = sorted(words, key = len,reverse=True)
print(sorted_words)

# Remove all elements from a list that are not integers using filter and a lambda.
li_elements = [1,2,"Apple","Orange","Banana",True,False]
sorted_li_elements = list(filter(lambda el:isinstance(el,int) and not isinstance(el,bool) ,li_elements))
print(sorted_li_elements)

# Extract the domain name from a list of email addresses using map and a lambda.
emails = ["alice@gmail.com", "bob@yahoo.com", "charlie@outlook.com"]
extracted_emails = list(map(lambda email:email.split("@")[1],emails))
print(extracted_emails)


# Combine first and last names from two lists into full names using map and a lambda.

first_names = ["Alice", "Bob", "Charlie"]
last_names = ["Smith", "Johnson", "Brown"]

full_names = list(map(lambda first_name,last_name:f'{first_name} {last_name}',first_names,last_names))
print(full_names)