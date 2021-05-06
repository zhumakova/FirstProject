"""
https://api.github.com/repos/ryanheise/audio_service
Системные параметры (sys.argv) username repository start_date end_date
1). Вывести все коммиты в данном промежутке времени
2. Вывести все pull requests созданные в данном промежутке времени (key:created_at)
3. Вывести все issues созданные в данном промежутке времени (key:created_at)
"""
import sys
import datetime

import requests


#Pagination


def fetch_url(url:str):
    r=requests.get(url,headers={'Authorization':'Token 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'}).json()
    return  r

def format_date(date:str):

    for response in responses:
        formated_date = datetime.datetime.strptime(response['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
        formated_date = datetime.date(formated_date.year, formated_date.month, formated_date.day)
    return formated_date


def get_commits(url:str):
    responses = fetch_url(url)
    for response in responses:
        # print(response)
        start_date=datetime.date(2020,11,1)


        end_date=datetime.date(2021,1,1)

        formated_date=datetime.datetime.strptime(response['commit']['author']['date'],'%Y-%m-%dT%H:%M:%SZ')
        formated_date=datetime.date(formated_date.year,formated_date.month,formated_date.day)
        if start_date<=formated_date<=end_date:
            commit_msg = response['commit']['message']

            print(commit_msg)



def main():
    github_username=sys.argv[1]
    github_repository=sys.argv[2]


    url = 'https://api.github.com/repos/{}/{}/commits'.format(github_username,github_repository)
    get_commits(url)
# main()
# print(time.time() - start_time)
main()

