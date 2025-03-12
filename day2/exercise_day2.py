# 🌟 Exercise 1 : Convert lists into dictionaries


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for i in zip(keys,values):
    print(i)
    
# 🌟 Exercise 2 : Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

cost = 0

for name, age in family.items():
    if age < 3 :
        print(f"{name} is for  free")
    elif age > 15: 
        print(f"{name} gonna pay 15")
        cost +=15
    else :
        print(f" {name} gonna pay 10")
        cost+=10
    
print(cost)

# 🌟 Exercise 3: Zara

brand = {"name":"zara","creation":  1975,"creator_name":"Amancio Ortega Gaona ","type_of_clothes":["men", "women", "children", "home"],"international_competitors":["Gap", "H&M", "Benetton"],"number_stores": 7000,
"major_color": {
    "France": "blue", 
    "Spain": "red", 
    "US": "pink, green"
    }
}

# 🌟 Exercise 3: Zara

brand["number_stores"]=2 
print(brand)

for i in brand["type_of_clothes"]:
  print(f"Zara provides clothing for {', '.join(brand['type_of_clothes'])}.") 
  
  
brand["country_creation"] = "spain"
print(brand)
    
    
if "international_competitors" in brand :
    brand["international_competitors"].append("Desigual")
print(brand)
    
del brand["creation"]
print(brand)

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])


print(len(brand))

print(brand.keys())

more_on_zara ={ "creation": 1975, "number_stores": 10000 }

brand.update(more_on_zara)
print(brand)


# 🌟 Exercise 4 : Some Geography
def describe_city(city,country="Morocco"):
     print(city +" " +"is in "+ country)
 
describe_city("Casa")

# 🌟 Exercise 5 : Random
# import random

# def compare_numbers(user_number):
#     random_number = random.randint(1, 100)
    
#     if user_number == random_number:
#         print("Success! The numbers match.")
#     else:
#         print(f"Fail! The numbers do not match. Your number: {user_number}, Random number: {random_number}")

# user_input = int(input("Enter a number between 1 and 100: "))
# compare_numbers(user_input)

# 🌟 Exercise 6 : Let’s create some personalized shirts !

def make_shirt():
    size = input("What's your size ? ")
    text = input("What's the text you want ?")
    print (f" The size of the shirt {size} is and the text is {text} " )
make_shirt()

def make_shirt1(size="L",text="I LOVE PYTHON"):
    print (f" The size of the shirt {size} is and the text is {text} " )
make_shirt1()

def make_shirt2(size,text):
    print (f" The size of the shirt {size} is and the text is {text} " )
make_shirt2("xl","NICE DAY")
    
# 🌟 Exercise 7 : Temperature Advice
import random

def get_random_temp(season):
    if season == 'winter':
        temp = random.uniform(-10, 16)
    elif season == 'spring':
        temp = random.uniform(0, 20)
    elif season == 'summer':
        temp = random.uniform(20, 40)
    elif season == 'autumn' or season == 'fall':
        temp = random.uniform(5, 18)
    else:
        temp = random.uniform(-10, 40)

    return temp

def give_advice(temp):
    if temp < 0:
        return "Brrr, that’s freezing! Wear some extra layers today."
    elif 0 <= temp <= 16:
        return "Quite chilly! Don’t forget your coat."
    elif 16 < temp <= 23:
        return "It’s a bit cool, but comfortable! A jacket should be enough."
    elif 24 <= temp <= 32:
        return "Warm weather! A T-shirt will do."
    elif 32 < temp <= 40:
        return "It’s hot out! Stay hydrated and wear light clothes."

def main():
    user_input = input("Enter a season (winter, spring, summer, autumn) or a month number (1-12): ").lower()

    if user_input.isdigit():
        month = int(user_input)
        if 12 >= month >= 3:
            season = "spring" if month in [3, 4, 5] else ("summer" if month in [6, 7, 8] else ("autumn" if month in [9, 10, 11] else "winter"))
        else:
            season = "winter"
    else:
        season = user_input

    temp = get_random_temp(season)
    
    advice = give_advice(temp)

    print(f"The temperature right now is {temp:.2f} degrees Celsius.")
    print(advice)

main()
# 🌟 Exercise 8 : Star Wars Quiz

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz():
    correct = 0
    incorrect = 0
    wrong_answers = []  

    for question in data:
        user_answer = input(question["question"] + " ")

        if user_answer.strip().lower() == question["answer"].lower():
            correct += 1
        else:
            incorrect += 1
            wrong_answers.append({
                "question": question["question"],
                "your_answer": user_answer,
                "correct_answer": question["answer"]
            })
    
    print(f"\nYou got {correct} correct answers and {incorrect} incorrect answers.")
    
    if incorrect > 0:
        print("\nYou got the following questions wrong:")
        for item in wrong_answers:
            print(f"Question: {item['question']}")
            print(f"Your answer: {item['your_answer']}")
            print(f"Correct answer: {item['correct_answer']}\n")
    
    if incorrect > 3:
        print("\nYou had more than 3 incorrect answers. Would you like to play again?")
        play_again = input("Type 'yes' to play again or 'no' to quit: ").lower()
        if play_again == 'yes':
            quiz()  
        else:
            print("Thanks for playing!")
    else:
        print("Thank you for playing!")

quiz()
