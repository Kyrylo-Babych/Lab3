t = str(input("Введіть слово: "))

if not t:
    print("Ви не ввели слово.")
else:
    max_count = 1
    current_count = 1

    for i in range(1, len(t)):
        if t[i] == t[i-1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 1

    
    if current_count > max_count:
        max_count = current_count
    
    print(f"Найбільша кількість однакових символів підряд: {max_count}")
