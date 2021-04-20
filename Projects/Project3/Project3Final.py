from tkinter import *
import os


#Creates GUI
root = Tk()


# Creates and displays the on screen text
myLabel1 = Label(root, text="This program removes spaces from file names and replaces them with underscores(_). To use it select the red input box and delete the text in it. Then type copy the full file path into the red text box. Finally select the button below to update all files within the path to remove spaces and add underscores.")
myLabel1.pack()


# Creates the text box to enter in file path and displays it
e = Entry(root, width=50, bg="red", fg="white", borderwidth="3")
e.pack()
e.insert(0, "Enter Desired Directory Path Here: ")

# Creates Button and Displays it
myButton = Button(root, text="Click Here", command=myClick,)
myButton.pack()

# Function to get text input and and change file names from have spaces to underscores
def myClick():
    path = e.get()
    myLabel = Label(root, text="The Directory you have entered is " + path) 
    myLabel.pack()
    for filename in os.listdir(path):
        os.rename(os.path.join(path,filename),os.path.join(path, filename.replace(' ',"_")))


# Loop the GUI to recieve user input.
root.mainloop()
