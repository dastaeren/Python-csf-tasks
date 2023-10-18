temperature = int(input('What is the temperature?:'))

if temperature >= 100:
    print('Boiling')

elif temperature<=99 and temperature>=32:
    print('Liquid')

else:
    print('Freezing')
