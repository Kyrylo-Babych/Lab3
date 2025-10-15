t = str(input("Введіть речення: "))

t_words = t.split()

t_words[0], t_words[-1] = t_words[-1], t_words[0]

s = " "
print(s.join(t_words))

