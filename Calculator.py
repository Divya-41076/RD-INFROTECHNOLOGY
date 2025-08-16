from tkinter import *
root= Tk()

root.title('Simple Calculator')
root.geometry('400x367')
e = Entry(root,bg='white',width=25,borderwidth=5,
          font=('Arial', 20))
e.pack(padx=2,pady=2)

input=''
# e.insert(0,'Enter your name:')
def button_click(num):
    # e.delete(0,END)
    e.insert(END,num)
    global input
    input += num
    print(input)
   

def button_equal():
    global input
    try:
        res = eval(input)
        e.delete(0,END)
        e.insert(0,str(res))
    except:
        e.delete(0,END)
        e.insert(0,'INVALID INPUT')
        input = ''
        
def button_clear():
    e.delete(0, END)
    global input 
    input = ''

def button_del():
    global input
    current_text = e.get()
    if len(current_text) > 0:
        e.delete(len(current_text)-1, END)
        input = input[:-1]

def button_doublezero():
    button_click('0')
    button_click('0')


def button_abs():
    global input
    current_text = e.get()
    last=current_text[-1]
    print(last)
    e.insert(len(input),'(')
    e.insert(len(input)+1, int(last)*(-1))
    e.insert(len(input)+2,')')
    

# define buttons
frame=Frame(root)
frame.pack()

button_1 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "1 " , padx=40, pady=20, command = lambda: button_click('1'))
button_2 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "2 " , padx=40, pady=20, command = lambda: button_click('2'))
button_3 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "3 " , padx=40, pady=20, command = lambda: button_click('3'))
button_4 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "4 " , padx=40, pady=20, command = lambda: button_click('4'))
button_5 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "5 " , padx=40, pady=20, command = lambda: button_click('5'))
button_6 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "6 " , padx=40, pady=20, command = lambda: button_click('6'))
button_7 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "7 " , padx=40, pady=20, command = lambda: button_click('7'))
button_8 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "8 " , padx=40, pady=20, command = lambda: button_click('8'))
button_9 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "9 " , padx=40, pady=20, command = lambda: button_click('9'))
button_0 = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "0 " , padx=40, pady=20, command = lambda: button_click('0'))

button_clear = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "AC" , padx=20, pady=20, width=7, command = button_clear)
button_modulus = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text = "%" , padx=39, pady=20, command = lambda: button_click('%'))

button_add = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text='+', padx= 40, pady=20, command = lambda: button_click('+'))
button_subtract = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text='-', padx= 40, pady=20, command = lambda: button_click('-'))
button_multiply = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text='x', padx= 40, pady=20, command = lambda: button_click('*'))
button_divide = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text='/', padx= 40, pady=20, command =lambda: button_click('/'))

button_del = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text='del', padx= 19, pady=20, command = button_del)
button_abs = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text='x^y', padx= 40, pady=20, command = lambda: button_click('**'))
button_doublezero = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text='00', padx= 38.6, pady=20, command = button_doublezero)
button_equal = Button(frame,activebackground='lightgrey',activeforeground='grey', font=('Arial',8,'bold') ,text='=', padx=40, pady=20, command = button_equal)

# put buttons on the screen
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_clear.grid(row=1, column=0)
button_modulus.grid(row=1,column=1)
button_del.grid(row=1,column = 2,columnspan = 1,sticky ='nsew')
button_abs.grid(row =1, column = 3)

button_0.grid(row=5, column=1)
button_doublezero.grid(row=5,column = 0)

button_add.grid(row = 4, column=3,columnspan=1,sticky='nsew')
button_subtract.grid(row=5,column=3,columnspan = 1,sticky="nsew")
button_multiply.grid(row=3,column=3,columnspan = 1,sticky="nsew")
button_divide.grid(row=2,column=3,columnspan = 1,sticky="nsew")

button_equal.grid(row=5,column=2, sticky="nsew")

root.mainloop()
