import tkinter
from tkinter import *
import string
import random
import pyperclip

# Function to generate random password:
def generate():
    lower_alphabets=string.ascii_lowercase
    upper_alphabets=string.ascii_uppercase
    digits=string.digits
    s_char=string.punctuation

    combine=lower_alphabets+upper_alphabets+digits+s_char

    pass_len=int(s_box.get())
    # password=random.sample(combine,pass_len)
    # e_field.insert(0,password)

    if choice.get()==1:
        e_field.insert(0,random.sample(lower_alphabets+upper_alphabets,pass_len))
    
    if choice.get()==2:
        e_field.insert(0,random.sample(lower_alphabets+s_char+upper_alphabets,pass_len))

    if choice.get()==3:
        e_field.insert(0,random.sample(combine,pass_len))

# Function to copy generated password:
def copy():
    c_password=e_field.get()
    pyperclip.copy(c_password)

root=Tk()
choice=IntVar()
Font=('arial',13,'bold')
root.config(bg='gray20')
pass_label=Label(root,text="Password Generator",font=('times new roman',20,'bold'),fg='white',bg='gray20')
pass_label.grid(pady=10)

w_radiobutton=Radiobutton(root,text="WEAK",value=1,variable=choice,font=Font) # Button for Weak Password
w_radiobutton.grid(pady=5)


m_radiobutton=Radiobutton(root,text="MEDIUM",value=2,variable=choice,font=Font) # Button for medium password
m_radiobutton.grid(pady=5)

s_radiobutton=Radiobutton(root,text="STRONG",value=3,variable=choice,font=Font) # Button for Strong password
s_radiobutton.grid(pady=5)

len_label=Label(root,text="Password Length",font=('times new roman',20,'bold'),fg='white',bg='gray20')
len_label.grid(pady=10)

s_box=Spinbox(root,from_=5,to_=24,width=5,font=Font)
s_box.grid(pady=4)

g_button=Button(root,text='GENERATE',font=Font,command=generate)
g_button.grid(pady=5)

e_field=Entry(root,width=25,bd=2,font=Font)
e_field.grid(pady=5)

copy_button=Button(root,text='COPY',font=Font,command=copy)
copy_button.grid(pady=5)

c_button=Button(root,text='CLEAR',font=Font,command=lambda:e_field.delete(0,'end'))
c_button.grid(pady=5)

root.mainloop()