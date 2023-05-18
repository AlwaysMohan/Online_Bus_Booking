from tkinter import*
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(h,w))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).pack()
Label(root,text="Online Bus Booking System",bg='light blue',fg='red',font='Arial 24 bold').pack()
#Entry(root).grid(row=3,column=4)
#Button(root,text="OK").grid(row=4,column=4)

Label(root,text="Name: Mohan Choudhary",fg='blue',font='Arial 12 bold').pack(pady=30)

Label(root,text='Er: 211B400',fg='blue',font='Arial 12 bold').pack(pady=10)

Label(root,text='Mobile: 9610008666',fg='blue',font='Arial 12 bold').pack(pady=20)
Label(root,text="").pack()
Label(root,text="Submitted to : Dr. Mahesh Kumar",bg='light blue',fg='red',font='Arial 16 bold').pack()

Label(root,text="Project Based Learning",fg='red',font='Arial 12 bold').pack(pady=10)
def close(e=0):
    root.destroy()
    import screen2.py

root.bind("<KeyPress>",close)
root.mainloop()
 
