import tkinter as tk
from time import strftime

# Create the window
root = tk.Tk()
root.title("Digital Clock")

# Define the clock update function
def time():
    current_time = strftime('%H:%M:%S %p')  # Fetch the current time in Hour:Minute:Second AM/PM format
    label.config(text=current_time)  # Update the label with the current time
    label.after(1000, time)  # Update the time every second (1000 milliseconds)

# Create and configure the clock label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Start the clock
time()

# Run the window loop
root.mainloop()
