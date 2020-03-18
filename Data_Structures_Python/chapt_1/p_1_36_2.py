list_of_words = input()
list_of_words = list_of_words.split(sep=' ')
repeat = []

print(list_of_words)

for word in range(len(list_of_words)):
    rep = 0
    for repeat_word in range(word, len(list_of_words)):
        if list_of_words[word] == list_of_words[repeat_word]:
            rep += 1
    repeat.append(rep)

print(repeat, len(list_of_words), sep=' ')