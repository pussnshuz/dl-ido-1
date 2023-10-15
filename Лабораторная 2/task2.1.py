money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
Bankrupt = True
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while Bankrupt:
    months += 1
    money_capital += salary - spend
    if (money_capital + salary) < spend:
        Bankrupt = not Bankrupt
        break
    spend += spend * increase
print("Количество месяцев, которое можно протянуть без долгов:", months)
