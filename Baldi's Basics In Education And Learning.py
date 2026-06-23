import random
import time

score = 0
questions = 10
inventory = []

print('O, hi!')
print('My name is Baldi and Welcome to my school!')
print("Answer to my questions in 5 seconds and you'll win!")

time.sleep(2)


for i in range(1, questions + 1):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.choice(['+', '-', '*'])
    
    if z == '+':
        answer = x + y
    elif z == '-':
        answer = x - y 
    else:
        answer = x * y
        
    print(f"\nProblem №{i}: {x} {z} {y} equals?...")
    start_time = time.time()
    
    try:
        user_answer = int(input("Your quick answer: "))
        end_time = time.time()
        time_taken = end_time - start_time
        

        if time_taken > 5:
            print(f"YOU'RE TOO LATE (your wasted time: {time_taken:.2f}s)")
            print(f"The correct answer was: {answer}")
            break
            

        if user_answer == answer:
            correct_answer_print = random.choice(["Amazing! You exist!", "Great job!", "I can't believe it! you're incredible!"])
            print(correct_answer_print)
            score += 1
        else:
            not_correct_answer_print = random.choice(["I GET ANGRIER FOR EVERY PROBLEM YOU GET WRONG", "I HEAR EVERY DOOR YOU OPEN"])
            print(not_correct_answer_print)
            print(f"The correct answer was: {answer}")
            break
            
    except ValueError:
        print("WRITE A NUMBER")
        break


if score == questions:
    print("I can't believe it, you're incredible! YOU WIN THE GAME!")
    prize = random.choice(["quarter", "chocolate", "BSODA"])
    if prize == 'quarter':
        print("Here's your prize! A shining quarter!")
        inventory.append("quarter")
    elif prize == 'chocolate':
        print("Here's your prize! A sweet chocolate!")
        inventory.append("chocolate")
    else:
        print("Here's your prize! An energetic BSODA!")
        inventory.append("BSODA")
    print(f"Your inventory: {inventory}")
else:
    print("Game Over, loser! Baldi caught you.")