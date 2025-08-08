#initiate a class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("starting executing attributes/data")
        self.id = 123
        self.salary = 60000
        self.designation ="SDE"
        print("attributes/data have been initialized")

    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination}")


#create an object/instance of the class
sam = employee()

#printing the attributes
#print(sam.salary)
#print(sam.id)

#calling a method
#sam.travel("Kolkata")

print(type(sam))