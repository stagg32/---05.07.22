people_dict = {"Кевин Митник": "06.08.1963", "Альберт Эйнштейн": "14.03.1879",
               "Роджер Желязны": "13.05.1937","Альберт Кинг": "25.04.1923", "Стив Джобс": "24.02.1955",
               "Гордон Фримен": "31.01.1971",
               "Александр Пушкин": "06.06.1799", "Нильс Бор": "07.10.1885", "Тур Хейердал": "06.10.1914",
               "Юрий Гагарин": "09.03.1934"}
days = {"06": "шестое", "14": "четырнадцатое", "13": "тринадцатое", "25": "двадцать пятое",
        "24": "двадцать четвертое", "31": "тридцать первое", "07": "седьмое", "09": "девятое"}
months = {"01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня",
          "07": "июля", "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декаюря"}

decision = "да"
while decision == "да":
    rightanswer = int(0)
    wronganswer = int(0)
    print("Привет! ")
    family_name = list(people_dict.keys())
    year_of_born = list(people_dict.values())

    import random
    questions = random.sample(family_name, 5)
    print("Знаешь ли ты дату рождения этого человека? (dd.mm.yyyy): ")
    for item in questions:
        print(item)
        answer = input("- ")
        dict_rightanswer = people_dict[item]
        day, month, year = dict_rightanswer.split(".")

        if answer in year_of_born:
            rightanswer += 1
        else:
            wronganswer += 1
            print("   Неверно, правильный ответ -", days[day], months[month], year, "года")

    print("Количество правильных ответов -", rightanswer)
    print("Количество неправильных ответов -", wronganswer)
    print("Процент правильных ответов -", format(float(rightanswer * 100 / 5), ".3g"))
    print("Процент неправильных ответов -", format(float(wronganswer * 100 / 5), ".3g"))

    decision = input("Сыграем еще?(да/нет): ")
print("До скорого!")
