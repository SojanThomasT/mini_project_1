#project one
import random

def roll():
  min_value = 1
  max_value = 6
  roll = random.randint(min_value,max_value)
  return roll

while True:
  players = input("Number of players (2-4")
  if players.isdigit("):
      players = int(players)
      if 1 <= players <= 4:
        break
      else:
        print("Must be between 2 - 4 players")
  else:
    print("Invalid, Try Again")

max_score = 50
player_scores = [0 for i in range(players)]

while max(player_scores) < max_score:
  for player_idx in range(players):
    print("Player", player_idx +1,"Turn has just started\n")
    current_score = 0
    
    #while True:
      should_roll = input("Would you like to roll (y)? ")
      if should_roll.lower() != "y":
        break
      #else:
      value=roll()
      if value == 1:
        print(" You rolled a 1! Turn Done!")
        current_score = 0
        break
      else:
        current_score += value
        print("You rolled a ", value)
    print0("Your score is: "current_score) 
    player_score[player_idx] == current_score
    print("Your total score is:",player_score[player_idx])
    
#calling function
value = roll()
print(value)
print(players)
print(players_scores)
