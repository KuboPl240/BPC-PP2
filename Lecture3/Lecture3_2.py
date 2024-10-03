S = "SometimesARandomWordJustIsn'tEnough"

L = ""
word = ""

for c in S:
    if c.isupper():
        L = L+" " +word
        word = ""
    word = word+ c.lower()
L = L+" " +word
if L[0]==" ":
    L=L[2:]

print(L)

L=L.split(" ")   
L[0],L[len(L)-1] =  L[len(L)-1],L[0]
L = ' '.join(L)
print(L)
