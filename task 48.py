import random
secret_number = random.randint(1,100)
guess = None

while guess != secret_number:
    guess = int(input('Guess the secret number between 1 and 100:'))

    if guess > secret_number:
        print('Too high!')
    elif guess< secret_number:
        print('Too low!')

print("Congratulations! You've guessed the secret number correctly, which was", secret_number)