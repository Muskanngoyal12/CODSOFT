from tkinter import Button, Entry, Label, Tk, Listbox
import tkinter as tk
from tkinter import messagebox

screen = Tk()
screen.title("List")
screen.geometry('600x400')
screen.configure(background ="pink")

text=Label(screen, text="To - Do List")
text.configure(font =("calibiri", 50))
text.configure(background ="light green", foreground="red",width=30)
text.pack()
text.place(x=200, y=10)

Tasks=[]

def Add_task():
        task = Task.get()
        if task:
            Tasks.append(task)
            Task_listbox.insert(tk.END, task)
            Task.delete(0,"end")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

def Delete_task():
        selection = Task_listbox.curselection()
        if selection:
            index = selection[0]
            del Tasks[index]
            Task_listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def Update_task():
        selection = Task_listbox.curselection()
        if selection:
            index = selection[0]
            new_task = Task.get()
            if new_task:
                Tasks[index] = new_task
                Task_listbox.delete(index)
                Task_listbox.insert(index, new_task)
                Task.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

def Tasklistbox():
        for task in Tasks:
            Tasklistbox.insert(tk.END, task)



Task=Entry(screen, font=('calibiri', 18, 'normal'), width= 35)
Task.pack()
Task.place(x=550, y=120)

Task_listbox = Listbox( height= 20, width=50)
Task_listbox.pack()
Task_listbox.place(x=600, y=250)

Add_button = Button( text="ADD TASK", width= 25, height=2, font=('calibiri', 15), fg= 'white', background='black', command=Add_task)
Add_button.pack()
Add_button.place(x=100, y=200)

Delete_button = Button( text="DELETE TASK", width= 25, height=2, font=('calibiri', 15), fg= 'white', background='black', command=Delete_task)
Delete_button.pack()
Delete_button.place(x=100, y=300)

Update_button = Button( text="UPDATE TASK", width= 25, height=2, font=('calibiri', 15), fg= 'white', background='black', command=Update_task)
Update_button.pack()
Update_button.place(x=100, y=400)

Tasklistbox()

screen.mainloop()
