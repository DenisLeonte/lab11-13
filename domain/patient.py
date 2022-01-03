class Patient:

    def __init__(self, first_name, last_name, age, cnp, disease):
        """
        Initialises the pacient class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cnp = cnp
        self.disease = disease

    def __str__(self):
        """
        Returns a string representation of the vector.
        """
        return f"Pacient {self.first_name} {self.last_name} (age {self.age}) with CNP {self.cnp} and disease {self.disease}."
   
    def get_first_name(self):
        """
        Returns the first name of the pacient.
        """
        return self.first_name

    def get_last_name(self):
        """
        Returns the last name of the pacient.
        """
        return self.last_name

    def get_age(self):
        """
        Returns the age of the pacient.
        """
        return self.age

    def get_cnp(self):
        """
        Returns the CNP of the pacient.
        """
        return self.cnp

    def get_disease(self):
        """
        Returns the disease of the pacient.
        """
        return self.disease

    def set_first_name(self, first_name):
        """
        Sets the first name of the pacient.
        """
        self.first_name = first_name

    def set_last_name(self, last_name):
        """
        Sets the last name of the pacient.
        """
        self.last_name = last_name

    def set_age(self, age):
        """
        Sets the age of the pacient.
        """
        self.age = age

    def set_cnp(self, cnp):
        """
        Sets the CNP of the pacient.
        """
        self.cnp = cnp

    def set_disease(self, disease):
        """
        Sets the disease of the pacient.
        """
        self.disease = disease

    
    