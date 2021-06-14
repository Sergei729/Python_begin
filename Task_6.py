# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой.


def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False


words = input('Введите строку из слов разделенных пробелами ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
