

def table(num):
  print(f'Table of {num}: \n')

  for i in range(1, 11):
    print(f'{i} * {num} = {num * i}')
    


if __name__ == "__main__":
  try: 
    num = int(input('Enter a number: '))
    table(num)
  except ValueError: 
    print('Invalid input.')

