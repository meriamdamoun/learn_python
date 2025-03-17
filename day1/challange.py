
########CHALLANGE 1 

number = int(input("give a number : "))
lenght = int(input("give a lenght : "))

my_list = []

for i in range(lenght) :
    my_list.append( number *(i+1))

print(my_list)


########CHALLANGE 2


word = input("Your word :")
result=""

for i in range(len(word)):
    if i==0 or word[i]!= word[i-1] or word[i] !="passing""lottery":
        result += word[i]
print(result)
    

    