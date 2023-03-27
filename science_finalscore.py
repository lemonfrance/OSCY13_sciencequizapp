from tkinter import *
import science_quizroutine 
import science_choosemode 
import science_startmenu 
import os

class Score:
    def __init__(self,parent,name,age,title,fgColor,bgColor,questions,answers,scorelist,time,explanation):##20may:new param
        self.name=name
        self.age=age
        self.parent=parent
        self.title=title
        self.fgColor=fgColor
        self.bgColor=bgColor
        self.questions=questions
        self.answers=answers
        self.scorelist=scorelist
        self.explanation = explanation ##20may
        self.time=time 
        if self.time < 60:
            self.time = str(self.time)+" seconds"
        elif self.time >= 60:
            self.time = str(round(self.time/60,2))+" minutes"
        self.perfScore = len(questions)
        parent.geometry("+500+30")
        parent.title(title)
        parent.configure(bg=self.bgColor,padx=75,pady=75)
        self.randomLabel = Label(self.parent,text=self.title,font="Arial 20 bold",fg=self.fgColor,bg=self.bgColor)
        self.randomLabel.pack()
    def calcScore(self):
        return sum(self.scorelist)
    def displayUserScore(self): 
        self.userFinalScore= self.calcScore()
        self.userFinalPercent = (int(self.userFinalScore)/self.perfScore)*100
        self.randomLabel = Label(self.parent,text="\n"+self.name+", your score percentage is:",font="Arial 18",fg=self.fgColor,bg=self.bgColor)
        self.randomLabel.pack()
        self.randomLabel= Label(self.parent,text=str(self.userFinalPercent) + "%",font="Arial 36 bold",fg=self.fgColor,bg=self.bgColor)
        self.randomLabel.pack()
        self.randomLabel = Label(self.parent,text="\nAlso, you've finished the quiz in "+self.time+".",font="Arial 18",fg=self.fgColor,bg=self.bgColor)
        self.randomLabel.pack()
        if self.userFinalPercent == 100:
            self.randomLabel = Label(self.parent,text="Excellent! \n You really are a science whizz!\n",font="Arial 18",fg=self.fgColor,bg=self.bgColor)
            self.randomLabel.pack()
        elif self.userFinalPercent >= 80 and self.userFinalPercent < 100:
            self.randomLabel = Label(self.parent,text="Very good! \n You really are a science whizz!\n",font="Arial 18",fg=self.fgColor,bg=self.bgColor)
            self.randomLabel.pack()
        elif self.userFinalPercent < 80 and self.userFinalPercent > 50:
            self.randomLabel = Label(self.parent,text="Good! You have the potential to become \n a science whizz with a few more practice.\n",font="Arial 18",fg=self.fgColor,bg=self.bgColor)
            self.randomLabel.pack()
        elif self.userFinalPercent == 50:
            self.randomLabel = Label(self.parent,text="Not bad! \n Aim higher and practice more.\n",font="Arial 18",fg=self.fgColor,bg=self.bgColor)
            self.randomLabel.pack()
        elif self.userFinalPercent < 50:
            self.randomLabel = Label(self.parent,text="Try better next time! \n Practice makes perfect.\n",font="Arial 18",fg=self.fgColor,bg=self.bgColor)
            self.randomLabel.pack()
        self.saveScoreBtn=Button(self.parent,text="Save Score Details as Text File",command=self.saveScore,font="Arial 18 bold",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.saveScoreBtn.pack()
        
        self.randomLabel=Label(self.parent,text="",bg=self.bgColor)
        self.randomLabel.pack()
        
        self.restartModeBtn= Button(self.parent,text="Restart Mode",command=lambda:self.restartMode(self.parent),font="Arial 18 bold",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.restartModeBtn.pack()
        
        self.randomLabel=Label(self.parent,text="",bg=self.bgColor)
        self.randomLabel.pack()
        
        self.backModeBtn = Button(self.parent,text="Choose Mode",command = lambda:self.backMode(self.parent),font="Arial 18 bold",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.backModeBtn.pack()

        self.randomLabel=Label(self.parent,text="",bg=self.bgColor)
        self.randomLabel.pack()
        
        self.backMainBtn = Button(self.parent,text="Back to Main Menu",command = lambda:self.backMain(self.parent),font="Arial 18 bold",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.backMainBtn.pack()

        self.randomLabel=Label(self.parent,text="",bg=self.bgColor)
        self.randomLabel.pack()
        
        self.exitBtn = Button(self.parent,text="Exit Program",command = lambda:self.exitProgram(self.parent),font="Arial 18 bold",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.exitBtn.pack()

        self.separator = Frame(self.parent,height=2,relief=SOLID,bg=self.fgColor)
        self.separator.pack(fill=X,padx=20,pady=20)
        self.randomLabel = Label(self.parent, text="Created by Franz Naling (2018)",font="Arial 14 bold",fg=self.fgColor,bg=self.bgColor,pady=5,padx=5).pack()
    def restartMode(self,parent): 
        parent.destroy()
        restartWindow = science_quizroutine.Quiz(self.name,self.age,self.title,self.fgColor,self.bgColor,self.questions,self.answers,self.explanation)#20may
        restartWindow.quizRoutine()
    def saveScore(self):
        #based on: https://stackoverflow.com/questions/17984809/how-do-i-create-a-incrementing-filename-in-python
        increment = 0
        self.userScoreFilename = self.name+"_sciencescore.txt"
        while os.path.exists(self.userScoreFilename):
            increment+=1
            self.userScoreFilename = self.name+str(increment)+"_sciencescore.txt"
        with open(self.userScoreFilename,"w") as self.userScoreFile:
            self.userScoreFile.write("Name: "+str(self.name)+"\n")
            self.userScoreFile.write("Age: "+str(self.age)+"\n")
            self.userScoreFile.write("Mode: "+str(self.title)+"\n")
            self.userScoreFile.write("Score: "+str(self.userFinalScore)+"/"+str(self.perfScore)+"\n")
            self.userScoreFile.write("Percentage: "+str(self.userFinalPercent)+"% \n")
            self.userScoreFile.write("Total Quiz Time: "+self.time)
            self.userScoreFile.close()
    def backMode(self,parent): 
        parent.destroy()
        modeWindow = Tk()
        science_choosemode.ModeSelection(self.name,self.age,modeWindow)
    def backMain(self,parent): 
        parent.destroy()
        root = Tk()
        science_startmenu.MainMenu(root)
    def exitProgram(self,parent): #added parent as parameter so that i can use it in another file
        exitMsg = messagebox.askyesno(title="Exit Program", message="Are you sure?")
        if exitMsg:
            parent.destroy()
        else:
            pass
