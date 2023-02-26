import random

characters = "abcdefghijklmnopqrstvxyzABCDEFGHIJKLMNOPQRSTVXZ!@#$%^&*()_+}:"
status = True
counter = 0
while status:
  password_length = int(input("What length do you want your password to be? "))
  password_count = int(input("How many password do you want? "))
  for i in range(password_count):
    password = " "
    for j in range(password_length):
      random_character = random.choice(characters)
      password += random_character

    print("Here is your password : " + password)
    counter += 1
    if counter == password_count:
      status = False