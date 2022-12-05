import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# root window
root = tk.Tk()
root.title('Position Calculator 📈')
root.geometry('325x150')
root.resizable(False, False)

# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# Portfolio label
pf_label = ttk.Label(frame, text='Portfolio $')
pf_label.grid(column=0, row=0, sticky='W', **options)

#Portfolio entry
pf = tk.StringVar()
pf_entry = ttk.Entry(frame, textvariable=pf)
pf_entry.grid(column=1, row=0, **options)
pf_entry.insert('1','100')
pf_entry.focus()

# Risk label
r_label = ttk.Label(frame, text='Risk %')
r_label.grid(column=0, row=1, sticky='W', **options)

# Risk entry
r = tk.StringVar()
r_entry = ttk.Entry(frame, textvariable=r)
r_entry.grid(column=1, row=1, **options)
r_entry.insert('1','1')
r_entry.focus()

# Drawdown label
draw_label = ttk.Label(frame, text='Drawdown %')
draw_label.grid(column=0, row=2, sticky='W', **options)

#Drawdown entry
draw = tk.StringVar()
draw_entry = ttk.Entry(frame, textvariable=draw)
draw_entry.grid(column=1, row=2, **options)
draw_entry.focus()

# calculate button
def calculate_button_clicked(event=None):
    try:
        portfolio = float(pf.get())
        risk = float(r.get())
        drawdown = float(draw.get())
        calculate = round(((risk/100)*portfolio)/(drawdown/100),2)
        result = f'Portfolio = {portfolio} Position size = {calculate} USD'
        result_label.config(text=(result),foreground="Dark Green",font=('Roboto', 10, 'bold'))
    except ValueError as error:
        showerror(title='Error', message=error)

# button settings
calculate_button = ttk.Button(frame, text='calculate')
calculate_button.grid(column=2, row=1, sticky='W', **options)
calculate_button.configure(command=calculate_button_clicked)

# bind enter key calculate
root.bind('<Return>', calculate_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=4, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()