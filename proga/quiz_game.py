from colorama import init, Fore, Back, Style
init(autoreset=True)

questions = ("Кто Андрюха?",
             "Рыжый взял рыбу к себе в аквариум?",
             "Сколько людей уважает Жекича в коммунарке?",
             "Краснознаменск город чемпионов?") # картеж вариантов вопроса   

options = (("A. Красавчик","B. Лошара","C. Сосисочник"),
           ("A. Да","B. Возможно","C. Хз"),
           ("A. 10000","B. 10","C. 0"),
           ("A. Возможно","B. Нет","C. Да,тк оттуда Миша"),)

answers =("C","A","B","C")  # картеж  ответов

guesses = [] # список варианта ответов 

score = 0 
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Введи (A, B, C): ").upper()
    guesses.append(guess)
    while guess not in ("A", "B", "C"):
        guess = input(Fore.RED + "Ошибочный ввод. Пожалуйста, введите A, B или C: ").upper()
    if guess == answers[question_num]:
        print(Fore.GREEN +"Правильно,красавчик")
        score += 1
    else:
        print(Fore.RED + "Неправильно(")
        print(f"{answers[question_num]} ----> это правильный ответ")

    question_num += 1 

print("-------------------------")
print(Style.BRIGHT + "Игра окончена! Ваш результат:")
print(f"Правильных ответов: {score} из {len(questions)}")

print(Fore.GREEN + "\nПравильные ответы:")
for i in range(len(questions)):
    print(Back.WHITE + f"Вопрос {i+1}: правильный ответ - {answers[i]}, вы ответили - {guesses[i]}")   