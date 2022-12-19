class my_class():
    # To make the Code Reuseable, Make a constructure in side the class
    def __init__(self, fname, lname, age, education):
        self.first_name = fname
        self.last_name = lname
        self.child_age = age
        self.child_education = education


Abdullah = my_class("Omer", "Ali", 20, "BSCS")
print("===========================\n\n")
print("Here is your Answer", Abdullah.first_name)
print("===========================\n\n")

# Abdullah.fname = "Abdullah-Niaz"
# Abdullah.email = "abdullahniaz423@gmail.com"
# Abdullah.education = "BSCS-1st"
# print(Abdullah.fname)

# Omer = my_class()
# Omer.fname = "Omer-Ali"
# Omer.email = "omerali423@gmail.com"
# Omer.education = "D-Form"
# print(Omer.fname)
