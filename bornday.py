year = input("Введите год рождения А.С. Пушкина: ")

#правильный ли год
if year == "1799":
    # Если год правильный, спросить день рождения
    day = input("Введите день рождения А.С. Пушкина (число): ")

    # правильный ли день
    if day == "6":
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")