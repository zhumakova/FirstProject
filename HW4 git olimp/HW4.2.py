#  Даны три целых числа A, B, C. Определить, есть ли среди них хотя бы одно
# четное и хотя бы одно нечетное.
A=int(input('A='))
B=int(input('B='))
C=int(input('C='))
if A%2==0 or B%2==0 or C%2==0:
    print('Got at least one even number!')
if  A%2!=0 or B%2!=0 or C%2!=0:
    print('Got at least one odd number')