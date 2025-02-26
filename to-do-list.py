from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle


root = Tk()
root.title("TO-DO-LIST")
root.iconbitmap()
root.geometry('600x500')

my_font=Font(
    family='Brush Script MT',
    size=30,
    weight='bold'
)
my_frame=Frame(root)
my_frame.pack(pady=10)

my_list = Listbox (my_frame,
    font=my_font,
    width=25,
    height=5,
    bg='SystemButtonFace',
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle='none'
)
my_list.pack(side=LEFT, fill= BOTH)

# lets create dummy list

# stuff=['walk the dog','buy groceries','pick up the kids at 3','leanr tkinter','Rule the world']
# # add dummy list to the box
# for item in stuff:
#     my_list.insert(END,item)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side = RIGHT, fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar)
my_scrollbar.config(command=my_list.yview)

# entry box
search_var = StringVar()
my_entry = Entry(root, font=("Helvetica",24),width=26 , textvariable=search_var)
my_entry.pack(pady=20)
def clear_search_box():
        search_var.set('')
       

button_frame=Frame(root)
button_frame.pack(pady=20)

# functions
def delete_item():
    my_list.delete(ANCHOR)#it deletes whatever is highlighted

def add_item():
    my_list.insert(END, my_entry.get())
    clear_search_box()
    #we need to clear the entry words??

def crossoff_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg='#dedede'  
    )
    # get rid of selection bar
    my_list.selection_clear(0,END)
     
    
def uncrossoff_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg='#464646'  
    )
    # get rid of selection bar
    my_list.selection_clear(0,END)

def delete_crossedoff():
     ind_list=0
     while ind_list<my_list.size():
        if my_list.itemcget(ind_list,'fg') == '#dedede':
            my_list.delete(my_list.index(ind_list))

        ind_list+=1
# save and open:
def remove_list():
    my_list.delete(0,END)


# pickle function
def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/divmi/Desktop/dev",
        title = 'Save File',
        filetypes=[('dat files','*.dat'),("all files","*.*")]
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
    #delte crossed of item before saving the list
    delete_crossedoff()

    # grab all the stuff
    stuff = my_list.get(0, END)

    output_file=open(file_name, 'wb')

    pickle.dump(stuff, output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir= 'C:/Users/divmi/Desktop/dev',
        title = 'OPEN FILE',
        filetypes=[('dat','*.dat'),('all files','*.*')]
    )
    # delete the current open list
    if file_name:
        remove_list()

    # open the file
    input_file = open(file_name, 'rb')

    # load the data from the file
    stuff = pickle.load(input_file)

    # output stuff to the screen 
    for item in stuff:
        my_list.insert(END, item)
    


#create menu
my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File',menu=file_menu)
 

# adding dropdown items in file
file_menu.add_command( label='Save List', command=save_list)
file_menu.add_command( label='Open List', command=open_list)
file_menu.add_separator()
file_menu.add_command( label='Clear List', command=remove_list)


# buttons of various function
delete_button=Button(button_frame,text='delete item',command=delete_item)
add_button=Button(button_frame,text='add item',command=add_item)
cross_button=Button(button_frame,text='cross off item',command=crossoff_item)
uncross_button=Button(button_frame,text='uncross off item',command=uncrossoff_item)
delete_crossed=Button(button_frame,text='delete crossed',command=delete_crossedoff)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1, padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed.grid(row=0,column=4)


root.mainloop()

