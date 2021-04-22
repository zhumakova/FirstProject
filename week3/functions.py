# def greetings(name):
#     print('hello' + name)
#
# greetings('vovan')
# def sum_of_3(a,b,c):
#     print(a+b+c)
# sum_of_3(1,2,3)

# def maximum_of_list(numbers):
#     return max(numbers)
#
#
# print(maximum_of_list([1, 2, 3, 4, 5, 6]))
# print(maximum_of_list([10,20,30]))


# def maximum_of_2():
#     num1=int(input())
#     num2=int(input())
#     if num1>num2:
#         print(num1)
#     else:
#         print(num2)
# maximum_of_2()
# maximum_of_2()


def register(username,password,confirm_password):
    if len(username) >=8 and not password.isalpha() and password==confirm_password:
        return username,password
    else:
        print('Пароли не совпадают')
try:
    username, password=register(input('username'),input('pas'),input('conf'))  #username,password( тут просто для вида присвоили значения, а так нужно вызвать return)
    print(username,password)
except TypeError:
    print('введите правильные данные')
def authorize(username1,password1):
    for i in range(3):
        if username1==username and password1==password:
            print("Success")
            break
        else:
            print('Not success')
authorize(input('user'),input('pass'))



