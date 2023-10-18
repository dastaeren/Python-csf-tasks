day = input('Enter the day:')

if day == 'Monday' or'tuesday' or 'Wednesday' or 'Thursday':
    print('Weekday')

elif day == 'Friday':
    print('TGIF')

elif day == 'Saturday' or 'Sunday':
    print('Weekend')

else: 
    print('Invalid input')