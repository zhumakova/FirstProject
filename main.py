# 12.04.2021
# x=int(input())
# print(x%100//10)

# x="4.5"
# print(type(x))
#
# price="500"
# if isinstance(price,int):
#     print(price,'ok')
# else:
#     price=int(price)
#     print(price,'not ok')

# import random
# print(random.randint(1,1000))

# import random
# secret_number=random.randint(1,10)
# print(secret_number)
# guess_number=int(input("Число от 1 до 10: "))
#
# if secret_number==guess_number:
#     print("chocolate")
# else:
#     print("=(")

# import random
# secret_number=random.sample([1,2,3,4,5,6,7,8,9,0],4)
# print(secret_number)


# import random
# secret_number= random.randrange(10000)/100
# print(secret_number)

# print(round(5.49959593,1))

# money=float(input('Сколько денег: '))
#
# years=int(input('Сколько лет:' ))
# percentage = int(input('проценты:'))
# money1=(money*percentage/100)*years
# money3=money+money1
# som=money3//1
# tyiyn1=money3%1
# tyiyn2=tyiyn1*100
# tyiyn=tyiyn2//1
# print('som:',som,'tiyin:',tyiyn)

price=float(input('Цена: '))
quantity=float(input('количество: '))
result=price*quantity
som=int(result)

tyiyn=(result-som)*100
tyiyn1=int(tyiyn)


print('som:',som,'tyiyn:',tyiyn1)

