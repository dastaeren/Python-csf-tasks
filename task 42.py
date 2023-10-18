user_name = input('Enter your name:')
vowel_present = False # is a boolen variable, initialized to false which will be set to True if a vowel is found

vowels = ['a','e','i','o','u']

counter = 0
found_vowel = False

while not vowel_present and counter < len(user_name):
    if user_name[counter] in vowels:
        vowel_present = True 

    counter += 1
print(vowel_present)