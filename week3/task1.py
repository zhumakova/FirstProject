"""
users:
    sale - скидка на любую покупку в %
    status - юридическое или частное лицо
purchases:
    taxes - процентная ставка налога на всю покупку,

Описание проблемы:
Большая часть базы данных удалилась, по имеющейся информации вычислить сколько люди потратили на уцелевшие покупки
Задание:
1. Вычислить сколько потратил каждый покупатель с оплатой налогов
2. Для пользователей у кого незаполнено поле total_amount - вычислить по имеющимся покупкам
3. Текущую общую стоимость записать в файл (Имя + потраченные деньги)
"""


users = [
    {'id':1,'username':'superman','country':'Crypton','total_amount':57890,'sale':10,'status':'gov'},
    {'id':2,'username':'Bruce Wayne','country':'USA','total_amount':1000000000,'sale':67,'status':'private'},
    {'id':3,'username':'joker','country':None,'total_amount':None,'sale':None,'status':'private'},
    {'id':4,'username':'jamilya','country':'Kyrgyzstan','total_amount':777000,'sale':30,'status':'gov'},
    {'id':5,'username':'aliya','country':'Kyrgyzstan','total_amount':777000,'sale':31,'status':'gov'},
    {'id':6,'username':'cr7','country':'Portugal','total_amount':None,'sale':50,'status':'private'},
    {'id':7,'username':'trump','country':'USA','total_amount':1000000000,'sale':0,'status':'gov'},
    {'id':8,'username':'cholpon','country':'Kyrgyzstan','total_amount':200000,'sale':10,'status':'private'},
]

purchases = [
    {'id':1,'user_id':1,'products':['glasses','cloak','coat'],'taxes':21},
    {'id':2,'user_id':2,'products':['washington_post','spaceX','gotham'],'taxes':56},
    {'id':3,'user_id':2,'products':['daily planet','bicycle'],'taxes':18},
    {'id':4,'user_id':2,'products':['factory','amazon','coat'],'taxes':70},
    {'id':5,'user_id':3,'products':['grenade','machine gun'],'taxes':1},
    {'id':6,'user_id':4,'products':['glasses','cloak','coat'],'taxes':23},
    {'id':7,'user_id':4,'products':['glasses','cloak','coat'],'taxes':29},
    {'id':8,'user_id':5,'products':['glasses','cloak','coat'],'taxes':41},
    {'id':9,'user_id':5,'products':['glasses','cloak','coat'],'taxes':23},
    {'id':10,'user_id':6,'products':['glasses','cloak','coat'],'taxes':24},
    {'id':11,'user_id':6,'products':['glasses','cloak','coat'],'taxes':11},
    {'id':12,'user_id':7,'products':['glasses','cloak','coat'],'taxes':0},
    {'id':13,'user_id':8,'products':['glasses','cloak','coat'],'taxes':7},
    {'id':14,'user_id':8,'products':['glasses','cloak','coat'],'taxes':7},
    {'id':15,'user_id':7,'products':['glasses','cloak','coat'],'taxes':1},
]
products = {'glasses':23000,'cloak':17000,'coat':16000,
            'washington_post':1000000,'spaceX':9999999,'gotham':None,
            'daily planet':1800000,'bicycle':1000,'factory':780000,'amazon':None,
            'grenade':8000,'machine gun':71000}

def customer_total_cost(users,purchases,products):
    for user in users:
        summ=0
        for purchase in purchases:
            if user['id']==purchase['user_id']:
                p_purchases=purchase['products']  # list of product as a value
                for product in p_purchases:
                    price=products[product]
                    if isinstance(price,int):
                        summ+=price
                summ=summ+(summ*purchase['taxes']/100)
        user['total_with_taxes']=summ
    return users


users=customer_total_cost(users,purchases,products)
print(users)
def fill_none(users,purchases,products):
    for user in users:
        sum = 0
        if user['total_amount'] is None:
            for purchase in purchases:
                if user['id'] == purchase['user_id']:
                    p_purchases = purchase['products']  # list of product as a value
                    for product in p_purchases:
                        price = products[product]
                        if isinstance(price, int):
                            sum += price

            user['total_amount'] = sum

    return users

users=fill_none(users,purchases,products)
print(users)

file1=open('test.txt','w')
file1.write(user['id'],user['total_amount'])