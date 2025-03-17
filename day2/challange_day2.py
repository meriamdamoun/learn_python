the_word = input("Enter a word: ")  
dic_words = {}
for index,word in enumerate(the_word) :
    if word in dic_words:
        dic_words[word].append(index)
    else :
        dic_words[word]=[index]
print(dic_words)