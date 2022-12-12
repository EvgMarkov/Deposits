per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму депозита: "))

keys = list(per_cent)

def proc(key):
    return money * per_cent[key] / 100

deposit = list(map(proc, keys))

print(deposit)

max = max(deposit)

print("Максимальная сумма, которую вы можете заработать — ", max)