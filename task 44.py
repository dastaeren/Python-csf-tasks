user_name = input('Enter your name:')

vowels_count = 0

counter = 0 
while counter < len(user_name):
    if user_name[counter] in 'aeiou':
        vowels_count +=1
    counter += 1

    print('number of vowels:' , vowels_count)