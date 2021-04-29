# dict1={'a':1,'b':2,'c':3}
# dict2={'a':33,'z':2,'x':3}
#
# dict1.update(dict2)
# print(dict1)

import pprint
users = [{'id':1,'user': 'digital', },
         {'id':2,'user': 'maksim', },
         {'id':3,'user': 'vova', },
         {'id':4,'user': 'begimai', },
         {'id':5,'user': 'aliya', },
         {'id':6,'user': 'bakyt',},
         {'id':7,'user': 'chingiz', },
         {'id':8,'user': 'jamilya',},
         {'id':9,'user': 'cholpon', },
         {'id':10,'user': 'erbol', }
         ]
posts = [{'id':1,'text':'hiring','status':'sponsored','keyword':'nic1'},
         {'id':2,'text':'text1','status':'pub'},
         {'id':3,'text':'text2','status':'pub'},
         {'id':4,'text':'text3','status':'pub'},
         {'id':5,'text':'text4','status':'pub'},
         {'id':6,'text':'text5','status':'pub'},
         {'id':7,'text':'Canada immigration','status':'sponsored','keyword':'interested!'}]
comments = [{'id':1,'user_id':1,'post_id':1,'comment':'This is not nic1'},
            {'id':2,'user_id':2,'post_id':1,'comment':'Hello this is nic1'},
            {'id':3,'user_id':3,'post_id':2,'comment':'looking good!'},
            {'id':4,'user_id':4,'post_id':2,'comment':'awesome!'},
            {'id':5,'user_id':5,'post_id':2,'comment':'LGTM'},
            {'id':6,'user_id':6,'post_id':3,'comment':'here we go!'},
            {'id':7,'user_id':6,'post_id':4,'comment':'not ok'},
            {'id':8,'user_id':6,'post_id':7,'comment':'interested!'},
            {'id':9,'user_id':6,'post_id':7,'comment':'woohoo!'},
            {'id':10,'user_id':6,'post_id':7,'comment':'interested!'}]
"""
1. Нужно найти все posts со статусом sponsored!
2. Найти комментарии к posts sponsored
3. Среди найденных комментариев найти те что содержат keyword из posts
"""

filtered_list=[]
def all_posts_sponsored(posts):
    """

    :param posts: Список постов
    :return: Отфильтрованный список
    """

    for post in posts:
        if post['status']=='sponsored':
            filtered_list.append(post)
            posts =filtered_list
    return posts
posts=all_posts_sponsored(posts)
pprint.pprint(posts)


def ap_comments(posts):
    """

    :param posts: Список постов
    :param comments: Список комментариев
    :return: Отфильтрованный список
    """

    for post in posts:
        if post['status'] == 'sponsored':
            post['comments'] = []
            for comment in comments:


                if post['id']==comment['post_id']:

                    post['comments'].append(comment['comment'])

    return posts
posts =ap_comments(posts)
print(posts)

def key_word(posts):
   for post in posts:
       key=post['keyword']
       for comment in post['comments']:
           if key not in comment:
               post['comments'].remove(comment)
   return posts
posts=key_word(posts)
print(posts)
us_comment = []
def users_comments(users):
    for post in posts:
        key=post['keyword']

        for comment in comments:
            if key in comment['comment']:

                for user in users:
                    if comment['user_id']==user['id']:
                        user1=user
                        print(user1)
                        us_comment.append(user1)
    return us_comment

users=users_comments(users)
print(us_comment)



