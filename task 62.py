user_input= []
for i in range(3):
    num = float(input("Enter a number :"))
    user_input.append(num)

def is_even(user_input):
    for num in user_input:
        if num % 2 != 0:
            return False
        return True
    
result = is_even(user_input)
print("All numbers are even:",result)



 