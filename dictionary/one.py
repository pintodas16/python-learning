# Group Words by Length

# Group a list of words into a dictionary based on their length.

# Input: ['apple', 'dog', 'car', 'banana']

# Output: {3: ['dog', 'car'], 5: ['apple'], 6: ['banana']}


arr = ['apple', 'dog', 'car', 'banana'];
arr = sorted(arr,key=len)
output={}

for item in arr:
    length = len(item)
    if length in output:
        output[length].append(item)
    else:
        output[length]=[item]
print(output)