# Nested Dictionary Lookup

# Given a nested dictionary (dictionary inside dictionary), write a function to retrieve a value by keys.

# Input: data = {'a': {'b': {'c': 10}}}, keys: ['a', 'b', 'c']

# Output: 10

data = {'a': {'b': {'c': 10}}}
keys= ['a', 'b', 'c']


def get_nested_value(data,keys):
    print(data)
    for key in keys:
        data = data[key]
        print(data,"inside")
    return data

ans = get_nested_value(data,keys)
print(ans)
