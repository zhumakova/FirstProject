"""
1. Вывести все коммиты (сообщения) и подсчитать все.
    1.1 Вывести сообщения длина которых больше 10 и их кол-во

"""
import sys

import requests
url = 'https://api.github.com/repos/{}/{}/commits?page1&per_page=100'.format(sys.argv[1],sys.argv[2])
response = requests.get(url,headers={'Authorization':'Token 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'}).json()

commit=[]

for r in response:
    commit.append(r['commit']['message'])
    sum=0
# print(commit)
    count = 0
    for massage in commit:
        sum+=1


        if len(massage)>10:
            count+=1
    print(massage)
print('total commits-',sum)
print('total commits that are great than 10-',count)
user=[]
for r in response:
    if r['commit']['author']['name'] not in user:
        user.append(r['commit']['author']['name'])
print(user)