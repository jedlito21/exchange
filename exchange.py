import requests
import json
from tkinter import *
from tkinter import ttk, messagebox
import os
import tkinter.font

#api to my file
api = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=187cb0fb71a43cf71f6c1e9acc70d216')
data = api.json()
test = data["rates"]
api_response = str(api)

def save_to_json(data):
    if os.path.exists('currencies.json'):
        with open('currencies.json', 'r') as file:
            currencies_data = json.load(file)
    else:
        currencies_data = {}

    currencies_data.update(data)

    with open('currencies.json', 'w') as file:
        json.dump(currencies_data, file, indent=2)

if api_response == "<Response [200]>":
            save_to_json(test)

def load_from_json():
    if os.path.exists('currencies.json'):
        with open('currencies.json', 'r') as file:
            currencies_data = json.load(file)
        return currencies_data
    else:
        return {}

json_data = load_from_json()
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
        result_label.config(text=f"Za: {round(money, 2)} {first_currency} \n Budete mít: {round(math, 2)} {second_currency}",padx=10, pady=10)
    except ValueError:
        result_label.config(text="Zadej platné číslo.", pady=10)

#listing currencies
currencies = []
for index, (key, value) in enumerate(json_data.items()):
    currencies.append(key)

#tkinter
win = Tk()
win.geometry("300x300")
win.minsize(300, 300)
win.title("Exchanger")
win.configure(bg="#262626")

style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12),
                padding=10,
                background="#262626",
                foreground="#262626"
                )

style.configure("TCombobox",
                font=("Arial", 12),
                padding=10,
                selectbackground="#2880BA",
                foreground="#262626"
                )
custom_font = tkinter.font.Font( family = "Arial", size = 12, weight = "bold")

options = StringVar(win)
options.set("")

options2 = StringVar(win)
options2.set("")

text1 = Label(win, text='Vybete vaši měnu', width=15, bg="#262626", fg="white", font=custom_font)
text1.pack()

om1 = ttk.Combobox(win, textvariable=options, values=currencies)
om1.set(currencies[0])
om1.pack()

text2 = Label(win, text='Vybete měnu do které chcete \n vyměnit peníze', width=40, bg="#262626", fg="white", font=custom_font)
text2.pack()

om2 = ttk.Combobox(win, textvariable=options2, values=currencies)
om2.set(currencies[1])
om2.pack()

cislo = Entry(win, width=20)
cislo.pack(pady=10)

potvrdit = ttk.Button(win, text="Potvrdit", command=number)
potvrdit.pack()

result_label = Label(win, text="", width=30, bg="#262626", fg="red", font=custom_font)
result_label.pack()


win.bind('<Return>', on_enter_press)

win.mainloop()