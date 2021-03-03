# x = 5
# print(x)
# y=123.9
# print(type(y))
# x= (int(y))
# print(x)
# print(round(y))
# name = input()
# print(name)

# name = input('как тебя зовут? ')
# print(f'привет, {name}!')
# lastname = input('как твоя фамилия? ')
# print(f'ясно, {lastname}!')
#
# print(name + ' '+ lastname)

# x = 2
# y = x+7>x+2*x**3**x
# print(y)
# if y is False:
#     break

# x = 10
# while True:
#     x -= 1 # x = x - 1 декрементация
#     if x < 0:
#         break
#     print(x)
# print('все')

# x = 10
# while x >= 0:
#     print(x)
#     x-=1

# for x in 3,6,7:
#     print(x**2)

# A = range(1,10)
# for x in A:
#     print(x)

# x = int(input())
# y = int(input())
# if y > 0:
#     if x > 0 :
#         print(1)
#     else:
#         print(2)
# else:
#     if x < 0:
#         print(3)
#     else:
#         print(4)

# x = int(input())
# y = int(input())
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# elif x > 0 and y < 0:
#     print(4)
# else:
#     print('never')

# import turtle
# wn = turtle.Screen()
#
# def david():
#     for step in range(6):
#         turtle.begin_fill()
#         for step in range(3):
#             turtle.forward(50)
#             turtle.left(120)
#         turtle.end_fill()
#
#         turtle.forward(50)
#         turtle.right(60)
#
#
# turtle.shape('turtle')
# turtle.color('red', 'yellow')
# turtle.speed(15)
# turtle.pensize(3)
#
# david()
# turtle.hideturtle()
#
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# turtle.speed(15)
# x = 10
# y = -5
# while True:
#     for step in range(4):
#         turtle.forward(x)
#         turtle.left(90)
#     turtle.penup()
#     turtle.goto(y,y)
#     turtle.pendown()
#     x +=10
#     y -= 5
#
# wn.exitonclick()
#
# x = 5
# y = 7
# x,y = y,x
# print(x,y)

# T = 1,2,3,5 #кортеж
# print(type(T))
# *rest,c,d = T
# print(rest)
# print(*T,sep=':',end='!\n') #кортеж запишет попорядку, : между числами, в конце "!"

# def hello_n(name:str,n:int): #функция hello с параметром name,
#                              #с типом по предположению строка, параметр n типа int
#     for i in range(n):
#         print("привет",name)
#
# hello_n('Вася',5)
# hello_n('Петя',5)
# V = 'Саша',5
# hello_n(*V)

# A = range(1,10)
# print(A[0:6]) #range(1, 7)
# for x in A:
#     print(x)

# A = [(1,10),(2,20),(3,30)]
# for i in range(len(A)):
#     T = A[i]
#     print(T)

# A = [(1,10),(2,20),(3,30)]
# for T in A:
#     print(T)
#
# import turtle
# wn = turtle.Screen()
# A = [(7,10),(6,20),(8,30)]
# for angle,length in A:
#     turtle.forward(length)
#     turtle.circle(angle)
# wn.exitonclick()

# A = [5,6,7,2,6,9]
# for i,x in enumerate(A): #чтобы пронумеровать
#     print(i,x)

'''множества(set) и словари(dict)'''

# s = {'msk','kzn','spb'} #множество
# h = {'msk','kzn','ncl'}
# s.add('ekb') # добавить в множество
# if 'msk' in s:
#     print('да')
# print(s & h)
# print(s | h)

# D = {'msk':78627, # СЛОВАРЬ
#      'kzn':45614,
#      'ncl':5217,
#      'spb':66125}
# D['ekb']={'pr.mira','r.lenina'}
# print(D)
# for key in D.items():
#     print(key)

'''функции. локальность имен'''
#
# def bar():
#     pass
# x = bar()
# print(x) #None

# def bar(X,y): # X,y формальные параметры
#     X[0]=7*y
#     X = [2,3,5,6]
#     print('локальный объект, который уничтожится ',X)
#
# A = [1,2,3,4]
# y=bar(A,3) # A,3 фактические параметры
# print(A)

'''в питон типизация не строгая, аннотация не запрещает'''
# def foo(x:str,y:int): # x строка, y целое число, но не обязательно
#     result = x
#     for i in range(y-1):
#         result += x
#     return result
# z = foo(2,5)
# print(z)
# z = foo('MA',2)
# print(z)

'''параметр по умолчанию'''
# def foo(x,y=0,z=0): # z=0 значение по умолчанию
#     return 100*x+10*y+1*z
#
#
# print(foo(1,2,3)) # по умолчанию позиционирование по порядку
# print(foo(z=1,x=2,y=3)) # именованные параметры (ключевые), можно только, которые есть
# print(foo(1,2)) # будет использовано значение по умолчанию
# print(foo(7))

'''функция с неограниченным количеством параметров'''
# def bar(*args, named_parametr='bar'):
#     for arg in args:
#         print(named_parametr,'arg =', arg)
#
# bar()
# bar(['the','list','of','strings'])
# bar(1,2,3)
# bar('jelly','fish')
# bar('jelly','fish',named_parametr='SEPARATOR')

'''качество кода, лекция 4'''


# x=1
# y=2
# print('{x},{y}'.format(x=10,y=5))
# print(f'{y},{x},{x}')
# print(x,y)

# x = (1,'list','of','strings')
# a2,_,w,_ = x
# print(f'{a2},{w}')


# txt = 'this is an awesome text'
# text = txt.split()
# temp = 0
# temp_word = 'none'
# for i in text:
#     if len(i) > temp:
#         temp = len(i)
#         temp_word = i
# print(temp_word)

# '''лекция 5'''

def main():
    x, y = 100, 0
    widht, height = 200, 300
    draw_house(x, y, widht, height)


def draw_house(x, y, widht, height):
    '''
    Функция рисует дом с шириной width и высриы height от опорной точки (x,y),
    которая находится в середине нижней точки фундамента
    :param x: координата х середины домика
    :param y: координата у низа домика
    :param wight: полная ширина домика
    :param height: полная высота домика
    :return:
    '''
    print('рисую дом с параметрами,', x, y, widht, height)
    foundation_height = 0.05 * height
    walls_widht = 0.9 * widht
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, widht, foundation_height)
    draw_house_walls(x, y + foundation_height, walls_height, walls_widht)
    draw_house_roof(x, y + foundation_height + walls_height, widht, roof_height)


def draw_house_foundation(x, y, widht, height):
    print('рисую фундамент с параметрами,', x, y, widht, height)
    '''
        нарисовать основание дома с шириной width и высриы height от опорной точки (x,y),
        которая находится в середине нижней точки фундамента
        :param x: координата х середины фундамента
        :param y: координата у низа фундамента
        :param wight: полная ширина фундамента
        :param height: полная высота фундамента
        :return:
        '''
    pass


def draw_house_walls(x, y, widht, height):
    print('рисую стену с параметрами,', x, y, widht, height)
    pass


def draw_house_roof(x, y, widht, height):
    print('рисую крышу с параметрами,', x, y, widht, height)
    pass


main()
