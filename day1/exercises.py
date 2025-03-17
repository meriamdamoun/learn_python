
# 🌟 Exercise 1 : Hello World

for i in range(1,5):
    print("hello word !")
    
    
    
# 🌟 Exercise 3 : What’s your name ?


name = input('give me your name :')
my_name = "meriam"
if name.lower() == my_name.lower():
    print("we have the same name :) ")
else:
    print("we don't share the same name")

# 🌟 Exercise 4 : Tall enough to ride a roller coaster

height = int(input("enter you height in cm :"))
required_heiht = int(145)
if required_heiht == height or required_heiht < height :
    print("you are tall enough to ride")
else :
    print("you need to grow some more to ride.")

# 🌟 Exercise 5 : Favorite Numbers


my_fav_numbers = {6,8,10,12,20}
my_fav_numbers.add(55)
my_fav_numbers.add(26)
print(my_fav_numbers)
my_fav_numbers.remove(26)
print(my_fav_numbers)
friend_fav_numbers={13,19,200,110,99}
our_fav_numbers = friend_fav_numbers.union(my_fav_numbers)
print(our_fav_numbers)


# 🌟 Exercise 6: Tuple

my_tuple = (1, 2, 3)
# no it's impossible to add more intgers 

# 🌟 Exercise 7: List

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("kiwi")
basket.insert(0,"Apples")
print(basket)
appel_count=basket.count("Apples")
print("there is",appel_count,"Apples")
basket.clear()
print(basket)

# 🌟 Exercise 8 : Sandwich Orders


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders :
    
    sandwich_orders.remove("Pastrami sandwich")
    
print("sandwich list :",sandwich_orders)

finished_sandwiches=[]

while sandwich_orders :
    current_sandwich=sandwich_orders.pop(0)
    print(f"we made your order:{current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print("All sandwiches made:", finished_sandwiches)




    
    








