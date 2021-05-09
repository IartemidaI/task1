import requests
r= requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
r=r.json()
f1 = open('currency.txt','w',encoding="UTF-8")
for i in r:
    data=["Валюта: ",i["ccy"],
        "\n\tКупівля:", i["buy"],
        "\n\tПродаж", i["sale"], "\n"]
    data="".join(data)
    f1.write(data)
f1.close()
