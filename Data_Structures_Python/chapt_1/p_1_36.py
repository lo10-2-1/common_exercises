list_of_words = input()
list_of_words = list_of_words.split(sep=' ')
copy_of_words = list(list_of_words)
repeat = []

print(list_of_words)

for word in list_of_words:
    rep = 0
    for repeat_word in copy_of_words:
        if word == repeat_word:
            rep += 1
    repeat.append(rep)

print(repeat, len(list_of_words), sep=' ')