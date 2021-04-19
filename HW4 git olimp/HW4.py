# #Даны три стороны треугольника a,b,c. Определите тип треугольника с
# заданными сторонами
import math
a=float(input('Сторона а: '))
b=float(input('Сторона b: '))
c=float(input('Сторона c: '))
if a==b and b==c:
    print("Равносторонний треугольний!")
elif c==math.sqrt(a**2+b**2) or a==math.sqrt(c**2+b**2) or b==math.sqrt(a**2+c**2) :
    print('Прямоугольный треугольник!')
elif a==b or b==c or a==c:
    print('Равнобедренный треугольний!')

else:
    print('Обычный разносторонний треугольник!')