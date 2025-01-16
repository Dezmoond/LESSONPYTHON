# Список знаменитостей и их годов рождения
celebrities = [
    ["Александр Сергеевич Пушкин", 1799],  # Подсказка: 1799
    ["Лев Николаевич Толстой", 1828],      # Подсказка: 1828
    ["Исаак Ньютон", 1643],                # Подсказка: 1643
    ["Альберт Эйнштейн", 1879],            # Подсказка: 1879
    ["Михаил Ломоносов", 1711]             # Подсказка: 1711
]

# Основной цикл программы
while True:
    print("Добро пожаловать в викторину! Введите год рождения знаменитости.\n")

    correct_answers = 0  # Счётчик правильных ответов
    total_questions = len(celebrities)  # Всего вопросов

    # Перебираем список знаменитостей
    for celebrity in celebrities:
        print("В каком году родился", celebrity[0], "?")
        user_answer = input()

        # Проверяем, введено ли число и совпадает ли ответ
        if user_answer.isdigit() and int(user_answer) == celebrity[1]:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Неверно! Правильный ответ:", celebrity[1])

    # Подсчитываем результаты
    incorrect_answers = total_questions - correct_answers
    correct_percent = (correct_answers * 100) / total_questions
    incorrect_percent = 100 - correct_percent

    # Выводим результаты
    print("\nРезультаты викторины:")
    print("Количество правильных ответов:", correct_answers)
    print("Количество ошибок:", incorrect_answers)
    print("Процент правильных ответов:", round(correct_percent, 2), "%")
    print("Процент неправильных ответов:", round(incorrect_percent, 2), "%")

    # Спросить, хочет ли пользователь повторить игру
    print("\nХотите сыграть снова? (да/нет)")
    play_again = input().strip().lower()
    if play_again != "да":
        print("Спасибо за игру! До свидания.")
        break