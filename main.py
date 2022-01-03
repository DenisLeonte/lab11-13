import os
from domain.department import Department
from domain.patient import Patient
from infrastucture.hospital import HospitalRepo
import frontend.ui as UI

dep_repo = HospitalRepo([
    [1,'Dep a',5,[Patient('John','Doe',20,'891273891','cancer'),Patient('Bob','Dough',18,'12890831','covid-19')]],
    [2,'Dep b',5,[]],
    [3,'Dep c',5,[]],
    [4,'Dep d',6,[]],
    [5,'Dep e',6,[]],
    ])

def read_department():
    """
    Reads the values of a department from the console.
    """
    name_valid = False
    capacity_valid = False

    depid = int(input('Enter the department id: '))
    while dep_repo.is_valid_id(depid):
        print('Department id already exists.')
        depid = int(input('Enter the department id: '))

    while not name_valid:
        name = input("Enter the name: ")
        if name == "":
            print("The name id cannot be empty.")
        else:
            name_valid = True
            dep_name = name
    
    while not capacity_valid:
        cap = int(input("Enter the capacity: "))
        if cap == "" or type(cap) != int:
            print("The name id cannot be empty.")
        else:
            capacity_valid = True
            dep_cap = cap

    vec = Department(depid, dep_name, dep_cap, [])
    return vec

def read_patient():
    """
    Reads the values of a patient from the console.
    """
    first_valid = False
    last_valid = False
    age_valid = False
    cnp_valid = False
    disease_valid = False

    while not first_valid:
        name = input("Enter the first name: ")
        if name == "":
            print("The name id cannot be empty.")
        else:
            first_valid = True
            first_name = name

    while not last_valid:
        name = input("Enter the last name: ")
        if name == "":
            print("The name id cannot be empty.")
        else:
            last_valid = True
            last_name = name
    
    while not age_valid:
        name = int(input("Enter the age: "))
        if name == "":
            print("The age id cannot be empty.")
        else:
            age_valid = True
            age = name

    while not cnp_valid:
        name = input("Enter the CNP: ")
        if name == "":
            print("The name id cannot be empty.")
        else:
            cnp_valid = True
            cnp = name

    while not disease_valid:
        name = input("Enter the disease: ")
        if name == "":
            print("The name id cannot be empty.")
        else:
            disease_valid = True
            disease = name

    vec = Patient(first_name,last_name,age,cnp,disease)
    return vec

def input_valid_index():
    """
    Checks if the index is valid.
    """
    index_valid = False
    while not index_valid:
        index = int(input("Enter the index: "))
        if index < 0 or index >= len(dep_repo):
            print("Invalid index")
        else:
            index_valid = True
            return index
    return

while(True):
    """
    Loop the menu and wait for an input
    """
    UI.print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    #Check what choice was entered and act accordin gly
    os.system('cls||clear')

    if option == 0:
        print('Exiting.')
        exit()
    elif option == 1:
        aux = read_department()
        dep_repo += aux
    elif option == 2:
        print(dep_repo)
    elif option == 3:
        if dep_repo.amount != 0:
            
                depid = int(input('Enter the department id: '))
                while not dep_repo.is_valid_id(depid):
                    print('Invalid department id')
                    depid = int(input('Enter the department id: '))
                aux = read_patient()
                dep_repo.add_patient(depid,aux)

        else:
            print('The list is empty')
        
    elif option == 4:
        if dep_repo.amount != 0:
            index = int(input('Enter the index: '))
            while not dep_repo.is_index_valid(index):
                print('Invalid index')
                index = int(input('Enter the index: '))
            dep_repo.sort_patient_by_age(index)
        else:
            print('The list is empty')
    else:
        print('Invalid option. Please enter a valid option.')