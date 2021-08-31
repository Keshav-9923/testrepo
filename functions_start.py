#
# Example file for working with functions
#
def power(num,x):
    result = 1
    for i in range(x):
        result=result*num
    return result
# define a basic function
print(power(2,3))


# function that takes arguments
def multi_add(*args):
    result=0
    for x in args:
        result = result + x
    return result

print(multi_add(1,2,5,7))

# function that returns a value


# function with default value for an argument


#function with variable number of arguments


