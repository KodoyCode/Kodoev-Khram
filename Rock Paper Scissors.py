import random

def play():
    v = ['Rock', 'Scissors', 'Paper']
    m = input("\nWrite Rock, Paper, or Scissors: ").lower()
    c = random.choice(v)
    print(f'\nComputer Choiced: {c}')

    if m == c:
        print('\nDraw!')
        
    elif (m == 'rock' and c == 'scissors') or \
    (m == 'scissors' and c == 'paper') or \
    (m == 'paper' and c == 'rock'):
        print("\nYou Won!")
        
    else:
        print("\nYou Lose!")
        
play()