"""Дан сложный список категорий товаров ( словарей) для каждой категории существует
соответствующий список словарей каждого обьекта товара конкретной категории.
Требуется узнать:
1.Самую дорогую категорию товаров.
2. Самую популярную категорию товаров
3. Товар с наименьшей и наибольшей стоимостью.
Каждый ответ выводить в таком формате: {
‘most_popular_category’:’total_popularity’"""
import pprint
data = [
    {'dress':[
                {'name':'louis vuitton',
                'popularity':500,
                 'price':1000
                },
                {'name':'versace',
                'popularity':21,
                 'price':888
                },
                {'name':'supreme',
                'popularity':57,
                 'price':765
                },
    ]
    },
    {'jeans':[
                {'name':'adidas',
                'popularity':42,
                 'price':2300
                },
                {'name':'armani',
                'popularity':67800,
                 'price':110
                },
                {'name':'casio',
                'popularity':230,
                 'price':3000
                },
    ]
    },
    {'t-shirt':[
                {'name':'tom ford',
                'popularity':999,
                 'price':5000
                },
                {'name':'lacoste',
                'popularity':777,
                 'price':230
                },
                {'name':'luxury',
                'popularity':876,
                 'price':2300
                },
    ]
    }
]
# list1=['dress','jeans','t-shirt']
# i=0
# category_price={}
#                 # pprint.pprint(data[0]['dress'][0]['price'])
# for category in data:
#          #  # print(category)
#         #     # print(category.keys())
#     category_sum=0
#     key=list1[i]
#     category_value=category[key]
#     for product in category_value:
#         category_sum+=product['price']
#     category_price[key]=category_sum
#     i+=1
# print(max(category_price.values()),category_price)


                                    # list1=['dress','jeans','t-shirt']
                                    # k=0
                                    # max1=0
                                    #
                                    # most_popular_category={}
                                    #
                                    # for category in data:
                                    #     category_sum = 0
                                    #     key=list1[k]
                                    #     category_value=category[key]
                                    #     for product in category_value:
                                    #         category_sum += product['popularity']
                                    #     most_popular_category[key]=category_sum
                                    #     if most_popular_category[key]>max1:
                                    #         max1=most_popular_category[key]
                                    #     if most_popular_category[key]<min:
                                    #
                                    #     k+=1
                                    # print('max=',max1)
                                    # print(max(most_popular_category.values()),most_popular_category)


list1 = ['dress', 'jeans', 't-shirt']
i = 0
price_list= []

for category in data:
    key = list1[i]
    value = category[key]
    # print(value)
    for product in value:
       price_list.append(product['price'])
    i+=1
print(max(price_list),min(price_list))



