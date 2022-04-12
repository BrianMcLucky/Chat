# Задание 4.
#
# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).
#
# Подсказки:
# --- используйте списки и циклы, не дублируйте функции

word1 = 'разработка'
word2 = 'администрирование'
word3 = 'protocol'
word4 = 'standard'

words_list = [word1, word2, word3, word4]

words_encode = []
for i in words_list:
    i_byte = i.encode('utf-8')
    words_encode.append(i_byte)

print(words_encode, '\n')

words_decode = []

for i in words_encode:
    i_byte = i.decode('utf-8')
    words_decode.append(i_byte)

print(words_decode)
