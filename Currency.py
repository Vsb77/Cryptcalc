import requests
import json
import pandas as pd
from colorama import init, Fore
init(autoreset=True)
df_orders = pd.read_excel('valuesk.xlsx')
tc = input(Fore.BLUE + "Введите валюту отображения(USD,RUB и тд.)_")
if tc != df_orders.iloc[0,4]:
    print(Fore.RED + "Внимание! Выбранная валюта отображения отличается от указанной в документе Excel, расчет прибыли может быть неверный!")
count = 0
def func(currency, tc, values, priced):
    response = requests.get(f'https://api.coinbase.com/v2/prices/{currency}-{tc}/spot')
    try:
        BTC = response.json()
        currency = BTC['data'] ['base']
        price = BTC['data'] ['amount']
        global count
        count += round(float(price) * values,2)
        return f"Криптовалюта: {currency}  |  Цена: {round(float(price),2)} {tc}  |  В активе: {round(float(price)*values, 2)} {tc}  |  Прибыль: {round(((float(price) - float(priced))/float(priced))*100,2)}%"
    except KeyError:
        return Fore.RED + f"Возникла ошибка! курс {currency} к {tc} не найден."

lines = df_orders.shape[0]
count2 = 0
a = 0
while lines > 0:
    print(func(df_orders.iloc[a, 0], tc, df_orders.iloc[a, 1], df_orders.iloc[a, 2]))
    count2 += df_orders.iloc[a, 2]*df_orders.iloc[a, 1]
    a +=1
    lines = lines - 1
print(Fore.MAGENTA + f'Стоимость всех автивов: {round(count, 2)} {tc} Вложено: {round(count2, 2)} {tc} Прибыль: {round(((float(count) - float(count2))/float(count2))*100,2)}%')

















