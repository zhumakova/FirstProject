# numbers=[10,20,30,40]
#
# for number in numbers:
#     if number%2==0:
#         print(number)

# try:
#     #упсешно
#     print('1'+'1')
# except TypeError:
#     # В случае ошибки
#     print('except')
# finally:
#     # Всегда
#     print('finally')

# names=['vova','aliya','begimai','erbol','cholpon','jamilya','bakyt']
# salaries=[0,10000,20000,None,30000,None,None]
# i=0
# while i<len(salaries):
#     try:
#         salaries[i]*=2
#     except TypeError:
#         salaries[i]=0
#     i+=1
# print(salaries)

names=['vova','aliya','begimai','erbol','cholpon','jamilya','bakyt']
salaries=[0,10000,20000,30000]
i=0
while i<len(names):
    try:
        salaries[i]*=2
    except IndexError:
        salaries.append(0)
    i+=1
print(salaries)