number = '7985'

number = int(number)
res = []
while number>0:
    temp = number % 10
    res.append(temp)
    number //= 10
print(res)
res.reverse()
print(res.reverse())