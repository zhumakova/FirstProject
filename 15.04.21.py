# numbers=[1,2,3,4,5,6,7,8,8,9,14,15,16,29,9,3]
# max_number=0
# i=0
# while i<len(numbers):
#     if numbers[i]>max_number:
#         max_number=numbers[i]
#     i+=1
# print(max_number)

# numbers=[1,2,3,4,5,6,7,8,8,9,14,15,16,29,9,30,31]
#
# i=0
# while i<len(numbers)-1:
#     if numbers[i]>numbers[i+1]:
#        numbers[i+1]=numbers[i]
#     i+=1
# print(numbers[i])

# numbers=[1,2,3,4,5,6,7,8,8,9,14,15,16,29,9,30,31]
# i=0
# sum=0
# while i<len(numbers):
#     sum+=numbers[i]
#     i+=1
# print(sum)

# numbers=[1,2,3,4,5,6,7,8,8,9,14,15,16,29,9,30,31]
# i=0
# max_num=0
#
# while i<len(numbers):
#     if numbers[i]>max_num:
#         max_num=numbers[i]
#     i+=1
# second=0
# i=0
# while i<len(numbers):
#     if numbers[i]>second and numbers[i]<max_num:
#         second=numbers[i]
#     i+=1
# print(max_num,second)

# numbers = [1, 2, 3, 4,  7, 8, 8, 9, 14, 16, 16,16, 29, 9, 30, 31]
# # Найти количество похожих цифр (соседей)
# i=0
# sum=0
# summ=0
# while i<len(numbers)-1:
#     if numbers[i]==numbers[i+1]:
#        sum=numbers[i]
#     if sum==numbers[i]:
#        summ=summ+1
#     i+=1
# print(summ)

# numbers = [1, 2, 3, 4,  7, 8, 8, 9, 14, 16, 16,16, 29, 9, 30, 31]
# # Найти количество похожих цифр (соседей)
# i=0
# sum=0
# summ=0
# while i<len(numbers)-1:
#     if numbers[i]==numbers[i+1]:
#        sum=numbers[i]
#     if sum==numbers[i]:
#        summ=summ+1
#     i+=1
# print(summ) домашняя работа

# numbers = [1, 2, 3, 4, 7, 8, 8, 9, 14, 16, 16, 16, 29, 9, 30, 31]
# gt_ten=0
# i=0
# while i<len(numbers):
#     if numbers[i]>10:
#         gt_ten+=1
#     i+=1
# print(gt_ten)

numbers = [1, 2, 3, 4, 7, 8, 8, 9, 14, 16, 16, 16, 29, 9, 30, 31]
uniq_numbers=[]
i=0
while i<len(numbers):
    if numbers[i] not in uniq_numbers:
        uniq_numbers.append(numbers[i])
    i+=1
uniq_numbers.sort()
print(uniq_numbers)
