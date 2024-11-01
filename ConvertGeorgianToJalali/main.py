from datetime import datetime
from tkinter import StringVar
import jdatetime

import ttkbootstrap as ttk


def update_label(sv):
    selected_date = sv.get()
    if selected_date == "":
        return
    date_object = datetime.strptime(selected_date, "%y/%m/%d")
    formated_date = date_object.strftime("%A, %b %d")
    year=date_object.strftime("%y")
    month=date_object.strftime("%m")
    day=date_object.strftime("%d")
    jalili = jdatetime.datetime.fromgregorian(day=int(day), month=int(month), year=int('20'+year), hour=None, minute=None, second=None)
    lable_jalali.config(text=jalili)
    lable_jalali.grid(row=2,column=0,padx=10)
    label.config(text=f"{formated_date}")

root = ttk.Window(title="Convert Georgian to Jalali date")
root.geometry("400x200")

# Label
label = ttk.Label(root, text="Today")
lable_jalali=ttk.Label(root,text="")
lable_jalali.grid(row=0,column=0)
# DateEntry
cal = ttk.DateEntry(root, bootstyle="primary")
cal.grid(row=0,column=0,pady=20,padx=30)

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: update_label(sv))
cal.entry.configure(textvariable=sv)
root.mainloop()
