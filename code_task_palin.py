def check(word):
  reverse_word = word[::-1]

  if not word:
    return True
  elif len(word) == 1:
      return True
  elif word == reverse_word:
      return True
  return False

if '__main__' == __name__:
  word = input("Digite a palavra:  ")
  print("Palindromo: {}".format(check(word)))