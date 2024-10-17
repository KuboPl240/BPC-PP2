
S="The car runs over the fence slowly."

def Bubble_sort(word_list: list):
    order = True
    if len(word_list)%2 == 0:
        order=False
    sorted = False
    while not(sorted):
        sorted=True
        for i in range(0, len(word_list)-1):
            if (order and (ord(word_list[i][0].lower()) > ord(word_list[i+1][0].lower()))) or (not(order) and (ord(word_list[i][0].lower()) < ord(word_list[i+1][0].lower()))):
                sorted=False
                word_list[i], word_list[i+1] = word_list[i+1], word_list[i]
    return word_list

word_list = S.split(" ")
print("Words count: ", len(word_list))
print("Sorted with my own bubble sort function: ",Bubble_sort(word_list))

word_list = [i.lower() for i in word_list]
if len(word_list)%2 == 0:
    word_list.sort(reverse=True)
else:
    word_list.sort()
print("Sorted with sort() function: ",word_list)

