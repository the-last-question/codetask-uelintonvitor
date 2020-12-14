def checkNumber(number):
  sum = 0
  number = int(number)
  for i in range(1, number):
      if(number % i == 0):
          sum = sum + i
  if (sum == number):
      return True
  else:
      return False

if '__main__' == __name__:
  number = input("Digite o numero:  ")
  print("É um numero perfeito: {}".format(checkNumber(number)))