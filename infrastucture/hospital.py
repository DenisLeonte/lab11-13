from domain.department import Department
from domain.patient import Patient

class HospitalRepo:
    def __init__(self,departments = []):
        self.departments = []
        for dep in departments:
            if type(dep[0]) == int and type(dep[1]) == str and type(dep[2]) == int and type(dep[3]) == list:
                self.departments.append(Department(dep[0],dep[1],dep[2],dep[3]))

    def __str__(self):
        i=0
        dep_str = f"Number of departments: {self.amount()}\n"
        for dep in self.departments:
            dep_str += f"{dep}\n"
        return dep_str

    def __add__(self,other):
        self.departments.append(other)
        return self

    def __iadd__(self,other):
        self.departments.append(other)
        return self

    def amount(self):
        """
        Returns the number of vectors in the list
        """
        return len(self.departments)

    def is_valid_id(self,id):
        """
        Returns true if the id is valid
        """
        for dep in self.departments:
            if dep.get_id() == id:
                return True
        return False

    def is_index_valid(self,index):
        """
        Returns true if the index is valid
        """
        if index < 0 or index >= len(self.departments):
            return False
        return True

    def add_patient(self,dep_id,patient):
        """
        Adds a patient to the department
        """
        for dep in self.departments:
            if dep.get_id() == dep_id:
                dep.add_patient(patient)

    def sort_patient_by_age(self,dep_index):
        """
        Sorts the patients in the department
        """
        self.departments[dep_index].sort_patient_by_age()