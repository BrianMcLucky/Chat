# Задание 2.
#
# Каждое из слов «class», «function», «method» записать в байтовом формате
# без преобразования в последовательность кодов
# не используя!!! методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.
#
# Подсказки:
# --- b'class' - используйте маркировку b''
#

word1 = b'class'
word2 = b'function'
word3 = b'method'

words_list = (word1, word2, word3)

for i in words_list:
    print(i, type(i), len(i))
