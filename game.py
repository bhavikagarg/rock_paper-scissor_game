# creating rock,paper,scissor game
import random
while True:
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
        if comp == 'paper':
            print('Computer:', comp)
            print("Player:", player)
            print('Computer Wins!')
    elif player == 'scissor':
        if comp == 'paper':
            print('Computer:', comp)
            print("Player:", player)
            print('Player Wins!')
        if comp == 'rock':
            print('Computer:', comp)
            print("Player:", player)
            print('Computer Wins!')
    elif player == 'paper':
        if comp == 'rock':
            print('Computer:', comp)
            print("Player:", player)
            print('Player Wins!')
        if comp == 'scissor':
            print('Computer:', comp)
            print("Player:", player)
            print('Computer Wins!')
    play_again = input("Play Again? Yes or No:").lower()
    if play_again == 'no':
        print("Thanks for playing game with me!! :) ")
        break
    else:
        print("Bring it on!!")
print("Bye Bye!!")
