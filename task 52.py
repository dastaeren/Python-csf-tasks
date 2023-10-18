number = int(input('Enter a number:'))
counter = 1
print('Multiplication table for',number)

while counter <= 20:
    result = number*counter
    print (f"{number} x {counter} = {result}")
    counter += 1