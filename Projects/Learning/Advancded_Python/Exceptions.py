try:
    print(variable)

except:
    print("Exception occurred(Name Error), because 'variable' was not defined")

attempts = 0

while True:
    
    try:
        input_var = input("Please enter a number: ")
        input_var = int(input_var)
        break
    
    except ValueError:
        attempts +=1
        
        if attempts < 3:
            print("Oops! That was not a valid number. Try again...")

        else:
            print("You really want to input a string! Fine we'll handle it")
            input_var = str(input_var)
            break
    finally:
        print("The 'try except block' ended")
        
#There are OSError,FileNotFoundError,NameError just look up all the different errors in the hieararchy 

#you can also explicitly raise an exception even if its not one
#number = int(input("Enter a number:"))

#if number > 5
#    raise Exception('The number should not exceed 5. The value of number is: {}'.format(number))
#except Exception as error:
#   print('Caught this Error: ' + repr(error))



