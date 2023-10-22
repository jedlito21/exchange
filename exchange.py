import requests
import json
from tkinter import *
from tkinter import messagebox

#api to my file
api = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=187cb0fb71a43cf71f6c1e9acc70d216')
data = api.json()
test = data["rates"]
api = str(api)

def on_enter_press(event):
    number()
def number(*args):
    try:
        first_currency = options.get()
        second_currency = options2.get()
        money = float(cislo.get())
        to_eur = test[first_currency]
        to_curr = test[second_currency]
        math = money / to_eur * to_curr
        messagebox.showinfo("Result", f"Za {round(money, 2)} {first_currency} budete mít {round(math, 2)} {second_currency}")
    except ValueError:
        messagebox.showerror("Chyba", "Zadej platné číslo.")


if api == "<Response [200]>":
    with open('venv/currencies.json', 'w') as outfile:
        json.dump(test, outfile)

#listing currencies
currencies = []
for index, (key, value) in enumerate(test.items()):
    currencies.append(key)

#tkinter
win = Tk()
win.geometry("300x200")
win.title("exchanger")

options = StringVar(win)
options.set("")

options2 = StringVar(win)
options2.set("")

text1 = Label(win,  text='Vybete vaši měnu', width=15)
text1.pack()

om1 = OptionMenu(win, options, *currencies)
om1.pack()

text2 = Label(win,  text='Vybete měnu do které chcete vyměnit peníze', width=40 )
text2.pack()

om2 = OptionMenu(win, options2, *currencies)
om2.pack()

cislo = Entry(win, width=20)
cislo.pack(pady=10)

potvrdit = Button(win, text="Potvrdit", command=number)
potvrdit.pack()

win.bind('<Return>', on_enter_press)

win.mainloop()