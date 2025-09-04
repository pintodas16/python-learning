# eval(expression, globals, locals)

# expression should be string and valid python expression 
# globals and locals are dictionary. These are optionals if not provided then the global namespace works and local namespace repectively 


number = int(input("Please enter a number: "))
square_number = eval("number * number * two",{"two":2},locals())
print(square_number)