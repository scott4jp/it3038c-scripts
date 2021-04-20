from tkinter import *

root = Tk()



myLabel1 = Label(root, text="Hello World!")
myLabel1.pack()

e = Entry(root, width=50, bg="red", fg="white", borderwidth="3")
e.pack()
e.insert(0, "Enter Desired Directory Path Here: ")


def myClick():
    Directory = e.get()
    myLabel = Label(root, text="The Directory you have entered is " + Directory) 
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

root.mainloop()