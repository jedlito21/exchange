import requests
import json

#api to my file
api = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=187cb0fb71a43cf71f6c1e9acc70d216')
data = api.json()
test = data["rates"]
api = str(api)

if api == "<Response [200]>":
    with open('venv/currencies.json', 'w') as outfile:
        json.dump(test, outfile)


#from file to program
#with open("currencies.json", "r") as file:


#print(api)
print("List měn možných k výměně: ")
print('\n'.join("{}".format(k) for k, v in test.items()))

first_currency = input("Vyber svou první měnu: ")
second_currency = input("Vyber svou druhou měnu: ")
money = float(input("Kolik si chcete vyměnit?: "))

to_eur = test[str(first_currency)]
to_curr = test[str(second_currency)]
math = money / to_eur * to_curr

print("Za",money, first_currency, "budete mít", math, second_currency)