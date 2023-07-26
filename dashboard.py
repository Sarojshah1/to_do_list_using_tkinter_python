from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox

root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("dashboard/taskninja")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400","300")
root.state("zoomed")

def planner():
    root.destroy()
    import dailyplanner
def cal():
    root.destroy()
    import ca
def quiz():
    root.destroy()
    import quiz
def exam():
    root.destroy()
    import exam
def das():
    root.destroy()
    import dashboard

def add():
    try:
        con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='taskninja')
        mycursor=con.cursor()
    except:
        messagebox.showerror("error","connection error!please add your medicine again")
                    

    vals={ 
                        "todo":todo.get(), 
                        "doing":todo1.get(),
                        "done":todo2.get()
                            }
    insert_query="""INSERT INTO todo(  todo, doing,done) VALUES(  %s,%s,%s)""",( vals['todo'],vals['doing'],vals['done'])
    mycursor.execute(*insert_query)
    con.commit()
    mycursor.close()
    con.close()
    todo.delete(0,'end')
    todo1.delete(0,'end')
    todo2.delete(0,'end')
   
    
def delete():
    try:
        con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='taskninja')
        mycursor=con.cursor()
    except:
        messagebox.showerror("error","connection error!please add your medicine again")
                    

    vals={ 
                        "todo":dele.get(), 

                            }
    delete_query="DELETE FROM todo WHERE todo=%s"
    mycursor.execute(delete_query,(dele.get(),))
    con.commit()
    mycursor.close()
    con.close()
    todo.delete(0,'end')
    todo1.delete(0,'end')
    todo2.delete(0,'end')
    

        


frame=Frame(width=160,padx=30,bg='black')
frame.pack(side=LEFT,fill=Y)
dash=Button(text='Dashboard',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=das)
dash.place(x=1,y=30)
medicine=Button(text='Daily planner',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=planner)
medicine.place(x=1,y=100)
category=Button(text='Calendar',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=cal)
category.place(x=1,y=170)
billing=Button(text='Quiz',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=quiz)
billing.place(x=1,y=240)
billing=Button(text='Exam',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=exam)
billing.place(x=1,y=310)
setting=Button(text='User Setting',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2')
setting.place(x=1,y=380)

frame1=Frame(root,width=950,height=370,bg="#fafafa")
frame1.place(x=250,y=270)
list1=Listbox(frame1,font=("Inter", 12, "bold"),width=100,height=15,bg="RED",bd=0,fg="black")
list1.place(x=10,y=50)
heading2=Label(root,text='DASHBOARD',bg='#FAFAFA',fg='black',font=("camb",20,'bold'))
heading2.place(x=600,y=5)
heading2=Label(frame1,text='ADD TO-DO LIST',bg='#FAFAFA',fg='black',font=("camb",15,'bold'))
heading2.place(x=300,y=5)

heading2=Label(root,text='TO-DO ',bg='#FAFAFA',fg='black',font=("camb",9,'bold'))
heading2.place(x=300,y=50)
todo=Entry(root,width=45,font=("Inter", 12, "bold"))
todo.place(x=300,y=70,height=30)


heading3=Label(root,text='ADD doing ',bg='#FAFAFA',fg='black',font=("camb",9,'bold'))
heading3.place(x=300,y=110)
todo1=Entry(root,width=45,font=("Inter", 12, "bold"))
todo1.place(x=300,y=130,height=30)

heading4=Label(root,text='ADD done',bg='#FAFAFA',fg='black',font=("camb",9,'bold'))
heading4.place(x=300,y=165)
todo2=Entry(root,width=45,font=("Inter", 12, "bold"))
todo2.place(x=300,y=185,height=30)
Button(root,text="ADD to-do",width=10,height=1,bg="blue",font=("Inter", 12, "bold"),border=2,command=add).place(x=300,y=220)
Button(root,text="delete todo",width=10,height=1,bg="red",font=("Inter", 12, "bold"),border=2,command=delete).place(x=900,y=110)


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
    
dele=Entry(root,width=30,font=("Inter", 12, "bold"))
dele.place(x=900,y=70,height=30)


root.mainloop()