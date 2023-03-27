from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from science_choosemode import ModeSelection

class MainMenu:
    def __init__(self,parent):
        self.parent=parent
        self.parent.title("Science Whizz | Main Menu")
        self.parent.geometry("630x670+500+150")
        self.parent.configure(bg="#00EA91",padx=75,pady=75)
        self.randomLabel = Label(parent,text="Welcome to Science Whizz!",font="Arial 20 bold",fg="#FFFACD",bg="#00EA91",pady=5,padx=5).pack()
        self.randomLabel = Label(parent,text="a science quiz programme to help Senior \n College students with their Science",font="Arial 16 bold",justify="center",fg="white",bg="#00EA91",pady=5,padx=5).pack()
        self.strvar = StringVar()
        self.intvar = IntVar()
        self.randomLabel = Label(parent,text="Name:",font="Arial 18 bold",fg="#FFFACD",bg="#00EA91",pady=15,padx=15).pack()
        self.userNameBox = Entry(parent,textvariable=self.strvar,relief=FLAT,font="Arial 18",bd=8,width=18)
        self.userNameBox.pack()
        self.randomLabel = Label(parent,text="Age:",font="Arial 18 bold",fg="#FFFACD",bg="#00EA91",pady=15,padx=15).pack()
        self.userAgeBox = Entry(parent,textvariable=self.intvar,relief=FLAT,font="Arial 18",bd=8,width=7)
        self.userAgeBox.pack()
        self.randomLabel = Label(parent,text="",font="Arial 15",bg="#00EA91").pack()
        self.startBtn = Button(parent,text="Start Quiz",relief=FLAT,command=self.startBtnCommand,font="Arial 18 bold",fg="white",bg="#00C479",pady=3,padx=5)
        self.startBtn.pack()
        self.randomLabel = Label(parent,text="",font="Arial 5",bg="#00EA91").pack()
        self.separator = Frame(parent,height=2,relief=SOLID,bg="white")
        self.separator.pack(fill=X,padx=20,pady=20)
        self.randomLabel = Label(parent, text="Created by Franz Naling (2018)",font="Arial 14 bold",fg="white",bg="#00EA91",pady=5,padx=5).pack()
    def startBtnCommand(self):
        global userName
        global userAge
        self.userName = str(self.userNameBox.get())
        self.userAge = self.userAgeBox.get()
        if len(self.userName)==0 or len(self.userAge)==0:
            messagebox.showerror("Incomplete Details","Please enter all details!")
        else:
            ##19 may: new condition for name length - 25 char limit no: \/:*?"<>|
            self.prohibChar = list('\/:*?"<>|')
            try:##to ensure age input is an integer
                if len(self.userName) > 25:
                    messagebox.showerror("Character limit","The maximum number of characters you can only have for your name is 25. Please try again.")
                elif any((pc in self.prohibChar) for pc in list(self.userName)):
                    messagebox.showerror("Prohibited Characters",'Your name must not contain the following: \ / : * ? " < > | ')
                elif int(self.userAge) not in range(15,20):
                    messagebox.showerror("Age Input Error","You must be 15 to 19 years of age to proceed.")
                elif len(self.userName) <= 25 and int(self.userAge) in range(15,20) and bool(any((pc in self.prohibChar) for pc in list(self.userName)))==False:
                    self.parent.withdraw()
                    global modeWindow
                    modeWindow=Tk()
                    self.modeWindow = ModeSelection(self.userName,self.userAge,modeWindow)
            except ValueError:##to ensure age input is an integer
                messagebox.showerror("Age Input Error","Please enter a number for the age.")
            ###
        
