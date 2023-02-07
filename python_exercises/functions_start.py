#
# Example file for working with functions
#

# define a basic function
def func1():
    print('I am a function')

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x**3

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args): #'*' allows a variable number of arguments, has to be last parameter
    result = 0
    for x in args:
        result = result + x
    return result


func1()
print (func1()) #prints 'I am a function' and 'None' b/c there is no return value
print (func1) #prints value of the function definition, which is '<function func1 at 0x10d8d5488>'
func2(10,20)
print(func2(10,20))
print(cube(3))
print(power(2))
print(power(2,3))
print (power(x = 3, num = 2)) #can assign arguments out of order only if you supply the names too
print(multi_add(10,4,5,10,4))