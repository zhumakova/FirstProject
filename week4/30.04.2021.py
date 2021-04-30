# dict={'1','2','3'}
# dict1={'5','6','1'}
# dict.update(dict1)
# print(dict)
customers = [
    {'id': 1, 'username': 'steeve', 'age': 22, },
    {'id': 2, 'username': 'Gena', 'age': 22, },
    {'id': 3, 'username': 'santino', 'age': 22, },
    {'id': 4, 'username': 'francisco', 'age': 22, },
    {'id': 5, 'username': 'dagny', 'age': 22, },
    {'id': 6, 'username': 'johngalt', 'age': 22, },
]
annotate = {
    'M': '1 million',
    'K': '1 thousand',
    'H': '1 hundred',
    'B': '1 billion'
}
purchases = [
    {'id': 1, 'user_id': 2, 'product_name': 'tesla obligations', 'total_amount': '40M'},
    {'id': 2, 'user_id': 3, 'product_name': 'cigarettes', 'total_amount': '120K'},
    {'id': 3, 'user_id': 1, 'product_name': 'beer', 'total_amount': '9H'},
    {'id': 4, 'user_id': 4, 'product_name': 'cake', 'total_amount': '400K'},
    {'id': 5, 'user_id': 6, 'product_name': 'chair', 'total_amount': '4M'},
    {'id': 6, 'user_id': 5, 'product_name': 'coca-cola obligations', 'total_amount': '20B'},
]
"""
1. Соединить два словаря customers и purchases в новый словарь.
    1.1 Удалить из purchases ключ - id
    1.2 После слияния словарей - удалить ключ - user_id
2. Ключ total_amount в результативном списке - перевести в целое число, используя аннотацию
"""
def task1():
    pass
def task2():
    pass
new_list_of_customers=[]
def update_new_list(customers,purchases):
    for purchase in purchases:
        key_to_remove='id'
        purchase.pop(key_to_remove)
        for customer in customers:
           if customer['id']==purchase['user_id']:
                customer.update(purchase)
                key_w='user_id'
                customer.pop(key_w)
                if customer not in new_list_of_customers:
                    new_list_of_customers.append(customer)
    return customers
purchases=update_new_list(customers,purchases)
print(new_list_of_customers)

def rounded_number(new_list_of_customers):
    for new in new_list_of_customers:
       if new['total_amount'].endswith('B'):
           new['total_amount']=int(new['total_amount'].replace('B','000000000'))
       elif new['total_amount'].endswith('M'):
           new['total_amount'] = int(new['total_amount'].replace('M', '000000'))
       elif new['total_amount'].endswith('K'):
           new['total_amount']=int(new['total_amount'].replace('K','000'))
       elif new['total_amount'].endswith('H'):
           new['total_amount']=int(new['total_amount'].replace('H','00'))

    return new_list_of_customers

new_list_of_customers=rounded_number(new_list_of_customers)
print(new_list_of_customers)







