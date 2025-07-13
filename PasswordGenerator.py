import random
print("Welcome to Password Generator\n")
length=int(input("Enter the legnth of password: "))
combinations = [
  'a', 'b', 'c', 'd', 'e', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '~', '=', '+'
]

password=""
for i in range(length):
    word=random.choice(combinations)
    password+=word
    
print("The password generated is: "+password)