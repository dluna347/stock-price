import yfinance as yf
import tkinter as tk
from tkinter import ttk

def get_stock_price(event=None):
    STK = stock_entry.get()
    ticker = yf.Ticker(STK)
    data = ticker.history(period="1d")
    last_price = data["Close"].iloc[-1]
    result_label.config(text=f"The last market price of {STK} is {last_price}")

# Create the main window
window = tk.Tk()
window.title("Stock Price Checker")

# Create and pack the widgets
stock_label = ttk.Label(window, text="Enter the name of the share:")
stock_label.pack()

stock_entry = ttk.Entry(window)
stock_entry.pack()
stock_entry.bind("<Return>", get_stock_price)  # Bind the Enter key to the entry field

check_button = ttk.Button(window, text="Check Price", command=get_stock_price)
check_button.pack()

result_label = ttk.Label(window, text="")
result_label.pack()

# Set focus to the entry field
stock_entry.focus()

# Run the main loop
window.mainloop()