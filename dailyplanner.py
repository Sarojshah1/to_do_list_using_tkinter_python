from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("daily planner/taskninja")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400","300")
root.state("zoomed")

def das():
    root.destroy()
    import dashboard
def cal():
    root.destroy()
    import ca
    
def quiz():
    root.destroy()
    import quiz
def user():
    root.destroy()
    import setting 
def exam():
    root.destroy()
    import exam

frame=Frame(width=160,padx=30,bg='black')
frame.pack(side=LEFT,fill=Y)
dash=Button(text='Dashboard',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=das)
dash.place(x=1,y=30)
medicine=Button(text='Daily planner',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2')
medicine.place(x=1,y=100)
category=Button(text='Calendar',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=cal)
category.place(x=1,y=170)
billing=Button(text='Quiz',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=quiz)
billing.place(x=1,y=240)
analytic=Button(text='Exam',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=exam)
analytic.place(x=1,y=310)
setting=Button(text='User Setting',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=user)
setting.place(x=1,y=380)

todo=Frame(root, width=300,height=500,bg="white")
todo.place(x=200,y=40)
heading=Label(todo,text='TO-DO',bg='#FAFAFA',fg='black',font=("camb",20,'bold'))
heading.place(x=100,y=5)
todo1=Frame(todo, width=500,bg="black")
todo1.place(x=1,y=40)
list1=Listbox(todo,font=("Inter", 12, "bold"),width=300,height=500,bg="red",bd=0,fg="black")
list1.place(x=0,y=45)

try:
            con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='taskninja')
            mycursor=con.cursor()
except:
            messagebox.showerror("error","connection error")
query='select * from todo'
mycursor.execute(query)
row=mycursor.fetchall()
x=1
for i in row:
    b=list(i)
    list1.insert(END,f"{b[1]}")
    


doing=Frame(root, width=300,height=500,bg="white")
doing.place(x=600,y=40)
heading1=Label(doing,text='DOING',bg='#FAFAFA',fg='black',font=("camb",20,'bold'))
heading1.place(x=100,y=5)
doing1=Frame(doing, width=500,bg="black")
doing1.place(x=1,y=40)
list2=Listbox(doing,font=("Inter", 12, "bold"),width=300,height=500,bg="yellow",bd=0,fg="black")
list2.place(x=0,y=45)
for i in row:
    b=list(i)
    list2.insert(END,f"{b[2]}")

done=Frame(root, width=300,height=500,bg="white")
done.place(x=960,y=40)
heading2=Label(done,text='DONE',bg='#FAFAFA',fg='black',font=("camb",20,'bold'))
heading2.place(x=100,y=5)
done1=Frame(done, width=500,bg="black")
done1.place(x=1,y=40)
list3=Listbox(done,font=("Inter", 12, "bold"),width=300,height=500,bg="green",bd=0,fg="black")
list3.place(x=0,y=45)

for i in row:
    b=list(i)
    list3.insert(END,f"{b[3]}")

root.mainloop()