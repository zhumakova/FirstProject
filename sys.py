"""
1. Вывести все коммиты (сообщения) и подсчитать все.
    1.1 Вывести сообщения длина которых больше 10 и их кол-во
    1.2 Вывести пользователей кто сделал коммит
    1.3 Вывести по каждому пользователю его кол-во коммитов
    ДЗ Запуск программы через терминала с указом имени пользователя и репозитория
"""
import sys
import time
import requests


#Pagination

start_time = time.time()

def fetch_url(url:str):
    r=requests.get(url,headers={'Authorization':'Token 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'})
    return  r


def get_commits(url:str):
    responses = fetch_url(url).json()
    for response in responses:
        commit_msg = response['commit']['message']
        if len(commit_msg) > 10:
            print(commit_msg)


def get_users(url:str):
    responses = fetch_url(url).json()
    author_list = []
    for response in responses:
        author = response['commit']['author']['name']
        if author not in author_list:
            author_list.append(author)
            print(author_list)
    return author_list,responses


def get_commits_by_user(url:str):
    authors,responses = get_users(url)
    for author in authors:
        commits_count = 0
        for response in responses:
            commit = response['commit']
            if commit['author']['name'] == author:
                commits_count += 1
        print(commits_count)

def main():
    github_username=sys.argv[1]
    github_repository=sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits?page1&per_page=100'.format(github_username,github_repository)
    get_users(url)
# main()
# print(time.time() - start_time)
main()

























