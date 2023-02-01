#DESCRIPTION:
#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    return "Even" if number%2==0 else "Odd"

#checking
print(even_or_odd(274))

#best practice
def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'