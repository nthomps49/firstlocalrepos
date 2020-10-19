animals_list = ['Lion', 'Giraffe', 'Elephant', 'Monkey', 'Cheetah']
student_marks = [89, 99, 34, 32, 43, 25, 29, 45, 49, 37]

def print_list(student_marks):
    print(student_marks)

def bubble_sort(original_list):
    length = len(original_list)
    
    for i in range(length - 1, 0, -1): #run the itterations backwards of the list
        
        for index in range(i):
            
            if original_list[index] > original_list[index + 1]:
                
                original_list[index + 1], original_list[index] = \
                    original_list[index], original_list[index +1]
        
        print('Unsorted till index: ', i -1)
        print_list(original_list)

print(bubble_sort(student_marks))