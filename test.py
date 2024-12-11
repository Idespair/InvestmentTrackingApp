import tkinter as tk
from Stock import query_stock
from tkinter import messagebox

def get_stock_price():
    stock = entry.get().strip()
    if stock:
        try:
            result = query_stock(stock)
            label = tk.Label(text=f" {stock }  Price: {result}")
            label.pack()
        except AttributeError:
            messagebox.showwarning("No stock could be found", "No stock could be found.")

root = tk.Tk()
root.title("Test")

#User types a stock name
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

#Button that executes the script
button = tk.Button(root, text="Submit", command=get_stock_price)
button.pack(pady=20)
root.bind('<Return>', lambda event: get_stock_price())

root.mainloop()