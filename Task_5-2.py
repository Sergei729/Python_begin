# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

line_txt = 0
word_txt = 0

f = open('text.txt')

for line in f:
    line_txt += 1
    words = line.split()
    word_txt += len(words)

f.close()

print('строк: ', line_txt)
print('слов: ', word_txt)
