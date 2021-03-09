p = (3,5) # распаковка
x,y = p
print(x,y)

auto = ['audi','bmw',('volvo','jelly')]
x,_,(y,z) = auto # можно откинуть некоторые значения,
print(f'{x}; china auto: {y}, {z}')

s = 'world'
a,b,c,d,e = s # так же работает со строками
print(a,b,d)

grades = [1,2,5,4,3,4,5,1,2,3,4,2,3,4,5,3,4,5,3,2,4,3,2,1,4,3,2,3]
def av(grades):
    first,*middle,last = grades #распаковка произвольной длины
    return sum(middle)/len(middle)
print(av(grades))

record = ('an','google@gmail.com','442-564','236-365')
name,mail,*number = record
print(name,':',number)

records = [                 #распаковка переменной длины
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]
def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':') #обработка строк
print(fields,sh)

city = (('msk','spb','ekb'),'rio','tokio','london','berlin')
(*_, ural), bra, jap, *_ = city # отбросить несколько
print(bra,jap,ural)

items = [1, 10, 7, 4, 5, 9]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(items))

from collections import deque
def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3); q.append(1)
print(q)
q.append(1)
print(q)

q = deque()
q.append(8); q.append(2); q.append(3); q.append(1)
print(q)
q.insert(1,6)
print(q)
q.appendleft(0)
print(q)

print(q.pop())
q.popleft()
print(q)

import heapq
nums = [1,8,2,23,7,-4,18,23,42,37,2,-10,50]
print(heapq.nlargest(3,nums)) #создает список максимальных элементов по убыванию
print(heapq.nsmallest(3,nums))

portfolio = [
     {'name': 'IBM', 'shares': 100, 'price': 91.1},
     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
     {'name': 'FB', 'shares': 200, 'price': 21.09},
     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
     {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nsmallest(3,portfolio, key=lambda  s: s['price'])) #сортирует с помощью лямбды по price
print(heapq.nlargest(3,portfolio, key=lambda  s: s['price']))

nums = [5,7,3,8,4,2,7,4,5]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)
heapq.heappop(heap)
print(heapq.heappop(heap))
print(heap)

#1.5. Реализация очереди с приоритетом
print('1.5 Реализация очереди с приоритетом')

import heapq

class priorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue,(-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = priorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

#1.6. Отображение ключей на несколько значений в словаре
print('1.6. Отображение ключей на несколько значений в словаре')

rd = {
    'a': [1,2,3],
    'b': [4,5]
}

rl = {'a': {1,2,3},
     'b': {4,5}
}
rd['f']= 4
print('eeeeeeeeeeeeeeeeee',rd)

from collections import  defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d.items())

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d.items())

d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)
print(d)

# d = {}
# for key,value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)

#1.7. Поддержание порядка в словарях
print('1.7. Поддержание порядка в словарях')


