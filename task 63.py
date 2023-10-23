user_inputs =[]
for i in range(3):
    number = int(input("Enter number:"))
    user_inputs.append(number)

def is_even(user_inputs):
    for number in user_inputs:
        if number % 2 == 0:
          print(f"{number} is even")  
        
        elif number % 2 == 0:
            print(f"{number} is even")

        else:
          print(f"{number} is odd")

is_even(user_inputs)        
