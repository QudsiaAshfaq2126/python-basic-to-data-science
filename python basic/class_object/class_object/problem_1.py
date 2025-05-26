class Employee:
    def __init__(self, name, id):
        self.name = name    
        self.id = id

    def display(self):
        print("Employee name:", self.name) 
        print("Employee id:", self.id)    

emp = Employee("coder", 1)
emp.display()
del emp.id
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")
del emp
try:
    emp.display()
except NameError:
    print("emp is not defined")


