import tkinter as tk
import random

def roll_dice():
    num_dice = int(dice_entry.get())
    result = []
    for _ in range(num_dice):
        dice_value = random.randint(1, 6)
        result.append(dice_value)
    result_label.config(text="Zar Atış Sonucu: " + " ".join(str(val) for val in result))

# Create the GUI window
window = tk.Tk()
window.title("Zar Atma Uygulaması")

# Create label and entry for dice count
dice_label = tk.Label(window, text="Zar Sayısı:")
dice_label.pack()

dice_entry = tk.Entry(window)
dice_entry.pack()

# Create roll dice button
roll_button = tk.Button(window, text="Zarları At", command=roll_dice)
roll_button.pack()

# Create label to display result
result_label = tk.Label(window, text="Zar Atış Sonucu:")
result_label.pack()

# Start the main event loop
window.mainloop()
