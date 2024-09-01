import tkinter as tk
from tkinter import ttk, colorchooser

# List to store the history of calculations
history = []

def calculate_marketcap_change():
    try:
        coin_name = coin_name_entry.get() if coin_name_entry.get() else "Unnamed Coin"
        current_marketcap = float(current_marketcap_entry.get()) * (1000 if current_marketcap_units_button.cget("text") == "K" else 1000000)
        future_marketcap = float(future_marketcap_entry.get()) * (1000 if future_marketcap_units_button.cget("text") == "K" else 1000000)
        investment_amount = float(investment_entry.get())

        percentage_change = (future_marketcap - current_marketcap) / current_marketcap * 100
        future_investment_value = (investment_amount / current_marketcap) * future_marketcap

        
        history.append({
            "coin_name": coin_name,
            "current_marketcap": current_marketcap,
            "future_marketcap": future_marketcap,
            "investment_amount": investment_amount,
            "percentage_change": percentage_change,
            "future_investment_value": future_investment_value
        })

        result_label.config(text=f"Percentage change: {percentage_change:.2f}%\nFuture investment value: ${future_investment_value:.2f}", foreground=get_color_from_percentage(percentage_change))
        history_listbox.insert(tk.END, f"{coin_name} | Current Marketcap: ${current_marketcap:.2f} | Future Marketcap: ${future_marketcap:.2f} | Percentage Change: {percentage_change:.2f}% | Future Investment Value: ${future_investment_value:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.", foreground="red")

def show_history(*args):
    selection = history_listbox.curselection()
    if selection:
        index = selection[0]
        calculation = history[index]
        result_label.config(text=f"Coin: {calculation['coin_name']}\nCurrent Marketcap: ${calculation['current_marketcap']:.2f}\nFuture Marketcap: ${calculation['future_marketcap']:.2f}\nPercentage Change: {calculation['percentage_change']:.2f}%\nFuture Investment Value: ${calculation['future_investment_value']:.2f}", foreground=get_color_from_percentage(calculation['percentage_change']))

def toggle_units(button, entry):
    if button.cget("text") == "K":
        button.config(text="M")
    else:
        button.config(text="K")
    update_marketcap_values(entry)

def update_marketcap_values(entry):
    try:
        value = float(entry.get())
        if entry == current_marketcap_entry and current_marketcap_units_button.cget("text") == "K":
            entry.delete(0, tk.END)
            entry.insert(0, str(value / 1000))
        elif entry == future_marketcap_entry and future_marketcap_units_button.cget("text") == "K":
            entry.delete(0, tk.END)
            entry.insert(0, str(value / 1000))
    except ValueError:
        pass

def get_color_from_percentage(percentage):
    if percentage > 0:
        return "green"
    elif percentage < 0:
        return "red"
    else:
        return "black"

root = tk.Tk()
root.title("Marketcap Calculator")

# Create the GUI elements
coin_name_label = ttk.Label(root, text="Coin Name:")
coin_name_entry = ttk.Entry(root)

current_marketcap_label = ttk.Label(root, text="Current Marketcap:")
current_marketcap_entry = ttk.Entry(root)
current_marketcap_units_button = ttk.Button(root, text="K", command=lambda: toggle_units(current_marketcap_units_button, current_marketcap_entry), width=5)

future_marketcap_label = ttk.Label(root, text="Future Marketcap:")
future_marketcap_entry = ttk.Entry(root)
future_marketcap_units_button = ttk.Button(root, text="K", command=lambda: toggle_units(future_marketcap_units_button, future_marketcap_entry), width=5)

investment_label = ttk.Label(root, text="Investment Amount:")
investment_entry = ttk.Entry(root)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_marketcap_change, style="Accent.TButton")

result_label = ttk.Label(root, text="", font=("Arial", 16), foreground="black")

history_label = ttk.Label(root, text="Calculation History:")
history_listbox = tk.Listbox(root, width=40, height=10)
history_listbox.bind("<<ListboxSelect>>", show_history)

# Styling
style = ttk.Style(root)
style.theme_use("default")
style.configure("Accent.TButton", background="green", foreground="white", font=("Arial", 12, "bold"))

# GUI elements
coin_name_label.grid(row=0, column=0, padx=10, pady=10)
coin_name_entry.grid(row=0, column=1, padx=10, pady=10)

current_marketcap_label.grid(row=1, column=0, padx=10, pady=10)
current_marketcap_entry.grid(row=1, column=1, padx=10, pady=10)
current_marketcap_units_button.grid(row=1, column=2, padx=10, pady=10)

future_marketcap_label.grid(row=2, column=0, padx=10, pady=10)
future_marketcap_entry.grid(row=2, column=1, padx=10, pady=10)
future_marketcap_units_button.grid(row=2, column=2, padx=10, pady=10)

investment_label.grid(row=3, column=0, padx=10, pady=10)
investment_entry.grid(row=3, column=1, padx=10, pady=10)

calculate_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

result_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

history_label.grid(row=0, column=3, padx=10, pady=10)
history_listbox.grid(row=1, column=3, rowspan=5, padx=10, pady=10)

root.mainloop()
