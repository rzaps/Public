import tkinter as tk



def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)


def mark_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task = task_list.get(selected_task_index)
        ready_task_list.insert(tk.END, selected_task)
        task_list.delete(selected_task_index)


root = tk.Tk()
root.title("Task")
root.configure(background="antique white")

title_input = tk.Label(root, text="Введите задачу", bg="antique white")
title_input.pack()

task_entry = tk.Entry(root, width=56, bg="white", fg="tan4")
task_entry.pack()

#Кнопки
button_frame = tk.Frame(root, bg="antique white")
button_frame.pack(pady=16)

add_task_button = tk.Button(button_frame, text="Добавить задачу", bg="tan4",
                            fg="white", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=8)

delete_task_button = tk.Button(button_frame, text="Удалить задачу", bg="IndianRed4",
                            fg="white", command=delete_task)
delete_task_button.pack(side=tk.LEFT, padx=8)

mark_button = tk.Button(button_frame, text="Задача выполнена", bg="dark olive green",
                            fg="white", command=mark_task)
mark_button.pack(side=tk.LEFT, padx=8)

#Списки
list_frame = tk.Frame(root, bg="antique white")
list_frame.pack()

task_list_frame = tk.Frame(list_frame, bg="antique white")
task_list_frame.pack(side=tk.LEFT, padx=16)

ready_task_list_frame = tk.Frame(list_frame, bg="antique white")
ready_task_list_frame.pack(side=tk.LEFT, padx=16)

title_list = tk.Label(task_list_frame, text="Список задач", bg="antique white")
title_list.pack()

task_list = tk.Listbox(task_list_frame, height=15, width=30, bg="wheat3")
task_list.pack()

title_ready_list = tk.Label(ready_task_list_frame, text="Выполненные задачи",
                            bg="antique white")
title_ready_list.pack()

ready_task_list = tk.Listbox(ready_task_list_frame, height=15, width=30,
                             bg="dark sea green")
ready_task_list.pack()


root.mainloop()