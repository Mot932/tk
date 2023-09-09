import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Конвертер валют")

# Фиксированные курсы обмена валют
rub_to_usd_rate = 0.013  # 1 рубль = 0.013 доллара
rub_to_eur_rate = 0.011  # 1 рубль = 0.011 евро
rub_to_cny_rate = 0.086  # 1 рубль = 0.086 юаня

# Создаем функцию для конвертации валют
def convert_currency():
    try:
        amount = float(entry_amount.get())
        usd_result = amount * rub_to_usd_rate
        eur_result = amount * rub_to_eur_rate
        cny_result = amount * rub_to_cny_rate

        result_label.config(text=f"{amount} RUB = {usd_result:.2f} USD, {eur_result:.2f} EUR, {cny_result:.2f} CNY")
    except ValueError:
        result_label.config(text="Введите корректное число")

# Создаем метки и поля для ввода
label_amount = tk.Label(root, text="Сумма в RUB:", font=("Impact", 19))
entry_amount = tk.Entry(root, font=("Impact", 18))

# Создаем кнопку для конвертации
convert_button = tk.Button(root, text="Конвертировать", font=("Impact", 17), background="#DAA520", command=convert_currency)

# Метка для вывода результата
result_label = tk.Label(root, text="Результат здесь", font=("Impact", 17))

# Размещаем элементы на экране
label_amount.pack(anchor="nw", padx=6, pady=6)
entry_amount.pack(anchor="nw", padx=6, pady=6)
convert_button.pack(anchor="nw", padx=6, pady=6)
result_label.pack(anchor="nw", padx=6, pady=6)

# Запускаем главный цикл программы
root.mainloop()
