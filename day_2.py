# Primitive datatypes in Python

# String subscripting 
# print("Hello"[2])


# Integer

# computer will ignore underscore, _ is for human eyes
# print(123_456_789)

# Float
# print(3141.9)

# Boolean

# True 
# False

# you cant concatenate str with integer
# num_char = 5
# print(type(num_char))

# new_num = str(num_char)
# print(type(new_num))
# new_num = float(num_char)
# print(type(new_num))
# new_num = int(num_char)
# print(type(new_num))


# Number operations 
# print(1 + 1)
# print(1 - 1)
# print(1 * 2)
# # pythn gives float if you use the divide
# print(1 / 1)
# print(2 ** 2)

# PEMDASLR => () ** */ +-



#  BMI = weight/height
# height = input("enter you height in m: \n")
# weight = input("enter you weight in kg: \n")

# bmi = int(weight) / float(height) ** 2
# new_bmi = str(int(bmi))
# print("Your BMI is: " + new_bmi)


# rounding up float num
# print(round(8/3, 2))
# print(8//3) => will give Integer result

# result = 4 / 2
# result /= 1
# print(result)

# F string*** f"always put the f in front of the {string}"
# score = 0
# height = 1.7
# weight = 80 
# isWinning = True 

# print(f"your score is {score}, your height is {height}, your weight is {weight}, you are winning {isWinning}")



# Life in Weeks 
# age = input("What is your age: \n")

# year_left = 90 - int(age)
# days = year_left * 365
# weeks =  year_left * 52
# months =  year_left * 12


# print(f"You have {days} days, {weeks} weeks, and {months} left.")


# Tip calculator 
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? \n$")
tip = input("What percentage tip would you like to give? 10, 12, or 15? \n")
ppl = input("How many people to split the bill? \n")

tip_total = float(total_bill) * (int(tip) / 100)
new_ttl = float(total_bill) + tip_total
each_person_bill = "{:.2f}".format(new_ttl / int(ppl))

print(f"Each person should pay: ${each_person_bill}")
