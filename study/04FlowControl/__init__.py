ageInput = input('please enter you real age.\n')
print('your input age is', ageInput)
age = float(ageInput)
if age <= 0:
    print('invalid age.')
else:
    if age > 18:
        print('adult')
    elif age > 6:
        print('teenager')
    else:
        print('kind')
