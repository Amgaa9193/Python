# Condition 
# if 90 % 2 == 0:
#   print("this is an even number")

# BMI 2.0
# height = float(input("What is your height in m: \n"))
# weight = float(input("What is your weight in kg: \n"))

# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#   print("You are slightly unerweigth")
# elif bmi >= 18.5 and bmi <= 25:
#   print("You are ormal weight")
# elif bmi > 25 and bmi <= 30:
#   print("You are overweigth")
# else:
#   print("You are obese")


# Leap year algo
# old_year = input("Enter a year to check: \n")

# year = int(old_year)

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#         print(f"The year {year} is a leap year")
#     else:
#       print(f"The year {year} is not a leap year")
#   else: 
#     print(f"The year {year} is a Leap year")
# else:
#   print(f"The year {year} is not a Leap year")


# Pizza order
# print("Welcme to Python pizza deliveries!")
# size = input("What size pizza do you want? S = Small; M = Medium; L = Large \n")
# add_pepperoni = input("Do you want to add pepperoni? Y and N \n")
# extra_cheese = input("Do you want to add extra cheese? Y and N \n")

# bill = 0

# if size == "S":
#   bill = 15
#   if add_pepperoni == "Y":
#     bill += 2
# elif size == "M":
#   bill = 20
#   if add_pepperoni == "Y":
#     bill += 3
# else:
#   bill = 25
#   if add_pepperoni == "Y":
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your total bill is ${bill}")

# Logical operators and or not 
#  and => both has to be True
#  or => one side True will eval True, both has to be False to eval false
#  not => reverse the logic

# True Love calculator 

# print("Welcome to the love calculator!")
# name_one = input("Enter your name: \n")
# name_two = input("Enter your partners name: \n")

# count = 0

# new_one = name_one.lower()
# new_two = name_two.lower()

# combined_name = new_one + new_two
# print(combined_name)

# t = combined_name.count("t")
# r = combined_name.count("r")
# u = combined_name.count("u")
# e = combined_name.count("e")

# true = t + r + u + e

# l = combined_name.count("l")
# o = combined_name.count("o")
# v = combined_name.count("v")
# e = combined_name.count("e")

# love = l + o + v + e
# score = int(str(true) + str(love))
# # print(int(score))

# if score < 10 or score > 90: 
#   print(f"Your score is {score}, you go together like a coke and menthos")
# elif score >= 40 and score <= 50:
#   print(f"Your score is {score}, you are alright together")
# else:
#   print(f"Your score is {score}")



# Tresure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')

print("Welcome to the treasure island! Your mission is to find the treasure")
first_step = input("You\'re at the crossroad, do you want to go left or right?: \n").lower()


if first_step == "left":
  second_step = input("Good going, lets keep going. oh ohh there is a lake in front of you, do you want to 'wait' for a boat or 'swim'?: \n").lower()
  if second_step == "wait":
    third_step = input("Good choice! There are 3 doors infron of you choose wisely as only on of them has the treasure behind them! Blue, Red or Yellow?: \n").lower()
    if third_step == "yellow":
      print("You\'ve found the treasure box! You won!")
    else:
      print("You\'ve chosen wrong door! Game over")
  else: 
    print("You\'ve been eaten by a crocodile! So close...")
else:
  print("You\'ve chosen wrong road and fell into a whole!")

