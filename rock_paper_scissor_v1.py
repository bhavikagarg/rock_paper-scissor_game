# creating rock,paper,scissor game
import random
player_wins=0
computer_wins=0
winning_score=3
while player_wins<winning_score and computer_wins<winning_score:
#while True:
    print(f"Player Score={player_wins} Computer score={computer_wins}")
    choices = ["rock", "paper", "scissor"]
    comp = random.choice(choices)
    player = None
    while player not in choices:
        player = input('Rock,paper,scissors?:').lower()
# applying win condition
    if player == comp:
        print('Computer:', comp)
        print("Player:", player)
        print('Tie!')
    elif player == 'rock':
        if comp == 'scissor':
            print('Computer:', comp)
            print("Player:", player)
            print('Player Wins!')
            player_wins+=1
        if comp == 'paper':
            print('Computer:', comp)
            print("Player:", player)
            print('Computer Wins!')
            computer_wins+=1
    elif player == 'scissor':
        if comp == 'paper':
            print('Computer:', comp)
            print("Player:", player)
            print('Player Wins!')
            player_wins+=1
        if comp == 'rock':
            print('Computer:', comp)
            print("Player:", player)
            print('Computer Wins!')
            computer_wins+=1
    elif player == 'paper':
        if comp == 'rock':
            print('Computer:', comp)
            print("Player:", player)
            print('Player Wins!')
            player_wins+=1
        if comp == 'scissor':
            print('Computer:', comp)
            print("Player:", player)
            print('Computer Wins!')
            computer_wins+=1
if player_wins > computer_wins:
    print("CONGRATULATIONS!!! PLAYER WINS THE GAME...")
else:
    print("CONGRATULATIONS!!! COMPUTER WINS THE GAME...")
print("Bye Bye!!")
