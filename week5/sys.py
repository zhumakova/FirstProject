"""
1. Вывести все коммиты (сообщения) и подсчитать все.
    1.1 Вывести сообщения длина которых больше 10 и их кол-во

"""
import sys
import requests


#Pagination

def fetch_url(url:str):
    r=requests.get(url)
    return  r


def get_commits(url:str):
    responses=fetch_url(url).json()
    for response in responses:
        print(responses['commit']['massage'])


def main():
    github_username=sys.argv[1]
    github_repository=sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits?page1&per_page=100'.format(github_username,github_repository)
    get_commits(url)
main()