from tkinter import*
from tkinter import messagebox
def processOK():
    print("I am OK")
def processCancel():
    messagebox.showinfo("Cancel Message", "This is cancel")
window=Tk()
window.geometry("200x300")
label_1=Label(window,text="Python window programming")
label_1.pack()
b1=Button(window,text="OK", bg="Yellow", command=processOK).pack(side=TOP)
b2=Button(window, text="Cancel",bg="Green", command=processCancel).pack(side=TOP)
window.mainloop()

