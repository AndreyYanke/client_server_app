
# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление
# в формат Unicode и также проверить тип и содержимое переменных.

word1, word2, word3 = 'разработка', 'сокет', 'декоратор'

print(type(word1), type(word2), type(word3))

word1_unicode, word2_unicode, word3_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', \
                                              '\u0441\u043e\u043a\u0435\u0442', \
                                              '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

if word1 == word1_unicode:
    print('True')
    if word2 == word2_unicode:
        print('True')
        if word3 == word3_unicode:
            print('True')
else:
    print('False')

print('#'*70, '\n')

'''2. Каждое из слов «class», «function», «method» записать в байтовом 
типе без преобразования в последовательность кодов (не используя методы encode и decode) 
и определить тип, содержимое и длину соответствующих переменных.'''

b_str1, b_str2, b_str3 = b'\xff\xfec\x00l\x00a\x00s\x00s\x00', \
                               b'\xff\xfef\x00u\x00n\x00c\x00t\x00i\x00o\x00n\x00',\
                               b'\xff\xfem\x00e\x00t\x00h\x00o\x00d\x00'


print(type(b_str1), type(b_str2), type(b_str3))
print(len(b_str1), len(b_str2), len(b_str3))

print('#'*70, '\n')

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.


word_b1 = b'attribute'
# word_b2 = b'класс' строки записанные на кириллице вылетает исключение
# word_b3 = b'функция' строки записанные на кириллице вылетает исключение
word_b4 = b'type'

print('line 45 \n'
      'word_b2 = b"класс" и word_b3 = b "функция" строки записанные на кириллице вылетает исключение \n'
      'SyntaxError: bytes can only contain ASCII literal characters.', '\n',
      '#'*70, '\n')


#  4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

enc_srt = ['разработка', 'администрирование', 'protocol', 'standard']

for word in enc_srt:
    word1_enc = word.encode('utf-16')
    print(word1_enc)
    word1_dec = bytes.decode(word1_enc, 'utf-16')
    print(word1_dec)

print('#'*70, '\n')


# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess

ping_resurs = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]

for ping in ping_resurs:
    ping_process = subprocess.Popen(ping, stdout=subprocess.PIPE)
    print(ping_process)

    i = 0

    for line in ping_process.stdout:

        if i < 3:
            print(line)
            line = line.decode('cp866').encode('utf-16')
            print(line.decode('utf-16'))
            i += 1
        else:
            print('#' * 70)
            break

# Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл
# в формате Unicode и вывести его содержимое

import locale

resurs_string = ['сетевое программирование', 'сокет', 'декоратор']

# Создаем файл
with open('file.txt', 'w+') as f_n:
    for i in resurs_string:
        f_n.write(i + '\n')
    f_n.seek(0)

print(f_n)  # печатаем объект файла, что бы узнать его кодировку

file_coding = locale.getpreferredencoding()

# Читаем из файла
with open('file.txt', 'r', encoding=file_coding) as f_n:
    for i in f_n:
        print(i)

    f_n.seek(0)

