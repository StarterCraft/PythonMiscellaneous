# Библиотека
import time
import math

# Инструкция для пользователя
print('''
Здравствуйте, уважаемый пользователь!
Данный универсальный калькулятор PythonCalc v 1.0 умеет выполнять 5 различных операций,
сохранение/сброс результата вычисления.
Версия 1.0 исполняется с помоощью командной строки.
Для начала вычислений, пожалуйста, укажите числа и символ необходимой операции:

1 (+) — Сложение
2 (-) — Вычитание
3 (*) — Умножение
4 (/) — Деление
5 (^) — Возведение в степень
6 (K) — Квадратный корень
7 (//) — Цельное деление
8.1 (%?) — Вычисление, сколько процентов составляет a от b
8.2 (%+) — Вычисление, чему равно a + b% a
8.3 (%-) — Вычисление, чему равно a - b% a
9 (окр+) — Округление а в большую сторону
10 (окр-) — Округление а в меньшую сторону
''')

# Контейнеры функциональности
check = bool(False)
s = str()

def wait():
      print('Выполнение операции, пожалуйста, подождите...')
      time.sleep(1)

def border():
        print('''
-----
''')

def reset():
        border()
        print('Сброс сессии...')
        border()

#Первоначальное ожидание
time.sleep(2)
print('''
Инициализация...
''')
time.sleep(3)

# Запуск первого бесконечного цикла работы
x = int(0)
while x <= 1:
        
# Запрос исходных данных
    if check == True:
        print('Введите 0 в стрoку ниже для принудительного сброса сессии')
        b = float(input('Пожалуйста, введите второе число: '))
        if b == 0:
            reset()
            a = 0
            a = float(input('Пожалуйста, введите первое число: '))
            s = str(input('Пожалуйста, введите код необходимой функции: '))
            b = float(input('Пожалуйста, введите второе число: '))
        else:
            s = str(input('Пожалуйста, введите код необходимой функции: '))
    else:
        a = float(input('Пожалуйста, введите первое число: '))
        s = str(input('Пожалуйста, введите код необходимой функции: '))
        b = float(input('Пожалуйста, введите второе число: '))
        
#Задаём функциональность и осуществляем выполнение операции
    r = float()
    if s == '+':
        print('Задана функция: сложение.')
     # Ожидание при выполнении операции
        wait()
        r = (a + b)
        print('Результат: ', r)
    else:
        if s == '-':
            print('Задана функция: вычитание.')
            wait()
            r = (a - b)
            print('Результат: ', r)
        else:
            if s == '*':
                print('Задана функция: умножение')
                wait()
                r = (a * b)
                print('Результат: ', r)
            else:
                if s == '/':
                    print('Задана функция: деление')
                    wait()
                    r = (a / b)
                    print('Результат: ', r)
                else:
                    if s == '^':
                        print('Задана функция: возведение a в степень b')
                        wait()
                        r = (math.pow(a, b))
                        print('Результат: ', r)
                    else:
                        if s == 'K':
                            print('Задана функция: корень числа a')
                            print('Внимание! При выполнении этой функции число b не учитывается.')
                            wait()
                            r = (math.sqrt(a))
                            print('Результат: ', r)
                        else:
                            if s == '//':
                                print('Задана функция: цельное деление')
                                wait()
                                r = (a // b)
                                print('Результат: ', r)
                            else:
                                if s == '%?':
                                    print('Задана функция: вычисление, сколько процентов составляет a от b')
                                    wait()
                                    r = ((a / b) * 100)
                                    print('Результат: ', r)
                                else:
                                    if s == '%+':
                                        print('Задана функция: вычисление, чему равно a + b% a')
                                        wait()
                                        r = a + (a * (b / 100))
                                        print('Результат: ', r)
                                    else:
                                        if s == '%-':
                                            print('Задана функция: вычисление, чему равно a - b% a')
                                            wait()
                                            r = a - (a * (b /100))
                                            print('Результат: ', r)
                                        else:
                                            if s == 'окр+':
                                                print('Задана функция: округление а в большую сторону')
                                                print('Внимание! При выполнении этой функции число b не учитывается.')
                                                wait()
                                                r = math.ceil(a)
                                                print('Результат: ', r)
                                            else:
                                                if s == 'окр-':
                                                    print('Задана функция: округление а в меньшую сторону')
                                                    print('Внимание! При выполнении этой функции число b не учитывается.')
                                                    wait()
                                                    r = math.floor(a)
                                                    print('Результат: ', r)

#Сохранить или удалить?
    sod = str(input('''Вы можете сохранить результат этой операции для продолжения действий с ним, не сохранять
или завершить работу калькулятора.
Y — сохранение, N — сброс калькулятор. Ваш выбор: '''))
        #Пользователь продолжает сессию калькулятора
    if sod == ('Y' or 'y' or 'У' or 'у'):
            a = r
            check = True
            continue
    else:
        reset()
        continue