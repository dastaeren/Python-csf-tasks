def is_even(user_input):
    for num in user_input:
        if num % 2!= 0:
            return False
    return True
user_input = []
for i in range(3):
    user_input = int(input('Enter a number:'))

result = is_even(user_input)
print('Are all numbers even?', result)    


 