import random
import os


def extract_unique_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()

        words = text.replace('.', ' ').split()
    
        words == list(dict.fromkeys(words))

        return words
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def generate_poem(word_list, words_per_line, lines_per_strophe):
    poem = []
    for _ in range(lines_per_strophe):
        line = ' '.join(random.choices(word_list, k=words_per_line))
        poem.append(line)
    return '\n'.join(poem)


file_path = os.path.join(os.getcwd(), "text.txt")
words_per_line = 5 
lines_per_strophe = 4 

word_list = extract_unique_words(file_path)


poem = generate_poem(word_list, words_per_line, lines_per_strophe)
print(poem)

f=open("poem.txt",'w')
f.write(poem)
