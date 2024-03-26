# this is the base class.
class Registration:
    # A loop that creates the total number of students that have entered data.
    # data_entry= 0

    def __init__(self):
        print("Enter the students name")
        self.FirstName = input("Enter Your First Name: ").lower()
        self.LastName = input("Enter Your Last Name: ").lower()

        while True:
            self.Gender = input("Enter Male or Female: ").lower()
            if self.Gender in ["male", "female"]:
                break
            else:
                print("INVALID INPUT!,Enter the vaild answer.")

        print("Choose Month or Year for Age selection.")
        print("1.Month(s)")
        print("2. Year(s)")
        selection= input("Enter Your Choice.:")

        if selection == "1":
            while True:
                self.Age = int(input("Enter Your Age in Months: "))
                if self.Age <=12:
                    break
                else: 
                        print("Please Enter the Valid Age!!")

        elif selection == "2":
            while True:
                self.Age = int(input("Enter Your Age in Years: "))
                if self.Age <= 7:
                    break
                else: 
                    print("Please Enter the Valid Age!!")

        else:
            print("Please Enter the Valid Age!!")

       
        self.Allergies = input("Enter In Your Allergies: ").split()
        for allergy in self.Allergies:
            print(allergy)

        print ("The following displays the grade your child is in, please select.")
        while True:       
            print("1.Top class")
            print("2.Baby class")
            print("3.Middle class")
            grade_choice = input("Select one of the choices: ")

            if grade_choice == "1":
                self.Grade = "Top class"
                break
            elif grade_choice == "2":
                self.Grade = "Baby class"
                break
            elif grade_choice == "3":
                self.Grade = "Middle class"
                break
            else:
                print("ENTER A VALID INPUT")

class Phonenumber(Registration):
    pass 
class Email(Registration):
    pass
class Password(Registration):
    pass
    # Registration.data_entry += 1 
# print(f"The Total Entry of Students: {Registration.data_entry}")

reg = Registration()
print(f"First name: {reg.FirstName}")
print(f"Last name: {reg.LastName}")
print(f"Gender: {reg.Gender}")
print(f"Age: {reg.Age}")
print(f"Allergies: {reg.Allergies}")
print(f"Grade: {reg.Grade}")