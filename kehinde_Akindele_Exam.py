#  Question 1
num1 = float(input("Enter first number: "))
operator =  input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

def calculator(num1, num2):
    if operator == "+":
      result = num1 + num2
      return result
    elif operator == "_":
      result = num1 + num2
      return result
    elif operator == "*":
      result = num1 + num2
      return result
    elif operator == "/":
      result = num1 + num2
      return result
    if num2 != 0:
       result = num1 / num2
    else:
      print("Cannot divide by zero")
print(f"Result is: {(calculator(num1, num2))}")



#  Question 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop

    num = int(user_input)   # convert to integer

    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


# Question 3
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age.lower() == "exit":
        print("Goodbye!")
        break

    try:
        age_num = int(age)
        if age_num >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input")


