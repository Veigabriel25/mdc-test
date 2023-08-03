def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def mult(num1, num2):
  return num1 * num2

def div(num1, num2):
  return num1 / num2


if __name__ == "__main__":
  try: 
    num1 = float(input("enter the first number: "))
    op = input("enter the operation (+, -, * or /): ")
    num2 = float(input("enter the second number: "))

    print(f'\nResult of {num1} {op} {num2} = ', end='')

    if(op == '+'):
      print(add(num1, num2))
    elif(op == '-'):
      print(sub(num1, num2))
    elif(op == '*'):
      print(mult(num1, num2))
    elif(op == '/'):
      print(div(num1, num2))
    else:
        print("ERROR")
  except ValueError: 
    print('Invalid input.')

