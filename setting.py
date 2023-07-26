from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("setting/Taskninja")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400","300")
root.state("zoomed")

    
def save():
    try:
            con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='taskninja')
            mycursor=con.cursor()
    except:
            messagebox.showerror("error","connection error")
            return
        
    if new_password.get() == confirm_password.get():
        vals={
            
            "password": confirm_password.get(),
            "email": username.get()
       }
        query='UPDATE user  SET password=%s WHERE Email=%s',(vals['password'],vals['email'])
        mycursor.execute(*query)
        con.commit()
        mycursor.close()
        con.close()
        username.delete(0,'end')
        confirm_password.delete(0,'end')
        new_password.delete(0,'end')
        messagebox.showinfo('Password',"updated sucessfully")
        



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
   
frame=Frame(root,width=160,padx=30,bg='black')
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
setting=Button(text='User Setting',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2')
setting.place(x=1,y=380)   



# frame for displaying setting details 

settings=Label(root,text='User Settings',fg='#363740',bg='#fafafa',font=('inter',15,'bold'))
settings.place(x=560,y=110)
# username 
username=Entry(root,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),width=40,cursor='hand2')
username.place(x=440,y=200,height=40)
username.insert(5,'Email')



new_password=Entry(root,width=40,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),cursor='hand2',show='*')
new_password.place(x=440,y=300,height=40)
new_password.insert(5,'New Password')


   
confirm_password=Entry(root,width=40,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),cursor='hand2',show='*')
confirm_password.place(x=440,y=400,height=40)
confirm_password.insert(5,'Confirm Password')

save=Button(root,text='SAVE',width=10,bg='green',fg='white',font=("microsoft yaHei UI light",12),cursor='hand2',command=save)
save.place(x=780,y=500)



root.mainloop()