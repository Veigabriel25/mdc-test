

def isPrime(num):
  for x in range(2, num, 1):
    if num % x == 0:
      return False
    
  return True

def firstTenPrimes():
  count = 0
  num = 2

  while count < 10:
    if(isPrime(num)):
      print(num, end=' ')
      count += 1
    
    num += 1
    
if __name__ == "__main__":
  try: 
    print('First ten prime numbers: ', end='')
    firstTenPrimes()
  except: 
    print('Error.')

  

