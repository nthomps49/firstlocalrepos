output_text = 'Hello, welcome to my math program\n'
print(output_text)

def add():
    sum = float(var1) + float(var2)
    print("That equals:"); print(sum);

def sub():
    sub = float(var1) - float(var2)
    print("That equals:"); print(sub)

choice = input("Do you want to do add or subtract?")
if choice == 'add':
    var1 = input("What is the first number you want to add?")
    var2 = input("What is the second number you want to add?")
    add()  
elif choice == 'subtract':
   var1 = input("What is the first number you want to subtract?")
   var2 = input("What is the second number you want to subtract?")
   sub()












