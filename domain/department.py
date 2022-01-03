from domain.patient import Patient
from general.general import sort
class Department:
    def __init__(self,id,name,capacity,patients: list):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.patients = patients

    def __str__(self):
        dep_str = f"\"{self.name}\" department with ID {self.id} has {self.capacity} beds and the following patients:\n"
        for patient in self.patients:
            dep_str += f"{patient}\n"
        
        return dep_str

    def get_id(self):
        """
        Returns the department ID
        """
        return self.id
    
    def get_name(self):
        """
        Returns the department name
        """
        return self.name

    def get_capacity(self):
        """
        Returns the capacity of beds in the department
        """
        return self.capacity
    
    def get_patients(self):
        """
        Returns the list of patients in the department
        """
        return self.patients

    def set_id(self,id):
        """
        Sets the department ID
        """
        self.id = id

    def set_name(self,name):
        """
        Sets the department name
        """
        self.name = name

    def set_capacity(self,capacity):
        """
        Sets the capacity of beds in the department
        """
        self.capacity = capacity

    def set_patients(self,patients):
        """
        Sets the list of patients in the department
        """
        self.patients = patients

    def add_patient(self,patient):
        """
        Adds a patient to the department
        """
        self.patients.append(patient)

    def remove_patient(self,patient):
        """
        Removes a patient from the department
        """
        self.patients.remove(patient)

    def criteriu(self, index1, index2):
        if self.patients[index1].get_age() < self.patients[index2].get_age():
            return True
        return False

    def sort_patient_by_age(self):
        sort(self.patients, self.criteriu)