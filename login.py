from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mysql
root=Tk()
root.title("TaskNinja🥷")
root.geometry("1000x600") 
root.resizable(0,0) 


#===background image

my_image=Image.open("login.png")
resized_image=my_image.resize((1000,600))
converted_image=ImageTk.PhotoImage(resized_image)
my_label=Label(root,image=converted_image,width=1000,height=600)
my_label.pack()
 
def signin():
    try:
            con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='taskninja')
            mycursor=con.cursor()
    except:
            messagebox.showerror("error","connection error")
    query='select * from user where email=%s and password=%s'
    mycursor.execute(query,(username1.get(),new_password.get()))
    row=mycursor.fetchone()
    if row==None:
       messagebox.showerror("error","invalid username or password")
    else:
        root.destroy()
        import dashboard
def registration():
    import tkinter as tk
    base = tk.Tk()
    base.geometry('500x500')  
    base.title("Registration Form")  
  
    labl_0 = Label(base, text="Registration form",width=20,font=("bold", 20))  
    labl_0.place(x=90,y=53)  
  
  
    labl_1 = Label(base, text="FullName",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=130)  
  
    entry_1 = Entry(base)  
    entry_1.place(x=240,y=130)  
  
    labl_2 = Label(base, text="Email",width=20,font=("bold", 10))  
    labl_2.place(x=68,y=180)  
  
    entry_02 = Entry(base)  
    entry_02.place(x=240,y=180) 

    labl_3 = Label(base, text="Gender",width=20,font=("bold", 10))  
    labl_3.place(x=70,y=230)
    
    Gender_Variable = tk.StringVar(base)
    Gender_Variable.set("Options")
    Gender_Option = tk.OptionMenu(base,Gender_Variable,"Male", "Female","Others")
    Gender_Option.place(x=242,y=230)

    labl_4 = Label(base, text="Age:",width=20,font=("bold", 10))  
    labl_4.place(x=70,y=280)  
  
  
    entry_03 = Entry(base)  
    entry_03.place(x=240,y=280)  
    
    labl_1 = Label(base, text="password",width=20,font=("bold", 10))  
    labl_1.place(x=80,y=330)  
  
    entry_4 = Entry(base,show="*")  
    entry_4.place(x=240,y=330) 
    
    def submit(): 
        try:
                    con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='taskninja')
                    mycursor=con.cursor()
        except:
                messagebox.showerror("error","connection error! please add again")
                
        try:
                vals={ 
                    "fullname":entry_1.get(), 
                        "email":entry_02.get(),  
                        "age":entry_03.get(),
                        "password":entry_4.get()
                        }
                insert_query="""INSERT INTO user( fullname, email, age,password) VALUES(  %s, %s, %s,%s)""",( vals['fullname'],vals['email'],int(vals['age']),vals['password'])
                mycursor.execute(*insert_query)
                con.commit()
                mycursor.close()
                con.close()
                entry_1.delete(0,'end')
                entry_02.delete(0,'end')
                entry_4.delete(0,'end')
                entry_03.delete(0,'end')
        except:
                entry_1.delete(0,'end')
                entry_02.delete(0,'end')
                entry_4.delete(0,'end')
                entry_03.delete(0,'end')
    
    Button(base, text='Submit',width=20,bg='brown',fg='white',command=submit).place(x=180,y=380)  
    base.mainloop()  
def forget():
        top=Toplevel()
        top.title("Forget Password")
        top.geometry("1000x600") 
        top.resizable(0,0) 
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
        settings=Label(top,text='Forget Password?',fg='#363740',bg='#fafafa',font=('inter',15,'bold'))
        settings.place(x=360,y=40)
        # username 
        username=Entry(top,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),width=40,cursor='hand2')
        username.place(x=240,y=120,height=40)
        username.insert(5,'Email')



        new_password=Entry(top,width=40,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),cursor='hand2',show='*')
        new_password.place(x=240,y=200,height=40)
        new_password.insert(5,'New Password')


        
        confirm_password=Entry(top,width=40,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),cursor='hand2',show='*')
        confirm_password.place(x=240,y=280,height=40)
        confirm_password.insert(5,'Confirm Password')

        save=Button(top,text='SAVE',width=10,bg='green',fg='white',font=("microsoft yaHei UI light",12),cursor='hand2',command=save)
        save.place(x=240,y=360)

   
log=Frame(root,bg='#D9D9D9',border=0,width=350)
log.place(x=600,y=100,height=380)
def on_enter(e):
        username1.delete(0,'end')
        
def on_leave(e):
        name=username1.get()
        if name=='':
            username1.insert(0,"")
        # return name  
    # username 
username1=Entry(log,fg='black',bg='#1974D2',border=0.6,font=('microsoft yaHei UI light',9),width=40,cursor='hand2')
username1.place(x=30,y=80,height=30)
username1.insert(5,'Email')
username1.bind('<FocusIn>',on_enter)
username1.bind('<FocusOut>',on_leave) 

 # password functionality
def on_enter(e):
        new_password.delete(0,'end')
def on_leave(e):
        name=new_password.get()
        if name=='':
            new_password.insert(5,'')
    # /password workspace     
new_password=Entry(log,width=40,fg='black',bg='#1974D2',border=0.6,font=('microsoft yaHei UI light',9),cursor='hand2',show='*')
new_password.place(x=30,y=140,height=30)
new_password.insert(5,'New Password')
new_password.bind('<FocusIn>',on_enter)
new_password.bind('<FocusOut>',on_leave)
Button(log,width=35,pady=5,text='Log In',bg='#D62727',fg='white',border=0,font=('Inter',10,'bold'),cursor='hand2',command=signin).place(x=30,y=190)
forgotbutton=Button(log,text="Forgot Password?",bd=0,bg='#D9D9D9',cursor='hand2',font=('microsoft yaHei UI light',10,'bold'),command=forget)
forgotbutton.place(x=120,y=230)
frame1=Frame(log,width=300,bg="black")
frame1.place(x=30,y=260)
create=Button(log,text="CREATE NEW ACCOUNT",bd=0,bg='green',fg="black",cursor='hand2',font=('microsoft yaHei UI light',10,'bold'),command=registration)
create.place(x=100,y=290)

root.mainloop()