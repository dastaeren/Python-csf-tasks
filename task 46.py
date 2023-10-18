user_number = int(input('Enter a number:'))

factorial = 1

counter = 1

while counter <= user_number:
    factorial *= counter
    counter += 1

    print('facotorial of', user_number, 'is:', factorial)
