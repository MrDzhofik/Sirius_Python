def perevod(number, system, first, chislo=''):
    ostatok = number % system
    number //= system
    chislo += str(ostatok)
    if number != 0:
        perevod(number, system, chislo=chislo, first=first)
    else:
        print(f'{first}(10)={chislo[::-1]}({system})')


s = int(input('Система счисления: '))
n = int(input('Число: '))
perevod(number=n, system=s, first=n)
