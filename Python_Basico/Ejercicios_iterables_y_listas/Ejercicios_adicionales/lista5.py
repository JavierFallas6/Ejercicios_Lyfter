words_list = []
counter = 1

while counter <= 5:
    words = input(f"ingrese la palabras {counter}: ")
    words_list.append(words)
    counter += 1

long_words = []

for words in words_list:
    if len(words) > 4:
        long_words.append(words)

print(long_words)