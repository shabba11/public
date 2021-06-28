tickets = int(input("Введите количество билетов: "))
price = 0

for human in range(tickets):
   age = int(input('Укажите возраст:'))
   if age < 18:
      price += 0
   elif 18 <= age <= 25:
      price += 990
   elif age > 25:
      price += 1390
if tickets > 3:
      price = price * 0.9
print("Сумма к оплате: ", price)

