
# 🌟 Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        print(f"the cat  {cat_name} and her age is {cat_age}")
cat1=Cat("mimi",2)
cat2=Cat("lolo",1.5)
cat3=Cat("soso",2.5)

def oldest_cat(cat1,cat2,cat3):
    if cat1.age>cat2.age and cat1.age>cat3.age :
        return cat1
    elif cat2.age>cat1.age and cat2.age>cat3 :
        return cat2
    else:
        return cat3
the_older = oldest_cat(cat1,cat2,cat3)
print(f"The oldest cat is {the_older.name}, and she is {the_older.age} years old.")

# 🌟 Exercise 2 : Dogs

class Dog() :
     def __init__(self , name ,height):
         self.name = name
         self.height = height 
         print(f"the dog is {name} height : {height}")
     def bark (self):
         print(f"{self.name} goes woof!." )
     def jump (self):
         x = self.height *2
         print(f"{self.name} jumps {x} cm high")

         
dog1=Dog("bob",80)
dog1.bark()
dog1.jump()

davids_dog=Dog("rex",50)
davids_dog.bark()
davids_dog.jump()

sarahs_dog=Dog("Teacup",20)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same size!")

# 🌟 Exercise 3 : Who’s the song producer?


class Song ():
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(f"{line}  ")
            
stairway=Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# 🌟Exercise 4 : Afternoon at the Zoo

class Zoo():
    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []
        print(f"welcome to {self.name} ")
        
    def add_animal(self ,new_animal):
        
            if new_animal in self.animals:
                
                print("the animal is already in the list")

            else :
                self.animals.append(new_animal)
                print(f"{new_animal} has been added to the zoo.")
                
                
                
    def get_animals (self):
        if not self.animals:
            print("no animals in the zoo yet !")
        else:
            print("the animals in zoo are :")
            for animal in self.animals:
                print(f"{animal}")
                
                
                
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo!")
            
            
    def sort_animals(self):
       
        self.animals.sort()  
        self.animal_groups = {}  
        

        for animal in self.animals:
            first_letter = animal[0]  
            if first_letter not in self.animal_groups:
                self.animal_groups[first_letter] = []  
                
            self.animal_groups[first_letter].append(animal)
            
            
            
    def get_groups(self):
        if not self.animal_groups:
            print("No animal groups available. Please sort animals first!")
            return
        
        print("Animal Groups:")
        for letter, animals in self.animal_groups.items():
            print(f"{letter}: {animals}")
                
        
        
animal = Zoo("My ZOO")
animal.add_animal("Tiger")
animal.add_animal("Giraffe")

animal.get_animals()
animal.sell_animal("Giraffe")
animal.sort_animals()
animal.get_groups()


