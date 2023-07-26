from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
from datetime import date

root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("exam/taskninja")
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
def das():
    root.destroy()
    import dashboard
def user():
    root.destroy()
    import setting 
    
def submit():
    days_in_month=30
    days_day_num=int(today.strftime("%d"))
    count= Label(root,text=f" Today is: {days_day_num} of month",font=("Inter", 15, "bold"))
    count.pack(pady=20)
    day_left = days_in_month-days_day_num+int(days_exam.get())
    count= Label(root,text=f"days left is: {day_left}",font=("Inter", 15, "bold"))
    count.pack(pady=20)
    

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
billing=Button(text='Exam',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=quiz)
billing.place(x=1,y=310)
setting=Button(text='User Setting',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=user)
setting.place(x=1,y=380)

panic=Label(root,text="DON'T PANIC !",font=("Inter", 20, "bold"),bg="grey",border=21)
panic.pack(pady=20,ipadx=10,ipady=10)


today= date.today()
f_today=today.strftime("%A - %B %d,%Y")
today_lavel=Label(root,text=f"Today is: {f_today}",font=("Inter", 15, "bold"))
today_lavel.pack(pady=20)

days_exam=Entry(root,width=25,font=("Inter", 12, "bold"))
days_exam.place(x=200,y=250)
Button(root,text="Submit",font=("Inter", 15, "bold"),command=submit).place(x=200,y=290)




root.mainloop()