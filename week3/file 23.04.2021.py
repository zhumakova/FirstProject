# file1=open('text.txt','w')
# print(file1.write('\n'+'test append'))

"""
ТЗ:
По данным введенным пользователем вычислить, сможет он купить выбранный им товар или нет.
Если товар в списке отсутствует - NOT OK
__________
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

                                     # def order(name):
                                        #     if name in data.keys():
                                        #         return name
                                        #     else:
                                        #         print('Такого товара нет!')
                                        # name=order(input("название: "))
                                        # print(name,data[name])
                                        #
                                        # def order1(money):
                                        #     if money>=data[name]:
                                        #         print('success')
                                        #         return money
                                        #     else:
                                        #         print('Недостаточно средств ')
                                        # order1(int(input('money:')))"""

"""# def order(weapon_name):
#     if weapon_name in data.keys():
#         return weapon_name
#     else:
#         print('Такого товара нет!')
# weapon_name=order(input("weapon: "))
# print(weapon_name,data[weapon_name])
def count_money(price,quantity,cash):
    if cash>=data[weapon_name]*quantity:
        print('success')
        return  cash-price*quantity
    else:
        print('Недостаточно средств')
def shop(weapon_name,quantity,cash):
    if weapon_name in data.keys():
        print('success')
        return weapon_name,quantity
    else:
        print('Такого товара нет!')
    payback = count_money(data[weapon_name],1, cash)
shop(weapon_name,int(input('quantity'),int(input('Total'))))
print('ok')"""

""""# def order(weapon_name):
#      if weapon_name in data.keys():
#          return weapon_name
#      else:
#          print('Такого товара нет!')
# weapon_name=order(input("weapon: "))
# print(weapon_name,data[weapon_name])"""

def count_money(price,quantity,cash):
    if cash>=price*quantity:
        print('success')
        return  cash-price*quantity
    else:
        return 'Недостаточно средств'
def shop(weapon_name,quantity,cash):
    if weapon_name in data.keys():

        print('success')
        data1 = {}
        data1[weapon_name] = quantity
        data1[quantity*data[weapon_name]] = cash-quantity*data[weapon_name]
        print(data1)


        return weapon_name
    else:

        print('Такого товара нет!')


    payback = count_money(data[weapon_name], quantity, cash)



# except KeyError:



shop(input('weapon name'), int(input('quantity')), int(input('Total')))
