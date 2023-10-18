num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

if num1>num2:
    num1, num2 = num2,num1

sum_of_numbers = 0

for i in range(num1, num2 + 1):
    sum_of_numbers += i

print('The sum of all numbers between', num1 and num2, "is:", sum_of_numbers)
