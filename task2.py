# Задание на закрепление знаний по модулю json. Есть файл orders в формате
# JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(),
# в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.

import json

def write_order_to_json(item, quantity, price, buyer, data):
    basket = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'data': data,
    }
    file_name = 'orders.json'
    #Read file
    json_data = json.load(open(file_name, encoding='windows-1251'))
    #Added dict
    json_data['orders'].append(basket)
    #Upload file
    json.dump(json_data,open(file_name,mode='w',encoding='windows-1251'),sort_keys=True,indent=4)


if __name__ == '__main__':
    try:
        write_order_to_json('vegetable', '16', '800', 'PetrovAV', '30.05.2021')
    except Exception as ans:
        print(ans)