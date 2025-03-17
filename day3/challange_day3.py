class Farm:
    def __init__(self, farm_name):
        """Initialize the farm with a name and an empty animal dictionary."""
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal, count=1):
        """Add an animal to the farm. If it already exists, increase the count."""
        if animal in self.animals:
            self.animals[animal] += count
        else:
            self.animals[animal] = count

    def get_info(self):
        """Return a formatted string with all animals and their counts."""
        farm_info = f"{self.name}'s farm\n\n"
        
        for animal, count in self.animals.items():
            farm_info += f"{animal:<10} : {count}\n"

        farm_info += "\n    E-I-E-I-O!"
        return farm_info


macdonald = Farm("McDonald")

macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
