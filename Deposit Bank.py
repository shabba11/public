money = input("Введите сумму средств для депозита в банке:")
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent['ТКБ'] = 1.056 * float(money) - float(money)
per_cent['СКБ'] = 1.059 * float(money) - float(money)
per_cent['ВТБ'] = 1.0428 * float(money) - float(money)
per_cent['СБЕР'] = 1.04 * float(money) - float(money)
print(per_cent)
i = max(per_cent['ТКБ'], per_cent['СКБ'], per_cent['ВТБ'], per_cent['СБЕР'])
print("Максимальная сумма, которую вы можете заработать —", i)
