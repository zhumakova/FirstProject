# my_list=[1,2,3,4,5]
# print(type(my_list))
#
# my_tuple=(1,2,3,4,5,6)
# print(type(my_tuple))


# criminals=['plov','manty','kola','sprite','shaurma']
# name=input()
# if name not in criminals:
#     criminals.append(name)
# print(criminals)

# user_info=[[],[]]
# username=input()
# password=input()
# check_password=input()
# if password==check_password:
#     user_info[0].append(username)
#     user_info[1].append(password)
# print(user_info)

user_info=[[],[]]
while True:

    username=input()
    password=input()
    check_password=input()
    if username=='1':
        break
    if password==check_password:
        user_info[0].append(username)
        user_info[1].append(password)
    print(user_info)