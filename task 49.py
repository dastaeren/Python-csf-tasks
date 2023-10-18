import random

secret_number = random.randint(1,100)

for i in range(100):
    user_guess = int(input('Guess the secret number betwwen 1 and 100:'))

    if user_guess < secret_number:
        print('Too low!')
    elif user_guess > secret_number:
        print('Too high!')

    else:
        print("Congratulations! You've guessed the secret number, which was", secret_number)