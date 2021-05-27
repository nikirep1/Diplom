
a1 = float(input('Расстояние до НБ на авто:'))
a2 = float(input('Расстояние до НБ по ЖД:'))

y1 = 0
y2 = 0
if a1 >= 2500:
    y1 = 2.7 + 40
elif 1300 <= a1 < 2500:
    y1 = 2.5 + 40
elif a1 < 1300:
    y1 = 3.5 + 40

if a2 >= 2500:
    y2 = 1.8
elif 1300 <= a2 < 2500:
    y2 = 2.5
elif a1 < 1300:
    y2 = 3

import pulp as p
problem = p.LpProblem('problem',p.LpMinimize)
x1 = p.LpVariable('x1', lowBound=0)
x2 = p.LpVariable('x2', lowBound=0)

problem += a1*y1*x1 + a2 *y2*x2 #, 'Функция цели'
Z = int(input('Суммарный закакз, т:'))
problem += 20*x1 + 60*x2 >= Z #, '1'
T = int(input('Сколько доступно вагонов:'))
problem += x2 <= T
Av = int(input('Сколько автотранспорта доступно:'))
problem += x1 <= Av
print('1', problem)
status = problem.solve()
print('2',p.LpStatus[status])

print ('Результат:')
for variable in problem.variables():
    print (variable.name, '=', round(variable.varValue,0))
print ('Стоимость перевозки:')
print (round(p.value(problem.objective),2))
