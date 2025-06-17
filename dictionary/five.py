
# Frequency of All Elements in List of Dictionaries

# Given a list of dictionaries, count how often each value appears.

# Input: [{ 'fruit': 'apple' }, { 'fruit': 'banana' }, { 'fruit': 'apple' }]

# Output: {'apple': 2, 'banana': 1}

arr=[{ 'fruit': 'apple' }, { 'fruits': 'banana' }, { 'fruits': 'apple' }]
output={}

kyes=[]


for index,item in enumerate(arr):
    # print(item)
    for key,value in item.items():
        kyes.append(key)
        if value in output and kyes[index]==key:
            output[value]+=1
        else:
            output[value]=1
print(output)