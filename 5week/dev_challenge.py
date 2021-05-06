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
    r = requests.get(url)
    return r.json()


def to_datetime(date:str):
    if 'T' not in date:
        result_date = datetime.datetime.strptime(date,'%Y-%m-%d')
        result_date = datetime.date(result_date.year,result_date.month,result_date.day)
    else:
        result_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        result_date = datetime.date(result_date.year, result_date.month, result_date.day)
    return result_date


def get_commits(url:str,start_date:str,end_date:str):
    commits = []
    url = url + '/commits'
    start_date = to_datetime(start_date)
    end_date = to_datetime(end_date)
    responses = send_request(url)
    for response in responses:
        commit_date = to_datetime(response['commit']['author']['date'])
        commit = response['commit']['message']
        if start_date<=commit_date<=end_date:
            commits.append(commit)
    return commits


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
    print(get_commits(url, start_date,end_date))
    print(get_pulls(url, start_date, end_date))
    print(get_issues(url, start_date, end_date))
main()

