# my_list=['honda','honda','bmw','mercedes','bugatti']
# print(my_list.index('honda'))
# print(my_list[0])
# print(my_list.count('honda'))
# my_list.sort()
# print(my_list)
# my_list.pop()
# print(my_list)


# my_list=['honda','honda','bmw','mercedes','bugatti']
# copy_my_list=my_list.copy()
# print(copy_my_list)


# list1=[1,2,3]
# list2=list1.copy()
# del list1[0]
# print(list2)

# my_list=['honda','honda','bmw','mercedes','bugatti']
# # my_list.append('lexus')
# # print(my_list)

# my_list=['honda','honda','bmw','mercedes','bugatti']
# my_list.insert(1,'ford')
# print(my_list)

# my_list=['honda','honda','bmw','mercedes','bugatti']
#
# extend_list=['hello','ghetto']
# my_list.extend('Hello')
# print(my_list)

# my_list=['honda','honda','bmw','mercedes','bugatti']
# my_list.remove('honda')
# print(my_list)

# my_list=['honda','honda','bmw','mercedes','bugatti']
# my_list.reverse()
# print(my_list)
#
# my_list=['honda','honda','bmw','mercedes','bugatti']
# numbers=[1,2,3,4,5,6]
# print(my_list[2:])
# print(my_list[:3])
# print(my_list[1:4])
# print(numbers[0:4])
# print(numbers[0:5:2])

# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(numbers[::3])

# numbers=[1,2,3,4,5,6,7,8,9,10]
# print(numbers[::-2])


# data = ['Wt','Ht',342432423424324,5.996,5.77778,'Insurance_History_2',34243242342432124545312312534534534,'Insurance_History_4','Insurance_History_5', 'Insurance_History_7',234242049004328402384023849028402348203,55, 66, 11, 'Medical_Keyword_3','Medical_Keyword_4', 'Medical_Keyword_5', 'Medical_Keyword_6', 34243242342432124545312312534534534534503495345,'lalalalallalalalalalalalalalalala', 23409284028430928420483209482904380428, 'Medical_Keyword_10', 'Medical_Keyword_11',92384923849023849023842903482934324290, 93429423018319238192004829423482942, 'Medical_Keyword_14', 'Medical_Keyword_15','Medical_Keyword_16', 5.888, 'Medical_Keyword_18asfdasfdasfdasfdasdfasdfas','Medicagsfgsfgsfkgjsfkg',9.131, 0.978, 'Famidasdasdlasdlaspdlaspdlasp2948203948', 'Familygsdglksflg2849023840923;fksdkgsd234234234238409238490238','Family_Hist_4','Family_Hist_5', 9.19, 'Medical_History_2', 'Medical_History_3', 'Medical_History_4',13, 'Medical_History_6', 'Medical_History_7', 111, 'Medical_History_9',123.7773, 'Medical_History_41', 55823428882482374824828472348,'Product_Info_3',1111111111111111111111, 'Product_Info_5']
#
# i=0
# while i<len(data):
#     obj = data[i]
#     if isinstance(obj ,float):
#
#         if obj%1>=0.8 or obj%1<=0.2:
#             data[i] = round(obj)
#         else:
#             data[i]=int(obj)
#
#     elif isinstance(obj,int):
#         str_1=str(obj)
#         if len(str_1)>20:
#             del data[i]
#             i-=1
#
#     elif isinstance(data[i],str):
#         if len(data[i])>50:
#             del data[i]
#             i-=1
#     i+=1
#
# print(data)


data = ['Wt','Ht',342432423424324,5.996,5.77778,'Insurance_History_2',34243242342432124545312312534534534,'Insurance_History_4','Insurance_History_5', 'Insurance_History_7',234242049004328402384023849028402348203,55, 66, 11, 'Medical_Keyword_3','Medical_Keyword_4', 'Medical_Keyword_5', 'Medical_Keyword_6', 34243242342432124545312312534534534534503495345,'lalalalallalalalalalalalalalalala', 23409284028430928420483209482904380428, 'Medical_Keyword_10', 'Medical_Keyword_11',92384923849023849023842903482934324290, 93429423018319238192004829423482942, 'Medical_Keyword_14', 'Medical_Keyword_15','Medical_Keyword_16', 5.888, 'Medical_Keyword_18asfdasfdasfdasfdasdfasdfas','Medicagsfgsfgsfkgjsfkg',9.131, 0.978, 'Famidasdasdlasdlaspdlaspdlasp2948203948', 'Familygsdglksflg2849023840923;fksdkgsd234234234238409238490238','Family_Hist_4','Family_Hist_5', 9.19, 'Medical_History_2', 'Medical_History_3', 'Medical_History_4',13, 'Medical_History_6', 'Medical_History_7', 111, 'Medical_History_9',123.7773, 'Medical_History_41', 55823428882482374824828472348,'Product_Info_3',1111111111111111111111, 'Product_Info_5']
clear_data=[]
i=0
while i<len(data):
    obj = data[i]
    if isinstance(obj ,float):

        if obj%1>=0.8 or obj%1<=0.2:
            clear_data.append(round(obj))
        else:
            clear_data.append(int(obj))

    elif isinstance(obj,int):
        str_1=str(obj)
        if len(str_1)<=20:
            clear_data.append(str_1)

    elif isinstance(obj,str):
        if len(obj)<=50:
            clear_data.append(obj)
    i+=1

print(clear_data)