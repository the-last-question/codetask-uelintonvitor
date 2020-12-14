def checkpassword(password):
  
  if len(password) < 8:
    return "Not a good password"

  elif (any(char.isdigit() for char in password)) == False:
    return "Not a good password"

  elif (any(char.isupper() for char in password)) == False:
    return "Not a good password"

  elif (any(char.islower() for char in password)) == False:
    return "Not a good password"
  
  return "Good password"

if __name__ == "__main__":
  password = input("digite a senha: ")
  print("\n{}".format(checkpassword(password)))