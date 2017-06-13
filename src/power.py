"This is a program
"to calculate the power of a number "
def to_the_power(x, y = 2):
#    result = x
 #   for i in range(0, y):
  #      result = result * x
    return x ** y
def square_root(x):
    return math.sqrt(x)

x = 9
y = 8 
print("{0} to the power of {1} is: {2} ", .format(x,y,to_the_power(x, y))
print("The square root of {0} is {1}".format(x, square_root(x)))
print("The end")
