# identify operator
# Two identify operator is, is not 
# If the memory address are same then it will return True, Otherwise False. 

a = [1,2,3,4]
b = a 
c = [1,2,3,4]

print (a is b) #True because a and b are sharing same memory address 
print (a is c) #False because a and c are not sharing the same memory address. However, the values are same.


# membership operator
# It is used to test for the presence of a value within a sequence (List, Tupple, string, dictionary, set). If its then return True
# otherwise False. 
# in operator 

a = [1,2,3,4]
print (4 in a) #True. 4 is present 

