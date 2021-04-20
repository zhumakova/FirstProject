# list1=[1,2,3]
# tuple1=(1,2,3)
# dict1={3,2,4,2,2,1} #set
# student={'name':'Vova',
#          'list_name':'Zinkovsky',
#          'age':17,
#          'hobbies':['play','programming','reading']
#          }
# student['hobbies'].append('english')
# student['hobbies'].extend(['english','easy','finance'])
#
# print(student['hobbies'])


# student={'name':'Vova',
#          'list_name':'Zinkovsky',
#          'age':17,
#          'hobbies':['play','programming','reading']
#          }
# student['hobbies'].append('english')
# student['hobbies'].extend(['english','easy','finance'])
# name=student.pop('name')
#
# print(student)
# print(name)

# student={'name':'Vova',
#          'list_name':'Zinkovsky',
#          'age':17,
#          'hobbies':['play','programming','reading']
#          }
# student['hobbies'].append('english')
# student['hobbies'].extend(['english','easy','finance'])
#
# for i in student:
#     print(student[i])

students = [{"name":"Vova",
           "last_name":"Zinkovsky",
           "age":17,
           "scores":[1,2,3,4,5]  ,
           "hobbies":['play','programming','reading']
           },
            {"name": "Begimai",
             "last_name": "Zhumakova",
             "age": 18,
            "scores":[5,5,3,4,5],
             "hobbies": ['pubg', 'programming', 'reading','walking']
             },
            {"name": "Aliya",
             "last_name": "Andabekova",
             "age": 18,
                "scores":[1,4,3,1,2]  ,
             "hobbies": ['programming', 'reading','drawing']
             },
            {"name":"Cholpon",
           "last_name":"Kaimova",
           "age":16,
            "scores":[5,2,4,4,5]  ,
           "hobbies":['pubg','programming','reading','anime',]
           },
            {"name":"Bakyt",
           "last_name":"Asanaliev",
           "age":35,
            "scores":[],
           "hobbies":['play','programming','reading','footbal','history']
           },
            {"name":"Maksim",
           "last_name":"Surovkin",
           "age":22,
            "scores":[1,1,1,1,1] ,
           "hobbies":['programming','reading','traveling','cycling']
           }
            ]
general_avg=0
student_avg=[]
std=0
sum1 = 0


for student in students:
    # print(student['scores'])
    sum = 0
    for score in student['scores']:
        sum+=score
    # print(sum)
    try:
        student_avg.append(sum / len(student['scores']))
    except ZeroDivisionError:
        student_avg.append(0)

#print(student_avg)
for i in student_avg:
    sum1+=i
#print(sum1)
general_avg=(sum1 / len(student_avg))
#print(general_avg)
max=0
min=5
k=0
                                                        # while k<len(student_avg):
                                                        #     if student_avg[k]>max:
                                                        #         max = student_avg[k]
                                                        #     elif student_avg[k]<min:
                                                        #         min = student_avg[k]
                                                        #     k += 1
for stud_avg in student_avg:
    if stud_avg>max:
        max = stud_avg
    elif stud_avg<min:
        min = stud_avg
    k += 1
std=max-min
print(student_avg,round(general_avg,2),round(std,2),sep='\n')

                        # students[0]['avg']=5
                        # print(students)

dict_loop = 0
import pprint

for student in students:
    student['avg'] = student_avg[dict_loop]
    dict_loop += 1
pprint.pprint(students)
