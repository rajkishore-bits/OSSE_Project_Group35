# Function to add two numbers 
def add(num1, num2):
    return round(num1 + num2, 3)
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return round(num1 - num2, 3)
  
# Function to multiply two numbers
def multiply(num1, num2):
    return round(num1 * num2, 3)
  
# Function to divide two numbers
def divide(num1, num2):
    return round(num1 / num2, 3)

def calculator():
    print("Please select operation -\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Multiply\n" \
            "4. Divide\n")
    
    
    # Take input from the user 
    select = int(input("Select operations form 1, 2, 3, 4 :"))
    
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    
    if select == 1:
        print(number_1, "+", number_2, "=",
                        add(number_1, number_2))
    
    elif select == 2:
        print(number_1, "-", number_2, "=",
                        subtract(number_1, number_2))
    
    elif select == 3:
        print(number_1, "*", number_2, "=",
                        multiply(number_1, number_2))
    
    elif select == 4:
        if(number_2 != 0):
            print(number_1, "/", number_2, "=",
                            divide(number_1, number_2))
        else:
            print("Division by zero is not possible. Pls Retry.")
    else:
        print("Invalid input")