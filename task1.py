# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных
# данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
#     Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
#     с данными, их открытие и считывание данных. В этой функции из
#     считанных данных необходимо с помощью регулярных выражений
#     извлечь значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
#     Значения каждого параметра поместить в соответствующий список.
#     Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
#     В этой же функции создать главный список для хранения данных отчета — например, main_data — и
#     поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
#     «Название ОС», «Тип системы».
#     Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
#
#     Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
#     В этой функции реализовать получение данных через вызов функции get_data(),
#     а также сохранение подготовленных данных в соответствующий CSV-файл;
#
#     Проверить работу программы через вызов функции write_to_csv().

import csv
import re


def write_to_csv():
    myData = get_data()
    with open('list_csv.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for item in myData[1:2]:
            csv_writer.writerow(myData[0])
            print(item)
            i = 0
            start = 0
            while i < len(item):
                csv_writer.writerow([myData[1][start], myData[2][start], myData[3][start], myData[4][start]])
                start += 1
                i += 1


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = [main_data_list,os_prod_list,os_name_list,os_code_list,os_type_list]

    list_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for item in list_files:
        with open(item, 'r', encoding='windows-1251') as answer:

            for i in main_data[0]:
                for it in answer:
                    a = re.split(r' + ', it.strip())
                    if a[0] == 'Изготовитель системы:':
                        os_prod_list.append(a[1])
                        continue
                    elif a[0] == 'Название ОС:':
                        os_name_list.append(a[1])
                        continue
                    elif a[0] == 'Код продукта:':
                        os_code_list.append(a[1])
                        continue
                    elif a[0] == 'Тип системы:':
                        os_type_list.append(a[1])
                        continue
    return main_data


if __name__ == '__main__':
    try:
        write_to_csv()
    except Exception as answer:
        print(answer)