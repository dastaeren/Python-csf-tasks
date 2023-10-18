number = int(input('Enter a number:'))

print('Multiplication table for', number)

for counter in range(1,21):
    result = number*counter
    print(f"{number} x {counter} = {result}")