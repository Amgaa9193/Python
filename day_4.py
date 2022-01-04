import random

# what is module?
# Modules are responsible for different functionality 

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# make the float between 0 - 5
# num = random_float * 5
# print(num)

# random_side = random.randint(1,2)

# if random_side == 1:
#   print("Head")
# else:
#   print("Tail")

# List in Python => it is a data structure, way of organizing and organizing data

# names_string = input("Give me everybody's name, seperated by a comma.\n")

# names = names_string.split(",")

# Iterate over the names arr
# depending on the index number choose random name
# and print out the output

# random_num = random.randint(0, len(names)-1)
# print(f"Today {names[random_num]}, should pay the bill!")


# Treasure map
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical -1]
# selected_row[horizontal -1] = "X"

# print(f"{row1}\n{row2}\n{row3}")


# Rock Scissors Paper

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_input = random.randint(0,2)
game_images = [rock, paper, scissors]

if int(player_input) >= 3 or int(player_input) < 0:
  print("You entered invalid number, you lose!")
else:

  print(game_images[int(player_input)])

  print(f"Computer chose: \n {game_images[int(computer_input)]}")


  # if player_input == "0":
  #   print(rock)
  # elif player_input =="1":
  #   print(paper)
  # else:
  #   print(scissors)

  # if computer_input == 0:
  #   print("Computer chose", rock)
  # elif computer_input == 1:
  #   print("Computer chose", paper)
  # else:
  #   print("Computer chose", scissors)


  if player_input == "1" and computer_input == 0:
    print("You win!")
  elif player_input == "2" and computer_input == 1:
    print("You win!")
  elif int(player_input) == computer_input:
    print("Draw! Try again")
  elif player_input == "0" and computer_input == 1:
    print("You lose!")
  elif player_input == "1" and computer_input == 2:
    print("You lose!")
  elif player_input == "2" and computer_input == 0:
    print("You lose!")
  elif player_input == "0" and computer_input == 2:
    print("You win!")



