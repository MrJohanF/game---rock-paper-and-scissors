import random
import ascii_resources

rock = ascii_resources.rock
paper = ascii_resources.paper
scissors = ascii_resources.scissors


option = int(input("Choose a number: 0 = paper, 1 = rock, 2 = scissors: "))


result = [paper, rock, scissors]

print("You have choosen: ", result[option])

resultlenght = len(result)

machine = random.randint(0, resultlenght - 1)

print("Computer has choosen: ", result[machine])

if option == machine:
  print("Draw!")
  
if option == 0 and machine == 1:
  print("You have won!")
  
if option == 1 and machine == 2:
  print("You have won!")

if option == 2 and machine == 0:
  print("You have won!")

if machine == 0 and option == 1:
  print("You have lost!")
  
if machine == 1 and option == 2:
  print("You have lost!")

if machine == 2 and option == 0:
  print("You have lost!")
