def encode(text):
  text_new = ""
  for i in range(0,len(text)):
    index = ord(text[i])
    index = index + 3
    if index >= 123 and index <= 125:
      index = index - 26
    elif index >= 91 and index <= 93:
      index = index - 26
    text_new = text_new + chr(index)
  print(text_new)
  
def decode(text):
  text_new = ""
  for i in range(0,len(text)):
    index = ord(text[i])
    index = index - 3
    if index >= 94 and index <= 96:
      index = index + 26
    elif index >= 62 and index <= 64:
      index = index + 26
    text_new = text_new + chr(index)
  print(text_new)


def test_enconde(text):
  text_new = ""

  for i in range(0,len(text)):
    index = ord(text[i])
    if (index >= 65 and index <= 90):
      index = index + 3
      if index >= 91 and index <= 93:
        index = index - 26
      text_new = text_new + chr(index)
    elif (index >= 97 and index <= 122):
      index = index + 3
      if index >= 123 and index <= 125:
        index = index - 26
      text_new = text_new + chr(index)
    else:
      text_new = text_new + text[i]
  print(text_new)

def test_decode(text):
  text_new = ""

  for i in range(0,len(text)):
    index = ord(text[i])
    if (index >= 65 and index <= 90):
      index = index - 3
      if index >= 62 and index <= 64:
        index = index + 26
      text_new = text_new + chr(index)
    elif (index >= 97 and index <= 122):
      index = index - 3
      if index >= 94 and index <= 96:
        index = index + 26
      text_new = text_new + chr(index)
    else:
      text_new = text_new + text[i]
  print(text_new)

if __name__ == '__main__':
  process = input("Selecione 1 para criptografar e 2 para descriptografar: ")
  text = input("Digite a frase:  ")
  
  if process == "1":
    test_enconde(text)
  elif process =="2":
    test_decode(text)