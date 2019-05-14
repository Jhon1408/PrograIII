from pyDatalog import pyDatalog 

class Employee(pyDatalog.Mixin): # --> Employee inherits the pyDatalog capability
    
    def __init__(self, name, manager, salary): 
        # call the initialization method of the Mixin class
        super(Employee, self).__init__()
        self.name = name
        self.manager = manager     # direct manager of the employee, or None
        self.salary = salary       # monthly salary of the employee
    
    def __repr__(self): # specifies how to display an Employee
        return self.name

John = Employee('John', None, 6800)
Mary = Employee('Mary', John, 6300)
Sam = Employee('Sam', Mary, 5900)

pyDatalog.create_terms('has_car, X, Y, Z')
+ has_car(Mary)

#print(has_car(X)) # prints a list with one answer: the (Mary,) tuple

# which employees havea salary of 6300 ?
print
print(Employee.salary[X]==6800) # John !
print(X.v()) # 'v()' is a convenience function to get the first value of X
print

# all the indirect managers Y of X are derived from his manager, recursively
Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Y) & (Y != None)
Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Z) & Employee.indirect_manager(Z,Y) & (Y != None)

print("Indirect Manager")
print(Employee.indirect_manager(X,Y))

# the salary class N of employee X is a function of his/her salary
# this statement is a logic equality, not an assignment !
print
print("Aca muestro los valores que tiene salario")
print(Employee.salary[X] == Y)
print
print("Aca muestro la unificacion de X con los valores del diccionario")
print(X.v())
print(X.data)
Employee.salary_class[X] = Employee.salary[X]//1000

# What is the salary class of John ?
print(Sam.salary_class) # prints 6