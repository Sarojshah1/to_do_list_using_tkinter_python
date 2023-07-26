import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        todo_list.insert(tk.END, task)
        entry.delete(0, tk.END)

def move_to_doing():
    selected_task = todo_list.curselection()
    task = todo_list.get(selected_task)
    todo_list.delete(selected_task)
    doing_list.insert(tk.END, task)

def move_to_done():
    selected_task = doing_list.curselection()
    task = doing_list.get(selected_task)
    doing_list.delete(selected_task)
    done_list.insert(tk.END, task)

root = tk.Tk()
root.title("Daily Planner")

# Create the frames
todo_frame = tk.Frame(root)
doing_frame = tk.Frame(root)
done_frame = tk.Frame(root)

# Create the labels
tk.Label(todo_frame, text="To Do", fg='black',bg='red').pack(side=tk.TOP)
tk.Label(doing_frame, text="Doing", fg='black',bg='yellow').pack(side=tk.TOP)
tk.Label(done_frame, text="Done", fg='black',bg='green').pack(side=tk.TOP)

# Create the lists
todo_list = tk.Listbox(todo_frame)
doing_list = tk.Listbox(doing_frame)
done_list = tk.Listbox(done_frame)

todo_list.pack(side=tk.LEFT)
doing_list.pack(side=tk.LEFT)
done_list.pack(side=tk.LEFT)

# Create the entry and buttons
entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

to_doing_button = tk.Button(root, text="Move to Doing", command=move_to_doing)
to_doing_button.pack()

to_done_button = tk.Button(root, text="Move to Done", command=move_to_done)
to_done_button.pack()

# Pack the frames
todo_frame.pack(side=tk.LEFT)
doing_frame.pack(side=tk.LEFT)
done_frame.pack(side=tk.LEFT)

root.mainloop()