#project one
import random

def roll():
  min_value = 1
  max_value = 6
  roll = random.randint(min_value,max_value)
  return roll

while True:
  players = input("Number of players (2-4): ")
  if players.isdigit():
      players = int(players)
      if 2<=players<=4:
        break
      else:
        print("Must be between 2 - 4 players")
  else:
    print("Invalid, Try Again")

max_score = 50
player_scores = [0 for I in rangfe(len(players)]
    
#calling function
value = roll()
print(value)
print(players)
print(players_scores)
