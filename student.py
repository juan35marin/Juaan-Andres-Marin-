inventory_list = []

def add_product():
        student : str = str(input(f" Enter the name of the student: "))  
        average_per_student=0
        if not student:  
            print("You must enter the name of the student.")  
            return  
         
        try:
            n= int(input("enter number of grades: "))
            for i in range(n):
                grades: float = float(input("enter qualification:"))  
                if grades < 0: 
                    print("VInvalid value, grades cannot be negative.")  
                    return  

                product = {
                    'student': student,
                    'grades': grades
                }
                inventory_list.append(product) 
                print(f"'{student}' has been added to the inventory list.") 
                average_per_student += product["grades"]
                print(inventory_list)
            print(f"the average is: {average_per_student/n} ")
        except ValueError:  
                print("Invalid entry, please enter the corresponding value")  

#def Calculate_the_average_per_student():

#def suma():
 #   total_value= sum(pro['student'])/ len(product[student])


def main():
    print("System to manage a virtual library:")  
    print("1. Add books (title, author, pages)")  
    print("2. Search books by title")  

    
    while True:  
        try:
            option: int = int(input("Choose an option: ")) 
        except ValueError: 
            print("Invalid entry. Please enter a number from 1 to 6.") 
            continue 
        if option == 1:
            add_product()  
        elif option == 2:
            suma()  
        elif option == 3:
            print("Program completed.")  
            break  
        else:
            print("Invalid option. Please try again.") 


main()