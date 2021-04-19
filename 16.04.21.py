# numbers=[1,2,3,4,5]
# for i in numbers:
#     print(i)


# for i in range(100):
#     print(i)

# numbers=[1,3,4,5,6,7]
# numbers1=range(100)
# print(type(numbers1))

#
# numbers=['red','yellow','green','blue']
# for i in range(len(numbers)):
#     print(numbers[i])

#
# numbers=['red','yellow','green','blue']
# for i in range(0,len(numbers),2):
#     print(numbers[i])
#

#
# #Четные числа
# for i in range(0, 1000, 2):
#     print(i)
#
#Четные числа
# for i in range(1, 1000, 2):
#     print(i)


# import random
# random_numbers=random.sample(range(1,30),20)
# print(random_numbers)
# for i in random_numbers:
#     print(i)

# import random
# random_numbers=random.sample(range(1,30),20)
# for i in range(len(random_numbers)):
#     print((random_numbers[i]))

# random_numbers = [1, 2, 3, 4, 6, 'red', '55', 2, [2, 4, 6], '354', 10, 20, 30, 5, 5, 6, 7, ]
# for i in random_numbers:
#     if isinstance(i, int) or isinstance(i, float):
#         print(i ** 2)
#ctrl+alt+l

# random_numbers = [1, 2, 3, 4, 6, 'red', '55', 2, [2, 4, 6], '354', 10, 20, 30, 5.6, 5, 6, 7, 3]
# sum=0
# for i in random_numbers:
#     if isinstance(i, int) or isinstance(i, float):
#         sum+=i
# print(sum)


# random_numbers = [1, 2, 3, 4, 6, 'red', '55', 2, [2, 4, 6], '354', 10, 20, 30, 5.6, 5,[ 6, 7, 3]]
# sum=0
# nested_sum=0
# for i in random_numbers:
#     if isinstance(i, int) or isinstance(i, float):
#         sum+=i
#     elif isinstance(i,list):
#         for j in i:
#          nested_sum+=j
#     print(sum,nested_sum)
#
# string1= 'hello'
# print(string1[0])

# article='lalllalllala ldl elrkf; rkjfnrekjfne nf ,deld llll Internet a sd'
# ban_word='Internet'
# if ban_word in article:
#     print('NOT OKAY!')
# else:
#     print('OK')

# article='lalllalllala ldl elrkf; rkjfnrekjfne nf ,deld llll Internet a sd'
# print(article.index('l'))

# article='sTriNgSsSs'
# article=article.capitalize()
# print(article)

# article='sTriNgSsSs lala Lala'
# article=article.title()
# print(article)

# article='       sTriNgSsSs lala Lala        '
# article=article.strip()
# print(article)

# article=' begimai sTriNgSsSs lala Lala vova'
# article=article.endswith('vova')
# print(article)


# article=' begimai sTriNgSsSs lala Lala vova'
# article=article.startswith('vova')
# print(article)

# article=' begimai sTriNgSsSs lala Lala vova'
# article=article.find('vova')
# print(article)
#
# article=' begimai sTriNgSsSs lala Lala vova'
# article=article.rindex('v')
# print(article)

# article=' begimai sTriNgSsSs lala Lala vova'
# article=article.rfind('v')
# print(article)

# article='begimaisTriNgSsSslalaLalavova'
#
# print(article.isalnum())

# article='begimaisTriNgSsSslalaLalavova'
#
# print(article.isalpha())

# article='begimaisTriNgSsSslalaLalavova'
#
# print(article.islower())

# article='begimaisTriNgSsSslalaLalavova'
#
# print(article.isupper())

# article='uSeRnAmE'
# article=article.lower()
# print(article)

# article='uSeRnAmE'
# article=article.lower()
# print(article)

# article='uSeRnAmE'
# article=article.upper()
# print(article)

# article='Vova is the best of best! Vova is one of that person who found impressive code to use!'
#
# article=article.replace('Vova','Begimai')
# print(article)

# article='Vova is the best of best! Vova is one of that person who found impressive code to use!'
#
# article=article.replace('Vova','Begimai')
# print(article)

# article='Vova is the best of best! Vova is one of that person who found impressive code to use!'
# article=article.swapcase()
# print(article)

article='Vova is the best of best! Vova is one of that person who found impressive code to use!'
article=article.replace('Vova',' ')
print(article)













