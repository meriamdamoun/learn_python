class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def family_presentation(self):
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Power: {member['power']}, Incredible Name: {member['incredible_name']}")
    
    def born(self, member):
        self.members.append(member)

class TheIncredibles(Family):
    def __init__(self, last_name, members):
        super().__init__(last_name, members)
    
    def use_power(self, member_name):
        for member in self.members:
            if member['name'] == member_name:
                if member['age'] >= 18:
                    print(f"{member['name']} is using their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old.")
    
    def incredible_presentation(self):
        print(f"Here is our powerful family, the {self.last_name}:")
        super().family_presentation()

incredibles = TheIncredibles(
    last_name="Incredibles",
    members=[
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
    ]
)

incredibles.incredible_presentation()

incredibles.born({'name': 'Jack', 'age': 2, 'gender': 'Male', 'is_child': True, 'power': 'Unknown Power', 'incredible_name': 'BabyJack'})

incredibles.incredible_presentation()
