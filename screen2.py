from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(h,w))
def gui1():
    root.destroy()
    import screen3.py

def gui2():
    root.destroy()
    import screen4.py

def gui3():
    root.destroy()
    import screen6.py
    
frame1=Frame(root)
frame1.grid(row=0,column=2,padx=50)
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(frame1,image=bus).grid(row=1,column=4)
Label(frame1,text="Online Bus Booking System",bg='light blue',fg='red',font='Arial 24 bold').grid(row=2,column=4,pady=20)
Button(frame1,text='Seat Booking',bg='green',font='Arial 16 bold',command=gui1).grid(row=5,column=3,padx=100,pady=40)
Button(frame1,text='Check Booked Seat',bg='green',font='Arial 16 bold',command=gui2).grid(row=5,column=4,padx=20)
Button(frame1,text='Add Bus Details',bg='green',font='Arial 16 bold',command=gui3).grid(row=5,column=5,padx=100)
Label(frame1,text="For Admin Only",fg='red',font='Arial 12 bold').grid(row=7,column=5,pady=20)
root.mainloop()
