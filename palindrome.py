

def palindrome(word, num = 0):  
  if(num > (len(word) - 1) / 2): return True

  return word[num] == word[len(word) - 1 - num] and palindrome(word, num + 1) 

if __name__ == "__main__":
  try:
    word = input('Enter with a word: ')

    isPalindrome = palindrome(word)

    # The same as if/else but with ternary expression
    print(f'The word "{word}" is {"" if isPalindrome else "not " }a palindrome')
  except ValueError: 
    print('Invalid input.')


