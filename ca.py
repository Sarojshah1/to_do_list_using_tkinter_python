from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkcalendar import Calendar
from tkinter import messagebox

root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("calender/taskninja")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400","300")
root.state("zoomed")

def das():
    root.destroy()
    import dashboard

def planner():
    root.destroy()
    import dailyplanner
def exam():
    root.destroy()
    import exam
def quiz():
    root.destroy()
    import quiz
def user():
    root.destroy()
    import setting 


frame=Frame(width=160,padx=30,bg='black')
frame.pack(side=LEFT,fill=Y)
dash=Button(text='Dashboard',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=das)
dash.place(x=1,y=30)
medicine=Button(text='Daily planner',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=planner)
medicine.place(x=1,y=100)
category=Button(text='Calendar',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2')
category.place(x=1,y=170)
billing=Button(text='Quiz',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=quiz)
billing.place(x=1,y=240)
analytic=Button(text='Exam',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=exam)
analytic.place(x=1,y=310)
setting=Button(text='User Setting',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=user)
setting.place(x=1,y=380)



# Add Calendar
cal = Calendar(root, selectmode = 'day',
			year = 2023, month = 7,
			day = 26)

cal.place(x=300,y = 40,width=900,height=500)

def grad_date():
	date.config(text = "Selected Date is: " + cal.get_date())

Button(root, text = "Select Date",
	command = grad_date,width=14,height=3,bg="green").place(x=500,y = 550)

date = Label(root, text = "")
date.pack(pady = 20)

# Execute Tkinter
root.mainloop()
