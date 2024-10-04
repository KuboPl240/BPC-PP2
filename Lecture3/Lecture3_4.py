S="The car runs over the fence slowly."

word_dict = {}

for word in S.split(" "):
    if word in word_dict.keys():
        word_dict[word.lower()]+=1
    else:
        word_dict[word.lower()]=1

print(word_dict)

    
    