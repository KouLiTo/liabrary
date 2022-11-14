

liabrary = {}

print("""Ми створюємо бібліотеку. Заповніть її. Якщо хочете закінчити заповнення,
введіть "0" замість імені автора""")
while True:
    author = input("Введіть автора (0 завершить створення): ")
    if author == "0":
        print("Ви завершили заповнення бібліотеки")
        break
    compositions = input("Перечисліть твори автора через кому: ")
    liabrary[author] = compositions

print(liabrary.items())

print("""1 - змінити автора    2 - редагувати твори автора"
         3 - сортування за автором     4 - сортування за твором(ами)""")

def type():
    a = input("Введи бажану дію: ")
    match a:
        case "1" | "2" | "3" | "4":
            return a
        case _:
            print("Вводити можна тільки 1, 2, 3 або 4. Спробуйте ще!")
            return type()

choice = type()

match choice:
    case "1":
        author_to_change = input("Введіть автора, якого хочете змінити: ")
        if author_to_change not in liabrary.keys():
            print("Такого автора в бібліотеці не існує")
        else:
            new_author = input("Змініть чи відредагуйте автора: ")
            liabrary[new_author] = liabrary.pop(author_to_change)
            print(f"Зміна відбулася. Автор: {new_author}, твори: {liabrary[new_author]}")
    case "2":
        author_of_comps = input("Введіть автора, твори якого Ви хочете змінити: ")
        if author_of_comps not in liabrary.keys():
            print("Автора не знайдено для редагування творів")
        else:
            print("Стара версія для порівняння: ", liabrary[author_of_comps])
            liabrary[author_of_comps] = input("Введіть правильні назви творів ще раз: ")
            print(f"Актуалізовані твори автора {author_of_comps}: {liabrary[author_of_comps]}")
    case "3":
        print("Бібліотека, відсортована по авторам: ", sorted(liabrary.items()))
    case _:
        sorted_liabrary = sorted(liabrary.values())
        sorted_dict = {}
        for i in sorted_liabrary:
            for j in liabrary.keys():
                if liabrary[j] == i:
                    sorted_dict[j] = liabrary[j]
        print("Відсортована бібліотека по творам: ", sorted_dict)









