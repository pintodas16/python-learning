# function parameter are -- 

#     Positional
#     Keyward
#     default
#     Arbitrary positional Arguments --> *args  work like tuple
#     Arbitrary keyward Arguments   ---> ** kwargs work like dictionary

def positional(name,age):
    print(f'{name} is {age} years old')

def keyward(name,age):
    print(f'{name} is {age} years old')

def arbitraryPos(*args):
    sum = 0 
    for num in args:
        sum +=num
    print(sum)

def arbitraryKeypos(**kwargs):
    sum = 0
    for key,value in kwargs.items():
        sum +=value
        print(key,value)
    print(sum)

if __name__ == "__main__":
    positional('pinto',27) # here pinto is name and 27 is age
    keyward(name="pinto",age=27)
    arbitraryPos(1,2,3,4,5)
    arbitraryKeypos(one=1,two=2)

