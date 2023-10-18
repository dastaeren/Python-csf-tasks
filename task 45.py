user_name = input('rnter your name:')

vowels_count = 0

for char in user_name:
    if char in 'aeiour':
        vowels_count += 1

print('number of vowels:', vowels_count)