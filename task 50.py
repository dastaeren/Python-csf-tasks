num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

if num1 > num2:
    num1, num2 = num2, num1

sum_of_numbers = 0
current_number = num1

while current_number <= num2:
    sum_of_numbers += current_number
    current_number += 1

    print('The sum of all numbers between', num1 and num2 ,'is:', sum_of_numbers)