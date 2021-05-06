from decouple import config
import requests
import sys
import datetime
"""
https://api.github.com/repos/ryanheise/audio_service
Системные параметры (sys.argv) username repository start_date end_date
1. Вывести все коммиты в данном промежутке времени
2. Вывести все pull requests созданные в данном промежутке времени (key:created_at)
3. Вывести все issues созданные в данном промежутке времени (key:created_at)

"""


def send_request(url:str):
    """

    :param url:ссылка в параметре url
    :return: возвращаем ссылку в json формате для получения ее ввиде словаря
    """
    r = requests.get(url,headers={'Authorization':f'Token {config("token")}'}) #получаем даные из ссылки и используем
    # токен для неоднократного запроса на эту же страницу
    return r.json()


def to_datetime(date:str):
    """

    :param date: параметр для формата строки в формат даты
    :return: возвращаем значение даты
    """
    if 'T' not in date: # если "T" присутствует в введенном или обращенном значении даты (в строке) то:
        result_date = datetime.datetime.strptime(date,'%Y-%m-%d') # сохраняем в переменную наше изменненую из строки в дату значение
        result_date = datetime.date(result_date.year,result_date.month,result_date.day)
    else:
        result_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        result_date = datetime.date(result_date.year, result_date.month, result_date.day)
    return result_date


def get_commits_by_users(url:str,start_date:str,end_date:str):
    commits=[]
    author_list=[]
    url = url + '/commits'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    for response in responses:
        author = response['author']['login']
        commit_date = to_datetime(response['commit']['author']['date'])
        commit = response['commit']['message']

        if start_date<=commit_date<=end_date:
            commits.append(commit)
            if author not in author_list:
                author_list.append(author)
    author_dict={}
    for author in author_list:
        count_commits = 0
        for response in responses:
            login = response['author']["login"]
            if login==author:
                count_commits+=1
        author_dict[author]=count_commits

    return commits,author_dict

def get_pulls(url:str,start_date:str,end_date:str):
    pulls = []
    url = url + '/pulls'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    for response in responses:
        pulls_date = to_datetime(response['created_at'])
        pulls_title = response['title']
        if start_date<=pulls_date<=end_date:
            pulls.append(pulls_title)
    return pulls

def get_issues(url:str,start_date:str,end_date:str):
    issues = []
    url = url + '/issues'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    for response in responses:
        issues_date = to_datetime(response['created_at'])
        issues_title = response['title']
        if start_date<=issues_date<=end_date:
            issues.append(issues_title)
    return issues

def main():
    github_username = sys.argv[1]
    github_repository = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}'.format(github_username,github_repository)
    start_date = sys.argv[3]
    end_date = sys.argv[4]
    print(get_commits_by_users(url, start_date,end_date))
    print(get_pulls(url, start_date, end_date))
    print(get_issues(url, start_date, end_date))
main()
