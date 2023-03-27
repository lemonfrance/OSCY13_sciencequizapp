from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
from science_finalscore import Score  
import science_startmenu 
import science_choosemode
from threading import Timer

##20may: new param explanation
class Quiz:
    def __init__(self,name,age,title,fgColor,bgColor,questions,answers,explanation):
        global userScore
        global quizWindow
        quizWindow = Tk()
        quizWindow.title(title)
        self.userScore = []
        self.name = name
        self.age=age
        self.title=title
        self.bgColor=bgColor
        self.fgColor=fgColor
        self.questions=questions
        self.answers=answers
        self.explanation = explanation ##20may: new param explanation
        self.multiChoices = [
            ("Homogenous","Heterozygous","Homozygous"),
            ("A heterozygous individual and a homozygous recessive individual","Two heterozygous individuals","A homozygous recessive and a homozygous dominant individual"),
            ("Recessive alleles","Dominant alleles","Homozygous alleles"),
            ("Alpha radiation","Beta radiation","Gamma radiation"),
            ("Heat Energy","Chemical Energy","Electrical Energy")]
        self.TorFchoices = ("True", "False")
        quizWindow.geometry("+500+0")#20may:changed y coordinate placement
        quizWindow.configure(bg=self.bgColor,padx=75,pady=75)
    def quizRoutine(self):
        global iterQuestions
        global iterAnswers
        global currentQuestion
        global currentAnswer
        self.iterQuestions = (q for q in self.questions)
        self.iterAnswers = (a for a in self.answers)
        self.iterExplan = (ex for ex in self.explanation)##20may
        
        self.currentQuestion = next(self.iterQuestions)
        self.currentAnswer = next(self.iterAnswers)
        self.currentExplan = next(self.iterExplan)##20may
        
        self.randomLabel=Label(quizWindow,text=self.title+"\n",font="Arial 20 bold",fg=self.fgColor,bg=self.bgColor,wraplength=450)
        self.randomLabel.grid(row=1)

        self.timeCounter = []
        self.timeCommand = []
        self.timeCommand.append("start")
        self.userQuizTime()

        self.escapeBtns = Frame(quizWindow,bg=self.fgColor,width=600,height=50,padx=19,pady=10)
        self.escapeBtns.grid(row=2)
        
        self.restartModeBtn= Button(self.escapeBtns,activebackground=self.fgColor,activeforeground=self.bgColor,text="Restart Mode",command=lambda:Score.restartMode(self,parent=quizWindow),font="Arial 10 bold underline",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.restartModeBtn.pack(side=LEFT)
        
        self.backModeBtn = Button(self.escapeBtns,activebackground=self.fgColor,activeforeground=self.bgColor,text="Choose Another Mode",command = lambda:Score.backMode(self,parent=quizWindow),font="Arial 10 bold underline",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.backModeBtn.pack(side=LEFT)

        self.backMainBtn = Button(self.escapeBtns,activebackground=self.fgColor,activeforeground=self.bgColor,text="Back to Main Menu",command = lambda:Score.backMain(self,parent=quizWindow),font="Arial 10 bold underline",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.backMainBtn.pack(side=LEFT)
        
        self.exitBtn = Button(self.escapeBtns,activebackground=self.fgColor,activeforeground=self.bgColor,text="Exit Program",command = lambda:Score.exitProgram(self,parent=quizWindow),font="Arial 10 bold underline",fg="white",bg=self.fgColor,relief=FLAT,pady=3,padx=5)
        self.exitBtn.pack(side=LEFT)
        
        self.infoBar = Label(quizWindow,padx=30,pady=15,font="Arial 16 bold",text="Question Number: "+str(self.questions.index(self.currentQuestion)+1)+"/"+str(len(self.questions))+"             Current Score: "+str(sum(self.userScore))+"/"+str(len(self.questions)), fg="white", bg=self.fgColor)
        self.infoBar.grid(row=3)
        self.displayQuestion=Label(quizWindow,wraplength=450,text=str(self.currentQuestion)+"\n",font="Arial 20 underline",fg=self.fgColor,bg=self.bgColor,padx=100,pady=15)##20may:add padding
        self.displayQuestion.grid(row=5)
        global userAnswerVar
        self.userAnswerVar = StringVar(master=quizWindow)
        if self.bgColor== "#B3FFC1":
            global iterChoices
            self.iterChoices = (mc for mc in self.multiChoices)
            global currentChoices
            self.MC_currentChoices()
        elif self.bgColor=="#BEF6FE":
            for i in self.TorFchoices: 
                self.TorFchoice = Radiobutton(quizWindow,text=i,value=i,variable=self.userAnswerVar,command=self.getAnswer,font="Arial 18",fg=self.fgColor,bg=self.bgColor)
                self.TorFchoice.grid()
                self.TorFchoice.deselect()
        elif self.bgColor=="#E5E6FF":
            self.userEntry = Entry(quizWindow,textvariable= self.userAnswerVar,relief=FLAT,font="Arial 18",bd=8,width=15)
            self.userEntry.grid()
        global submitBtn
        self.randomLabel=Label(quizWindow,text="",bg=self.bgColor)
        self.randomLabel.grid(row=9)
        self.submitBtn=Button(quizWindow,text="Submit",command=self.checkAnswer,relief=FLAT,font="Arial 18 bold",fg="white",bg=self.fgColor,pady=3,padx=5)
        self.submitBtn.grid(row=10)
        self.randomLabel=Label(quizWindow,text="",bg=self.bgColor)
        self.randomLabel.grid(row=11)
        self.separator = Frame(quizWindow,bg=self.fgColor,width=500,height=3)
        self.separator.grid(row=12)
        self.randomLabel = Label(quizWindow, text="\n Created by Franz Naling (2018)",font="Arial 14",fg=self.fgColor,bg=self.bgColor,pady=5,padx=5)
        self.randomLabel.grid(row=13)
        quizWindow.mainloop()
    def MC_currentChoices(self):
        self.currentChoices = next(self.iterChoices)
        ##20may: defined them separately again so that i can remove all of them when needed
        self.MCchoice1 = Radiobutton(quizWindow,wraplength=450,anchor="w",text=self.currentChoices[0],variable=self.userAnswerVar,command=self.getAnswer,value=self.currentChoices[0],font="Arial 18",fg=self.fgColor,bg=self.bgColor,padx=100,pady=15)##20may:add padding
        self.MCchoice1.grid(row=6)
        self.MCchoice2 = Radiobutton(quizWindow,wraplength=450,anchor="w",text=self.currentChoices[1],variable=self.userAnswerVar,command=self.getAnswer,value=self.currentChoices[1],font="Arial 18",fg=self.fgColor,bg=self.bgColor,padx=100,pady=15)##20may:add padding
        self.MCchoice2.grid(row=7)
        self.MCchoice3 = Radiobutton(quizWindow,wraplength=450,anchor="w",text=self.currentChoices[2],variable=self.userAnswerVar,command=self.getAnswer,value=self.currentChoices[2],font="Arial 18",fg=self.fgColor,bg=self.bgColor,padx=100,pady=15)##20may:add padding
        self.MCchoice3.grid(row=8)
    def getAnswer(self):
        global chosenAnswer
        self.chosenAnswer = self.userAnswerVar.get()
    def accuScore(self,userAnswer,corrAnswer):
        self.displayQuestion.grid_remove()##20may
        if self.bgColor == "#B3FFC1":##20may
            self.MCchoice1.grid_remove()##20may
            self.MCchoice2.grid_remove()##20may
            self.MCchoice3.grid_remove()##20may
        global checkLabel1
        self.checkLabel1=Label(quizWindow,text="The correct answer is",font="Arial 18",fg=self.fgColor,bg=self.bgColor,pady=10)
        self.checkLabel1.grid(row=5)
        global checkLabel2
        ##20may: new param explanation added to checkLabel2
        self.checkLabel2=Label(quizWindow,wraplength=450,text=corrAnswer+"\n\n"+self.currentExplan,font="Arial 18 bold",fg=self.fgColor,bg=self.bgColor,padx=100,pady=15)
        self.checkLabel2.grid(row=6)
        ###
        if (userAnswer.replace(" ","")).lower()==(corrAnswer.replace(" ","")).lower():
            self.afterSubmitLabel=Label(quizWindow,text="You got it correct! \n +1",font="Arial 16",fg=self.fgColor,bg=self.bgColor,padx=100)##20may:add padding
            self.afterSubmitLabel.grid(row=7)
            self.userScore.append(1)
        else:
            global afterSubmitLabel
            self.afterSubmitLabel = Label(quizWindow,wraplength=450,text="You answered '{}' \n which is incorrect.".format(userAnswer),font="Arial 16",fg=self.fgColor,bg=self.bgColor)
            self.afterSubmitLabel.grid(row=7)
            self.userScore.append(0)
    def checkAnswer(self):
        if self.bgColor=="#E5E6FF":
            global chosenAnswer
            self.chosenAnswer = self.userEntry.get()
        try:
            if len(self.chosenAnswer) != 0:
                self.accuScore(self.chosenAnswer,self.currentAnswer)
                self.submitBtn.grid_remove()
                global nextQBtn
                if int(self.questions.index(self.currentQuestion)+1) != len(self.questions):
                    self.nextQBtnText="Next Question" 
                else: 
                    self.nextQBtnText="Finish Quiz"
                self.nextQBtn = Button(quizWindow,text=self.nextQBtnText,command= self.nextQuestion,relief=FLAT,font="Arial 18 bold",fg="white",bg=self.fgColor,pady=3,padx=5)###
                self.nextQBtn.grid(row=9)
            else:
                    messagebox.showerror(title="No User Input",message="Please answer the question!")
        except AttributeError:
            messagebox.showerror(title="No User Input",message="Please answer the question!")
        self.infoBar = Label(quizWindow,padx=30,pady=15,font="Arial 16 bold",text="Question Number: "+str((self.questions.index(self.currentQuestion))+1)+"/"+str(len(self.questions))+"             Current Score: "+str(sum(self.userScore))+"/"+str(len(self.questions)), fg="white", bg=self.fgColor)
        self.infoBar.grid(row=3)
    def nextQuestion(self):
        self.nextQBtn.grid_remove()
        self.checkLabel1.grid_remove()
        self.checkLabel2.grid_remove()
        self.afterSubmitLabel.grid_remove()
        if self.bgColor == "#B3FFC1":##20may; since choices are deselected unlike TorF mode
            self.chosenAnswer = ""
        try:
            global currentQuestion
            global currentAnswer
            global currentExplan ##20may
            self.currentQuestion = next(self.iterQuestions)
            self.currentAnswer = next(self.iterAnswers)
            self.currentExplan = next(self.iterExplan)##20may
            self.infoBar = Label(quizWindow,padx=30,pady=15,font="Arial 16 bold",text="Question Number: "+str((self.questions.index(self.currentQuestion))+1)+"/"+str(len(self.questions))+"             Current Score: "+str(sum(self.userScore))+"/"+str(len(self.questions)), fg="white", bg=self.fgColor)
            self.infoBar.grid(row=3)
            if self.questions.index(self.currentQuestion) in range(1,len(self.questions)+1):
                self.displayQuestion=Label(quizWindow,wraplength=450,text=str(self.currentQuestion)+"\n",font="Arial 20 underline",fg=self.fgColor,bg=self.bgColor,padx=100)##20may:add padding
                self.displayQuestion.grid(row=5)
                if self.bgColor == "#B3FFC1":
                    self.MC_currentChoices()
                self.submitBtn.grid(row=10)
        except StopIteration:
            self.timeCommand.append("stop")
            quizWindow.destroy()
            global userScoreWindow
            userScoreWindow = Tk()
            self.userFinalScore = Score(userScoreWindow,self.name,self.age,self.title,self.fgColor,self.bgColor,self.questions,self.answers,self.userScore,self.userFinalTime,self.explanation)##20may:new param
            self.userFinalScore.displayUserScore()
            userScoreWindow.mainloop()
    def userQuizTime(self):
        if "start" in self.timeCommand:
            self.userTimer = Timer(1.0, self.userQuizTime)
            self.userTimer.start()
            self.timeCounter.append(1)
        if "stop" in self.timeCommand:
            self.userTimer.cancel()
        global userFinalTime
        self.userFinalTime = sum(self.timeCounter)
    
