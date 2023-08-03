
def interestCalculation(value, rate, time):
  finalValue = value

  for i in range(0, time, 1):
    finalValue += finalValue * rate / 100

  return finalValue

if __name__ == "__main__":
  try: 
    initialCapital = float(input('Enter with the initial capital: '))
    interestRate = float(input('Enter with the interest rate (%): '))
    investmentTime = int(input('Enter with the investment time (months): '))

    finalValue = interestCalculation(initialCapital, interestRate, investmentTime)

    print(f'The final value of the investmen is: ${finalValue:0.2f}')
  except ValueError: 
    print('Invalid input.')

