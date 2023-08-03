VOWELS = ['a', 'e', 'i', 'o', 'u'] 

def countVowel(sentence): 
  vowelCount = 0
  
  for letter in sentence: 
    vowelCount += 1 if letter in VOWELS else 0

  return vowelCount

if __name__ == "__main__":
  try: 
    sentence = input('Enter with a sentence: ')
    vowelCount = countVowel(sentence.lower())

    print(f'The sentence has {vowelCount} vowels')
  except ValueError: 
    print('Invalid input.')


