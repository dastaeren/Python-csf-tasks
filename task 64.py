def find_max(numbers):
    if not numbers:
        return None
    max_value = numbers[0] 
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

numbers =[5,12,9,3]
maximum = find_max(numbers)
print("The maximum value is:", maximum)        
