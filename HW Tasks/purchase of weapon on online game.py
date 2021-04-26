"""ТЗ:
По данным введенным пользователем вычислить, сможет он купить выбранный им товар или нет.
Если товар в списке отсутствует - NOT OK
______
Входные данные: название товара,кол-во товара, наличные
Реализовать 2+ функциями
Выходные данные: словарь состящий из:
{названия товара как ключ:кол-во, следующий элемент - потраченная сумма - ключ, значение сумма}
"""
data = {
    'glock.20':2000,
    'usp':2500,
    'fs':3467,
    'deagle':5000,
    'p92':4000,
    'colt':90000,
    'magnum':6000,
    'p90':10000,
    'mp7':11000,
    'uzi':12000,
    'mp5':14000,
    'm16':20000,
    'ak-47':19000,
    'm416':24000,
    'famas':21000,
    'AWM':30000,
    'Dragunov':31000,
    'Barett':50000,
    'RPG':100000,
    'Topol-M':2000000
}
def count_money(price,quantity,cash):
    if cash>=price*quantity:
        return cash-price*quantity
    else:
        return 'Недостаточно средств'
def shop(weapon_name,quantity,cash):
    if weapon_name in data.keys():
        data1 = {}
        total_sum = quantity*data[weapon_name]
        data1[weapon_name] = quantity
        data1[total_sum] = count_money(data[weapon_name], quantity, cash)
        print(data1)
        return weapon_name
    else:
        print('Такого товара нет!')
# except KeyError:
shop(input('weapon name'), int(input('quantity')), int(input('Total')))