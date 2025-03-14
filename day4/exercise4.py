class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False  

    def family_presentation(self):
        print(f"The {self.last_name} Family:")
        for member in self.members:
            print(f"- {member['name']}, Age: {member['age']}, Gender: {member['gender']}")

smith_family = Family("Smith", [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

smith_family.family_presentation()
print(smith_family.is_18("Michael"))  
smith_family.born(name='Emma', age=0, gender='Female', is_child=True)
smith_family.family_presentation()
