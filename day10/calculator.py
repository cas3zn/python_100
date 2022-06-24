from art import logo

# adding numbers
def add(n1, n2):
  return n1 + n2

# subtracting numbers
def subtract(n1, n2):
  return n1 - n2

# multiplying numbers
def multiply(n1, n2):
  return n1 * n2

# dividing numbers
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  num1 = int(input("What's the first number? "))
  loop = True
  while loop:
    for operation in operations:
      print(operation)
    
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number? "))
    
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Would you like to continue with {answer}? y to continue or n to restart calculator: ") == "y":
      num1 = answer
    else:
      loop = False
      calculator()

calculator()