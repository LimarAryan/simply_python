#Takes two numbers as input and 
#takes math operation as input
#and preforms calculation

number_one = int(input("Enter your first value: "))
number_two = int(input("Enter your second value: "))

def math_operation(number_one, number_two):
    operation = input("Enter which math operation (add, sub, mult, div) you'd like: ")
    if(operation == "add"):
        return number_one + number_two
    elif(operation == "sub"):
        return number_one - number_two
    elif(operation == "mult"):
        return number_one * number_two
    elif(operation == "div"):
        return number_one / number_two

print(math_operation(number_one, number_two))