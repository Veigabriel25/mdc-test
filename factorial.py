def factorial(num):
  if(num == 0): return 1

  return num * factorial(num - 1)


if __name__ == "__main__":
  try: 
    num = int(input('enter the number: '))
    print(f'The factorial of {num} is {factorial(num)}')
  except ValueError: 
    print('Invalid input.')
