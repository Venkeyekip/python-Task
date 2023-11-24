class Organisation:
    def __init__(self, id, name):
        self.id = id
        self.name = name
organisation1 = Organisation(1, 'XYZ College')
organisation2 = Organisation(2, 'ABC University')
class Employee:
    def __init__(self, id, name, position):
        self.id = id
        self.name = name
        self.position = position
employee1 = Employee(1, 'Venky', 'java')
employee2 = Employee(2, 'Nagarjuna', 'dot_net')
employee1.organisation = organisation1
employee2.organisation = organisation2
print(employee1.name)
print(employee2.name)