from tkinter import *
import time

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # add a clock
        self.label = Label(text="", fg="Blue", font=("Helvetica", 12))
        self.label.place(x=560, y=450)
        self.update_clock()

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create a menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

        # create a label
        text = Label(self, text="This is a label", font=("Helvetica", 18))
        text.place(x=250, y=180)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton, width=10)

        # place button at
        exitButton.place(x=300, y=400)

    def clickExitButton(self):
        exit()

    def exitProgram(self):
        exit()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)

# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("Tkinter Window")

root.geometry("640x480")

root.after(1000, app.update_clock)

# show window
root.mainloop()