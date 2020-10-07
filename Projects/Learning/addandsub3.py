output_text = 'Hello, welcome to my math program\n'
print(output_text)

choice = input("Do you want to do add or subtract? ")
if choice != 'add' or 'sub' or 'subtract':
    print('You must make a choice')
    exit()
if choice == 'add':
    quantity = input('How many numbers do you want to add? ')
    x = 0
    s = 0
    while x < int(quantity):
        x += 1
        s += (int(input('Enter a number: ')))
    print('The sum of the numbers is ' + str(s))
elif choice == 'subtract' or 'sub':
    quantity = input('How many numbers do you want to subtract? ')
    first_element = int(input('What is the number to start subtracting from? '))
    x = 1
    s = 0
    while x < int(quantity):
        x += 1
        s += (int(input('Enter a number: ')))
        s1 = int(first_element) - int(s)
    print('The subtraction equates to ' + str(s1))
else:
    choice != 'add' or 'subtract' or 'sub'
    print('You must make a choice')













