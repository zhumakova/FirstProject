# Дан список обьектов спам-писем пришедших на почту. С помощью метода split найти слово
# которое повторяется в списке больше всего (напомню что split возвращает из строки – список).
# Найденное слово сохранить в переменную.
# Далее на вход подается единственная строка – нужно проверить спам это или нет

data = [
    {'text':'oh hi duuuude how r uy??check this 1xbet'},
    {'text':'Dear Harry Potter, i am Frodo Baggins i represent 1xbet company.Best bet service'},
    {'text':'wooooh yoow harry look at my jackpot 100000000$ at 1xbet service'},
    {'text':'Harry , today i saw the man who looks like Hawkeye from Avengers on 100% and he dont use 1xbet service'},
]
final_mail = 'Hello Harry, my name is Maksim, Im still waiting for the letter from Hogwarts'
list=final_mail.split()
# print(list)
q_spam=0
spam_word=''
database=[]
for mail in data:
    str=mail['text'].lower().split()
    database.extend(str)

for word in database:
    quantity=database.count(word)
    #print(quantity)
    if quantity>q_spam:
        q_spam=quantity
        spam_word=word
print(q_spam,spam_word)

if spam_word in final_mail.lower():
    print('Mail is not OK')
else:
    print("Mail is OK")
