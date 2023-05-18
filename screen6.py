from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(h,w))
def gui4():
    root.destroy()
    import screen7.py

def gui5():
    root.destroy()
    import screen10.py

def gui6():
    root.destroy()
    import screen9.py

def gui7():
    root.destroy()
    import screen8.py
       
bus=PhotoImage(file='.\\bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
Label(root,text="Online Bus Booking System",bg='light blue',fg='red',font='Arial 24 bold').grid(row=1,column=0,columnspan=10,padx=w//2.5,pady=h//30)
Label(root,text="Add New Details to Database",bg='white',fg='green',font='Arial 18 bold').grid(row=2,column=0,columnspan=10,pady=h//30)
Button(root,text='New Operator',bg='green',font='Arial 14 bold',command=gui4).grid(row=3,column=2)
Button(root,text='New Bus',bg='orange',font='Arial 14 bold',command=gui5).grid(row=3,column=3)
Button(root,text='New Route',bg='royal blue',font='Arial 14 bold',command=gui6).grid(row=3,column=4)
Button(root,text='New Run',bg='light pink',font='Arial 14 bold',command=gui7).grid(row=3,column=5)
root.mainloop()
