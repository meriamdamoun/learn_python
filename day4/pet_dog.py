
# 🌟 Exercise 3 : Dogs Domesticated

import random
from dog import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *dog_names):
        all_dogs = ", ".join(dog_names)
        print(f"{all_dogs} all play together.")
    
    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll.",
                f"{self.name} stands on his back legs.",
                f"{self.name} shakes your hand.",
                f"{self.name} plays dead."
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet!")

if __name__ == "__main__":
    pet_dog = PetDog("Buddy", 4, 22)
    pet_dog.train()
    pet_dog.play("Max", "Rex", "Bolt")
    pet_dog.do_a_trick()
