

if __name__ == "__main__":
  try: 
    grade1 = float(input('Enter with the first grade: ')) 
    grade2 = float(input('Enter with the second grade: ')) 
    grade3 = float(input('Enter with the third grade: '))

    average = (grade1 + grade2 + grade3) / 3

    print(f'The average of the student is = {average:0.2f}')
  except ValueError: 
    print('Invalid input.')


