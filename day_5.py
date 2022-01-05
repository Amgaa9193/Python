import random
# Python loops

# exc 1 
# student_heights = input("Input a list of student heights \n").split()

# print(student_heights)
# turning array of str into arr of int
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# # print(student_heights)
# count = 0
# sum = 0
# for num in student_heights:
#   sum += num
#   count += 1

# result = round(sum / count)
# print(result)


# Average score
# student_scores = input("Input a list of student scores \n").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# # print(student_scores)

# max = 0 
# for score in student_scores:
#   if max < score:
#     max = score 
  
# print(f"The highest score in the class is : {max}")

# Total of even number
# total = 0 

# for num in range(1, 101):
# # for num in range(1, 101, 2): => this will also work without the if condition
#   if num % 2 == 0:
#     total += num 

# print(f"The total number is {total}")

# FizzBUzz

# for i in range(1, 101):
#   if i % 3 == 0 and i % 5 == 0:
#     print("FizzBuzz")
#   elif i % 5 == 0:
#     print("Buzz")
#   elif i % 3 == 0:
#     print("Fizz")
#   else:
#     print(i)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for char in range(1, num_letters + 1):
#   random_char = random.choice(letters)
#   password += random_char

# for symbol in range(1, num_symbols + 1):
#   random_symbol = random.choice(symbols)
#   password += random_symbol

# for num in range(1, num_numbers + 1):
#   random_num = random.choice(numbers)
#   password += random_num

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password = []

for char in range(1, num_letters + 1):
  random_char = random.choice(letters)
  random_password += random_char

for symbol in range(1, num_symbols + 1):
  random_symbol = random.choice(symbols)
  random_password += random_symbol

for num in range(1, num_numbers + 1):
  random_num = random.choice(numbers)
  random_password += random_num

print(random_password)

random.shuffle(random_password)

hard_password = ""
for char in random_password:
  hard_password += char

print(hard_password)