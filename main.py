print('Таблица умножения')

for i in range(1, 10):
    for k in range(2, 10):
        print(f'{i} * {k} = {i * k}\t\t', end=' ')
    print('')
    print('')
else:
    print('Well done')