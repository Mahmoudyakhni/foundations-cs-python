# FCS Assignment 1 - Solution
# Section 45 - Frederick

############
# Question 2
############

# ID

user_id = input("Enter your ID: ")
user_id = "0" + user_id
print("The ID is:", user_id)

# Name

user_name = input("Enter your name: ").upper()
print("The name is:", user_name)

# Date of Birth

user_dob = input("Enter your date of birth: ")
for x in range(len(user_dob)):
  if user_dob[x] == "-":
    user_dob = user_dob[:x] + "/" + user_dob[x+1:]
print("The date of birth is:", user_dob)

# Address

user_address = input("Enter your address: ").lower().strip()
print("The address is:", user_address)

############
# Question 3
############

number = input("Enter a number: ")
counter = 0
for x in range(len(number)):
    if number[x].isdigit():
        # We use isdigit() to check if the character is a digit, in case the user enters a letter or a symbol
        counter += 1
print("The number of digits in", number, "is:", counter) 

############
# Question 4
############

# Solution in class notes

############
# Question 5
############

number = int(input("Enter a number for pattern: "))
for x in range(1, number+1):
    # We start at 1 since multiplying by 0 will give us no stars, which is not what we want
    print("*"*x)
for x in range(number-1, 0, -1):
    print("*"*x)

############
# Question 6
############

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

while number1 > number2:
   # To ensure that the first number is smaller than the second number
   print("Invalid Input! The second number must be greater than the first number")
   number2 = int(input("Enter second number again: "))

for x in range(number1, number2+1):
   if x % 2 == 0:
       # Checks if the number is even and prints it
       print(x)