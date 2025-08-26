import tkinter 
import random
from tkinter import messagebox

#root window
root=tkinter.Tk()

#root settings
root.configure(bg="white")
root.title("TO DO List")
root.geometry("325x275")


tasks=[]

#testing purposes for a default list
tasks=["buy earphones","buy cooling pad","buy wire"]

#functions

def update_listbox():
    clear_listbox()

    # to add at end
    for task in tasks:
        ib_tasks.insert("end",task)

def clear_listbox():
    ib_tasks.delete(0,"end")

def add_task():
    #get task to add
    task=txt_input.get()
    # not empty
    if task!="":
        tasks.append(task)
        update_listbox()
    else:
        title["text"]="enter the task"
    txt_input.delete(0,end="")

def delete_all():
    confirmed=messagebox.askyesno("please confirm ", "Do you really waqnt to delete ")

    if confirmed==True:
        global tasks
        tasks=[]
        update_listbox()

def delete_one():
    task=ib_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_random():
   ele=random.choice(tasks)
   title["text"]=ele
    
def number_of_task():
    number_of_tasks=len(tasks)
    msg="Number of Tasks : ",number_of_tasks
    title["text"]=msg

def quit():
    root.destroy()

title=tkinter.Label(root,text="To Do List",bg="white")
title.grid(row=0,column=0)

txt_input=tkinter.Entry(root,width=15)
txt_input.grid(row=1,column=1)

btn_add_task=tkinter.Button(root,text="Add Task",fg="Black", bg="white",command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all=tkinter.Button(root,text="delete all",fg="Black", bg="white",command=delete_all)
btn_del_all.grid(row=2,column=0)


btn_del_one=tkinter.Button(root,text="delete ",fg="Black", bg="white",command=delete_one)
btn_del_one.grid(row=3,column=0)


btn_sort_asc=tkinter.Button(root,text="Ascending",fg="Black", bg="white",command=sort_asc)
btn_sort_asc.grid(row=4,column=0)


btn_sort_desc=tkinter.Button(root,text="Dscending",fg="Black", bg="white",command=sort_desc)
btn_sort_desc.grid(row=5,column=0)


btn_choose_random=tkinter.Button(root,text="choose Random",fg="Black", bg="white",command=choose_random)
btn_choose_random.grid(row=6,column=0)

btn_number_of_task=tkinter.Button(root,text="number of task",fg="Black", bg="white",command=number_of_task)
btn_number_of_task.grid(row=7,column=0)


btn_quit=tkinter.Button(root,text="Quit",fg="Black", bg="white",command=quit)
btn_quit.grid(row=8,column=0)

ib_tasks=tkinter.Listbox(root)
ib_tasks.grid(row=2,column=1,rowspan=7)
update_listbox()

root.mainloop()