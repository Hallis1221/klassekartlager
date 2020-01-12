from tkinter import *
import random
import liste
import mergeFiles
from tkinter import messagebox as mb
#TODO flytte til flere script istendenfor et
x = 0
x2 = 0
pulter = []
window = Tk()
window.state('zoomed')
window.configure(bg='white')
tekstKat = False
tilfeldig = True

def pultTekst():
    global tilfeldig
    mergeFiles.merge()
    pult = 0
    ledigeElever = list(elever)
    ledigeGutter = list(gutter)
    ledigeJenter = list(jenter)
    print(pult)
    def badSolution(value):
        #TODO endre if til switch eller lignende
        #DoDo
        if value == 0:
            nummer = pult0
        elif value == 1:
            nummer = pult1
        elif value == 2:
            nummer = pult2
        elif value == 3:
            nummer = pult3
        elif value == 4:
            nummer = pult4
        elif value == 5:
            nummer = pult5
        elif value == 6:
            nummer = pult6
        elif value ==7:
            nummer = pult7
        elif value == 8:
            nummer = pult8
        elif value == 9:
            nummer = pult9
        elif value == 10:
            nummer = pult10
        elif value == 11:
            nummer = pult11
        elif value == 12:
            nummer = pult12
        elif value == 12:
            nummer = pult12
        elif value == 13:
            nummer = pult13
        elif value == 14:
            nummer = pult14
        elif value == 15:
            nummer = pult15
        elif value == 16:
            nummer = pult16
        elif value == 17:
            nummer = pult17
        elif value == 18:
            nummer = pult18
        else:
            nummer = pult0
        return nummer
    def finnElev(måte):
        global elever
        global gutter
        global jenter
        if måte == "Gutter":
            if len(ledigeGutter) == 0:
                return ""
            elevID = random.randint(0, len(ledigeGutter) - 1)
            elev = ledigeGutter[elevID]
            ledigeGutter.remove(elev)
        elif måte == "Jente":
            if len(ledigeJenter) == 0:
                return ""
            elevID = random.randint(0, len(ledigeJenter) - 1)
            elev = ledigeJenter[elevID]
            ledigeJenter.remove(elev)
        else:
            if len(ledigeElever) == 0:
                return ""
            elevID = random.randint(0, len(ledigeElever) - 1)
            elev = ledigeElever[elevID]
            ledigeElever.remove(elev)
        return elev
    for i in range(len(pulter)):
        pult = badSolution(i)
        print(pult.winfo_width())
        if pult.winfo_width() == 79:
            print("riktig")
            plass1 = Text(pult, width=8, height=1, bg = "black", fg="white")
            plass1.insert(INSERT, finnElev("Tilfeldig"))
            plass1.config(font=("Courier", 10))
            plass1.place(x=7, y=22)
        else:
            print("alternative")
            plass1 = Text(pult, width=8, height=1, bg="black", fg="white")
            if tilfeldig:
                plass1.insert(INSERT, finnElev("Tilfeldig"))
            else:
                plass1.insert(INSERT, finnElev("Gutter"))
            plass1.config(font=("Courier", 10))
            plass1.place(x=7, y=22)

            plass2 = Text(pult, width=8, height=1, bg="black", fg="white")
            if tilfeldig:
                plass2.insert(INSERT, finnElev("Tilfeldig"))
            else:
                plass2.insert(INSERT, finnElev("Jente"))
            plass2.config(font=("Courier", 10))
            plass2.place(x=80, y=22)

def generer():
    #TODO fjern
    print("generer..")
def drag(event):
    event.widget.place(x=event.x_root, y=event.y_root, anchor=CENTER)
def lagPult():
    print(tilfeldig)
    global x
    globals()["pult%s" % x] = Canvas(window, width=150, height=74, bg='black')
    globals()["pult%s" % x].place(x=300, y=600, anchor=CENTER)
    globals()["pult%s" % x].bind("<B1-Motion>", drag)
    globals()["pult%s" % x].pack()
    canID = globals()["pult%s" % x]
    pulter.insert(x, canID)
    x += 1
    return canID
def lagEnkelPult():
    print(tilfeldig)
    global x
    globals()["pult%s" % x] = Canvas(window, width=75, height=50, bg='black')
    globals()["pult%s" % x].place(x=300, y=600, anchor=CENTER)
    globals()["pult%s" % x].bind("<B1-Motion>", drag)
    globals()["pult%s" % x].pack()
    canID = globals()["pult%s" % x]
    pulter.insert(x, canID)
    x += 1
    return canID
def uiStarters():
    kateter = Canvas(window, width=200, height=74, bg='black')
    if tekstKat:
        kateterTekst = Text(kateter, width=8, height=1, bg = "black", fg = "white")
        kateterTekst.insert(INSERT, "Kateter")
        kateterTekst.config(font=("Courier", 25))
        kateterTekst.place(x=15,y=25)
    kateter.place(x=680, y=100, anchor=CENTER)
    kateter.bind("<B1-Motion>")
    ck = Checkbutton(window, text="Gutt og jente", command=checkList)
    bp = Button(window, text="Lag en pult", command=lagPult)
    bpe = Button(window, text="Lag en enkelpult", command=lagEnkelPult)
    bg = Button(window, text="Generer", command=pultTekst)
    blg = Button(window, text="Liste over gutter", command=liste.main_gutter)
    blj = Button(window, text="Liste over jenter", command=liste.main_jenter)
    ba = Button(window, text="Forslag", command=generer)
    bg.place(x=0,y=0)
    bp.place(x=50, y=0)
    ba.place(x=120,y=0)
    blg.place(x=170,y=0)
    blj.place(x=267,y=0)
    bpe.place(x=363,y=0)
    ck.place(x=460,y=0)

def checkList():
    global tilfeldig
    if not tilfeldig:
        tilfeldig = True
    elif tilfeldig:
        tilfeldig = False
    return tilfeldig
with open('elever.txt', 'r') as filehandle:
    elever = []
    number_of_lines = len(open('elever.txt').readlines())
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        elever.append(currentPlace)
with open('gutter.txt', 'r') as filehandle:
    gutter = []
    number_of_lines = len(open('gutter.txt').readlines())
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        gutter.append(currentPlace)
with open('jenter.txt', 'r') as filehandle:
    jenter = []
    number_of_lines = len(open('jenter.txt').readlines())
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]

        # add item to the list
        jenter.append(currentPlace)
def on_closing():
    print("lukket")
    window.quit()
    window.destroy()
    liste.close()

window.protocol("WM_DELETE_WINDOW", on_closing)
uiStarters()
window.mainloop()
print(pulter)