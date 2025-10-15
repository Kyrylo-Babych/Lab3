word = input("Введіть слово: ")

if not word:
    max_count = 0
    print("Ви не ввели слово.")
    quit()
else:
    max_count = 1
    current_count = 1

    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count

print(f"Найбільша кількість однакових символів підряд: {max_count}")
