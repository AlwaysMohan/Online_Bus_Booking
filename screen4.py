from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(h,w))
bus=PhotoImage(file='.\\bus.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//2.5)
Label(root,text="Online Bus Booking System",bg='light blue',fg='red',font='Arial 24 bold').grid(row=1,column=0,columnspan=10,padx=w//2.5,pady=h//30)
Button(root,text='Check Booking Details',bg='light green',font='Arial 16 bold').grid(row=2,column=0,columnspan=10,padx=w//2.5,pady=h//30)
Label(root,text='Enter Your Mobile No:',font='Arial 10 bold').grid(row=3,column=2,sticky=E)
Entry(root).grid(row=3,column=3)
Button(root,text='Check Booking').grid(row=3,column=4)
root.mainloop()

