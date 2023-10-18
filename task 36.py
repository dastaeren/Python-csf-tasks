score = int(input('Enter the score:'))
if score >= 90:
    print('A')

elif score<=79 and score>=70:
    print('B')

elif score<= 69 and score>=60:
    print('C')

elif score<60:
    print('F')

else:
    print('invalid score')