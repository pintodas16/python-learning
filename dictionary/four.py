# Build Dictionary from Two Lists

# Given two lists, one of keys and one of values, convert them into a dictionary.

# Input: ['name', 'age'], ['Alice', 25]

# Output: {'name': 'Alice', 'age': 25}

arr_one = ['name', 'age','name']
arr_two = ['Alice', 25,'pinto']
output = {}

for index,item in enumerate(arr_one):
    if item in output:
        output[item] = arr_two[index]
    else:
        output[item] = arr_two[index]
print(output)

