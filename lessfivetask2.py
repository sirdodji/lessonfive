s = str(input("Введите текст: "))
l = len(s)
l2 = len(s) - s.count(" ")
words = s.count(" ") + 1
print("Количество символов: ", l)
print("Количество слов: ", l2)
