# DESCRIPTION:
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    return number*9 if number%2 else number*8


#checking
print(simple_multiplication(8))

#best practice
def simple_multiplication(n) :
    return n * (8 + n%2)