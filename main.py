import random
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

our_choice = int(input("What do you choose, type '0' for rock, '1' for paper, '2' for scissors: \n"))
computer = [rock, paper, scissors]
if our_choice == 0:
  print("User's Choice:")
  print(rock)
  ran = random.randint(0,2)
  print(f"Computer's Choice: {computer[ran]}")
  if computer[ran] == rock:
    print("Draw, try another time")
  elif computer[ran] == paper:
    print("Computer WON, better luck next time")
  elif computer[ran] == scissors:
    print("You WON, congrats!")
elif our_choice == 1:
  print("User's choice:")
  print(paper)
  ran = random.randint(0,2)
  print(f"Computer's Choice: {computer[ran]}")
  if computer[ran] == rock:
    print("You WON, congrats!")
  elif computer[ran] == paper:
    print("Draw, try another time")
  elif computer[ran] == scissors:
    print("Computer WON, better luck next time")
elif our_choice == 2:
  print("User's choice:")
  print(scissors)
  ran = random.randint(0,2)
  print(f"Computer's Choice: {computer[ran]}")
  if computer[ran] == rock:
    print("Computer WON, better luck next time")
  elif computer[ran] == paper:
    print("You WON, congrats")
  elif computer[ran] == scissors:
    print("Draw, try another time")
else:
  print("Please read the first statement properly and give the appropriate input idiot!")
  print("GAME OVER")
