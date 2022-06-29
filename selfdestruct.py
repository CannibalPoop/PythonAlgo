n = int(input())
i = 2
print(n/i)
answer = input()
while answer != 'Угадал':
    i += i
    if answer == 'Мало':
        n += n // i
        print(n)
    else:
        n -= n // i
        print(n)
    answer = input()
print('Загаданное число = ', n)