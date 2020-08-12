while True:
    print('''
    Welcome to the calculator program!
    Created by: Stef58
    Below is a list of the various functions available:

    -To perform an Addition, select 1;
    -To perform a Subtraction, select 2;
    -To perform a Multiplication, select 3;
    -To perform a Split, select 4;
    -To perform an Exponential Calculation, select 5;
    -To exit the program you can type ESC;
    ''')

    scelta = input('Enter the number corresponding to the selected operation --->  ')
    if scelta == "1":
        print('\nYou have chosen: Addition\n')
        a = float(input('Enter the First Number -> '))
        b = float(input('Enter the Second Number -> '))
        print('The sum result is: ' + str(a + b))
    elif scelta == "2":
        print('\nYou have chosen: Subtraction\n')
        a = float(input('Enter the First Number -> '))
        b = float(input('Enter the Second Number -> '))
        print('Il risultato della Sottrazione è: ' + str(a - b))
    elif scelta == "3":
        print('\nHai scelto: Moltiplicazione\n')
        a = float(input('Enter the First Number -> '))
        b = float(input('Enter the Second Number -> '))
        print('Il risultato della Moltiplicazione è: ' + str(a * b))
    elif scelta == "4":
        print('\nHai scelto: Divisione\n')
        a = float(input('Enter the First Number -> '))
        b = float(input('Enter the Second Number -> '))
        print('Il risultato della Divisione è: ' + str(a / b))
    elif scelta == "5":
        print('\nHai scelto: Calcolo Esponenziale\n')
        a = float(input('Insert the Base -> '))
        b = float(input('Enter the Exponent -> '))
        print('The result of the Exponential Calculation is: ' + str(a ** b))
    elif scelta == "ESC":
        print('''The application will now be closed!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break

    loop = input('\nYou want to continue using the application? Y/N ')
    if loop == "Y" or loop == "y":
        print('''I'm going back to the main menu!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        continue
    else:
        print('''Thank you and goodbye!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break