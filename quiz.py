from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import json
from tkinter import messagebox
import mysql.connector as mysql

root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("Quiz/taskninja")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400","300")
root.state("zoomed")

def planner():
    root.destroy()
    import dailyplanner
def cal():
    root.destroy()
    import ca
def das():
    root.destroy()
    import dashboard
def exam():
    root.destroy()
    import exam


frame=Frame(width=160,padx=30,bg='black')
frame.pack(side=LEFT,fill=Y)
dash=Button(text='Dashboard',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=das)
dash.place(x=1,y=30)
planner=Button(text='Daily planner',width=15,height=3,border=1,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=planner)
planner.place(x=1,y=100)
calander=Button(text='Calendar',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=cal)
calander.place(x=1,y=170)
quiz=Button(text='Quiz',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2')
quiz.place(x=1,y=240)
analytic=Button(text='Exam',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2',command=exam)
analytic.place(x=1,y=310)
setting=Button(text='User Setting',width=15,height=3,border=0,bg='#FAFAFA',fg='black',font=("Inter", 12, "bold"),cursor='hand2')
setting.place(x=1,y=380)

questions = ["What is the maximum length of a Python identifier?","What will be the output of the following code snippet? print(2**3 + (5 + 6)**(1 + 1))","How is a code block indicated in Python?","Which of the following statements are used in Exception Handling in Python?","As what datatype are the *args stored, when passed into a function?"]
options = [['32','16','128','No length specified.','No length specified.'],['129','8','121','None of the above.','129'],
           ['Brackets.','Indentation.','Key','None of the above.','Indentation.'],['try','except','finally','All of the above','All of the above'],['List.','Tuple.','Dictionary.','None of the above.','Tuple.']]

5
frame =Frame(root, padx=10, pady=10,bg='#fff')
question_label =Label(frame,height=5, width=28,bg='grey',fg="#fff", 
                          font=('Verdana', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 =Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
option2 =Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
option3 =Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
option4 =Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))

button_next =Button(frame, text='Next',bg='Grey', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)


index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/1:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'





    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'





displayNextQuestion()

    


# programming=Button(root,text="Programming",bg="green",fg="black",width=20,height=5,font=("Inter", 12, "bold"),cursor='hand2',command=programming)
# programming.place(x=200,y=200)

root.mainloop()