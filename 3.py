sentence = input("Введіть речення: ")
word_list = sentence.split()

if len(word_list) > 1:
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    new_sentence = " ".join(word_list)
    print(new_sentence)
else:
    print(sentence)