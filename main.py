import tkinter as tk
import requests
from datetime import datetime

API = "https://api.sheety.co/952ea927b5ee42228ec81e7a704646d6/toye'sWorkouts/dailyhabits"

# Get the current date
today = datetime.now().strftime('%d/%m/%Y')

# Open the window, setting its characteristics
window = tk.Tk()
window.title('Daily Tasks')
window.minsize(width=300, height=200)

# Define Empty Variables
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()

# Creating The checklist
task_1 = tk.Checkbutton(window, text='Take my pills', variable=var1, onvalue=1, offvalue=0)
task_1.grid(column=1, row=1)
task_2 = tk.Checkbutton(window, text='Read 10 pages', variable=var2, onvalue=1, offvalue=0)
task_2.grid(column=1, row=2)
task_3 = tk.Checkbutton(window, text='Did I Smoke', variable=var3, onvalue=1, offvalue=0)
task_3.grid(column=1, row=3)
task_4 = tk.Checkbutton(window, text='Eat Needed Calories', variable=var4, onvalue=1, offvalue=0)
task_4.grid(column=1, row=4)
task_5 = tk.Entry(width=15)
task_5.grid(column=1, row=5)
task_5_label = tk.Label(text='Total Hours Slept')
task_5_label.grid(column=2, row=5)

# Define Submit function
def submitDaily():

    tk_1 = var1.get()
    tk_2 = var2.get()
    tk_3 = var3.get()
    tk_4 = var4.get()

    print(f'{tk_1}, {tk_2}, {tk_3}')

    sheet_input = {
        'dailyhabit': {
            'date': today,
            'pills': int(tk_1),
            'read': int(tk_2),
            'spark': int(tk_3),
            'eat': int(tk_4),
            'hours': int(task_5.get())
        }
    }

    sheet_response = requests.post(url=API, json=sheet_input)
    print(sheet_response.text)


# Submit Button
button = tk.Button(text='Submit', command=submitDaily)
button.grid(column=1, row=6)

window.mainloop()
