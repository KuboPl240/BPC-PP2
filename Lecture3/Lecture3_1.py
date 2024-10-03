S="The car runs over the fence slowly."

def Bubble_sort(String_to_sort: str):
    word_list = String_to_sort.split(" ")
    order = False
    if len(word_list)%2 == 0:
        order=True
    sorted = False
    while not(sorted):
        sorted=True
        for i in range(0, len(word_list)-1):
            if (order and (ord(word_list[i][0].lower()) > ord(word_list[i+1][0].lower()))) or (not(order) and (ord(word_list[i][0].lower()) < ord(word_list[i+1][0].lower()))):
                sorted=False
                word_list[i], word_list[i+1] = word_list[i+1], word_list[i]
                print(word_list)
    return word_list

print(Bubble_sort(S))
