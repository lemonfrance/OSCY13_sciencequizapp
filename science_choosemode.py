from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from science_quizroutine import Quiz
from science_finalscore import Score 
import science_startmenu

class ModeSelection:
    def __init__(self,name,age,parent):
        global MCQuestions
        global MC_CorrAnswers
        global TorFQuestions
        global TorF_CorrAnswers
        global IDQuestions
        global ID_CorrAnswers
        self.name = name
        self.age = age
        self.parent = parent
        self.parent.geometry("700x875+500+85")
        self.parent.configure(bg="#00EA91",padx=75,pady=75)
        self.parent.title("Science Whizz | "+ self.name)
        self.randomLabel=Label(parent,wraplength=450,text="Science Whizz | "+ self.name,font="Arial 20 bold",fg="#FFFACD",bg="#00EA91",pady=5,padx=5)
        self.randomLabel.pack()
        self.randomLabel=Label(parent,text="Choose your mode:",font="Arial 20 bold",fg="white",bg="#00EA91",pady=5,padx=5)
        self.randomLabel.pack()

        self.randomLabel = Label(parent,text="",font="Arial 15",bg="#00EA91").pack()
        
        self.MCBtn = Button(parent,text="Multiple choices\nSelect one from the provided choices through radio buttons",anchor="w",width=45,wraplength=450,font="Arial 15 bold",bg="#B3FFC1",fg="#009A46",pady=15,padx=15,relief=FLAT,justify="left",command=self.MCcommand)
        self.MCBtn.pack()

        self.randomLabel = Label(parent,text="",font="Arial 15",bg="#00EA91").pack()
        
        self.TorFBtn = Button(parent,text="True or False\nDetermine whether the statement provided is right or wrong",anchor="w",width=45,wraplength=450,font="Arial 15 bold",bg="#BEF6FE",fg="#009A46",pady=15,padx=15,relief=FLAT,justify="left",command=self.TorFcommand)
        self.TorFBtn.pack()

        self.randomLabel = Label(parent,text="",font="Arial 15",bg="#00EA91").pack()
        
        self.IDBtn = Button(parent,text="Identification\nType in your answer in the entry box",font="Arial 15 bold",bg="#E5E6FF",fg="#009A46",anchor="w",width=45,wraplength=450,pady=15,padx=15,relief=FLAT,justify="left",command=self.IDcommand)
        self.IDBtn.pack()

        self.randomLabel = Label(parent,text="",font="Arial 15",bg="#00EA91").pack()

        self.backMainBtn = Button(parent,text="Back to Main Menu",command = lambda:Score.backMain(self,parent=parent),font="Arial 18 bold",fg="white",bg="#00C479",relief=FLAT,pady=3,padx=5)
        self.backMainBtn.pack()

        self.randomLabel = Label(parent,text="",font="Arial 15",bg="#00EA91").pack()
        
        self.separator = Frame(parent,height=2,relief=SOLID,bg="white")
        self.separator.pack(fill=X,padx=10,pady=10)
        self.randomLabel = Label(parent, text="Created by Franz Naling (2018)",font="Arial 14 bold",fg="white",bg="#00EA91",pady=5,padx=5).pack()
        
        ### 20 may: added extra explanations to display every time answer is submitted, changed questions, answers and choices.

        #Multiple Choice
        self.MCQuestions = [
            "What is the right term to describe an animal that carries two identical alleles?",
            "Which of the following pairs can produce a homozygous dominant offspring?",
            "These alleles are only observable physically when two of them are present.",
            "Among the following radiations, which one is the most dangerous?",
            "What type of energy is released in an exothermic reaction?"]   
        self.MC_CorrAnswers = [
            "Homozygous",
            "Two heterozygous individuals",
            "Recessive alleles",
            "Gamma radiation",
            "Heat Energy"]
        self.MCexplan = [
            "The term 'homozygous' describes individuals who carry two of the same allele, be it a dominant or recessive allele.",
            "A homozygous dominant offspring can only be produced if both parents have at least one dominant allele.",
            "When an individual is heterozygous, the observable effect of the recessive allele is “masked” by the dominant allele. Therefore, the effect of the recessive allele can only be physically dominant when the only alleles present are recessive alleles and there are no dominant alleles present.",
            "Gamma rays have no mass or charge, so it can penetrate and pass through anything, making it dangerous. Alpha radiation is the least dangerous as it can be absorbed easily.",
            "The energy difference between the reactants and products in an exothermic reaction is released as heat energy."]

        #True or False
        self.TorFQuestions = [
            "The phenotype is the physical representation of an individual’s genotype.",
            "A homozygous recessive individual and a homozygous dominant individual has a 100% chance of producing heterozygous offspring.",
            "An exothermic reaction absorbs heat.",
            "Alpha particles consist of two protons and two neutrons.",
            "If the object is placed in front of a concave mirror and if it is located at the focal point, it will produce an real, upright images."]
        self.TorF_CorrAnswers = [
            "True",
            "True",
            "False",
            "True",
            "False"]
        self.TorFexplan = [
            "The phenotype is the physical characteristics and trait that can be observed on an individual due to its genetic makeup.",
            "If you plot these genotypes on a Punnett square, the results are all heterozygous offspring.",
            "Endothermic reactions absorb heat while exothermic reactions releases heat.",
            "Alpha particles have helium nuclei; they have two protons and two neutrons.",
            "If the object is placed in front of a concave mirror and if it is located at the focal point, no image will be produced."]

        #Identification
        self.IDQuestions = [
            "Brown eyes are caused by the dominant allele B, while blue eyes are caused by the recessive allele b. What would be the colour of the eyes of an individual with the genotype Bb?",
            "What is the rate of change in velocity over time, but with decreasing speed and going to the opposite direction?",
            "The amount of matter in an object; it is measured in kilograms (kg). It does not change even if you change its location.",
            "It is the measurement of how far the object’s starting point from which the object has travelled is from the end point.",
            "It is the process of gaining a positive/negative charge by losing/gaining electrons."]
        self.ID_CorrAnswers = [
            "Brown",
            "Deceleration",
            "Mass",
            "Displacement",
            "Ionisation"]
        self.IDexplan = [
            "Heterozygous individuals (Bb) still exhibit the same characteristics as homozygous dominant individuals (BB, brown-eyed) since the dominant allele “masks” the effect of the recessive allele. To have blue eyes, one must have two recessive alleles i.e. one must be homozygous recessive.",
            "The increasing rate of change in velocity over time is acceleration, but when speed is decreasing, and the object goes the opposite direction, it is called deceleration.",
            "Mass is the amount of matter in an object and is measured in kilograms. Weight, on the other hand, is the amount of force acting on an object due to gravitational force, and it is measured in Newtons.",
            "Distance measures how far an object travelled while displacement measures how far the starting point of the object’s path is from the ending point.",
            "Ionisation is the process of gaining a positive/negative charge by losing/gaining electrons."]
        ###
    def MCcommand(self):
        global modeTitle
        global modeBG
        global modeFG
        self.parent.destroy()
        self.modeTitle = "Science Whizz | "+self.name+" \n Multiple Choice"
        self.modeBG = "#B3FFC1"
        self.modeFG = "#00B0F0" 
        self.MCset = Quiz(self.name,self.age,self.modeTitle, self.modeFG, self.modeBG, self.MCQuestions, self.MC_CorrAnswers,self.MCexplan)
        self.MCset.quizRoutine()        
    def TorFcommand(self):
        global modeTitle
        global modeBG
        global modeFG
        self.parent.destroy()
        self.modeTitle = "Science Whizz | "+self.name+" \n True or False"
        self.modeBG = "#BEF6FE"
        self.modeFG = "#00C085"
        self.TorFset = Quiz(self.name,self.age,self.modeTitle, self.modeFG, self.modeBG, self.TorFQuestions, self.TorF_CorrAnswers,self.TorFexplan)
        self.TorFset.quizRoutine()
    def IDcommand(self):
        global modeTitle
        global modeBG
        global modeFG
        self.parent.destroy()
        self.modeTitle = "Science Whizz | "+self.name+" \n Identification"
        self.modeBG = "#E5E6FF" 
        self.modeFG = "#03C19F"
        self.IDset = Quiz(self.name,self.age,self.modeTitle, self.modeFG, self.modeBG, self.IDQuestions, self.ID_CorrAnswers, self.IDexplan)
        self.IDset.quizRoutine()
