import tkinter as tk
import tkinter.font as tkfont
import tkinter.filedialog as tkfd
import savehandler as sh
import re

#TODO: MOVE AWAY FROM USING GRIDS AND USE TKINTER'S GRID SYSTEM https://www.tutorialspoint.com/align-buttons-and-labels-in-each-row-with-tkinter

#Non GUI Variables

songdata = []
tinydata = ""
score = 0
songname = ""
difficulty = ""
filename = "No directory"

window = tk.Tk()
window.resizable(False, False)
window.title("Funkin' Save Editor")
canvas = tk.Canvas(window, width=640, height=480, bg="White")


songnameinput = tk.Entry(window)
canvas.create_window(250,150,window=songnameinput)

songdifficultyinput = tk.Entry(window)
canvas.create_window(250,200,window=songdifficultyinput)

songscoreinput = tk.Entry(window)
canvas.create_window(250,250,window=songscoreinput)

def createText(x:int, y:int, text:str):
    text = tk.Label(window, text=text, font=("VCR",16), anchor="w", width=15)
    canvas.create_window(x + 95, y,window=text)
    
def splitSongData(songdata):
    regex = "([z]y|y)\d{1,2}:"
    datarray = re.findall(regex, songdata)
    #Get The Name
    
    
    pass

def loadRawData():

    filetypes = [("FNF Save File", "*.sol"), ("All Files", "*")]
    global rawdata 
    global filename
    rawdata = tkfd.askopenfile(filetypes=filetypes)
    filename = rawdata.name
    rawdata = open(filename, "r")
    rawdata = rawdata.read()
    dirinfo.insert(tk.INSERT, filename)
    
    sh.fetchSongs(rawdata , 0)
    print(sh.songScoreindex)
    print(sh.numberofsongs)
    for i in range(sh.songScoreindex + 1, sh.numberofsongs):
        sh.fetchSongs(rawdata , i)
        if sh.fetchSongName[-1].isdigit() and not "week" in sh.fetchSongName:
            listUI.insert(i, sh.fetchSongName)
            

#List of Songs
listUI = tk.Listbox(window, width=35, height=20)
listUI.bind('<Double-Button>', lambda x: splitSongData(listUI.curselection()))
canvas.create_window(535,250,window=listUI)

#Directory UI Stuff
text = tk.Label(window, text="Directory:", font=("VCR",8), anchor="w", width=10)
dirinfo = tk.Entry(window,font=("VCR",8),width=96, background="GRAY")   
dirbtn = tk.Button(window,command=loadRawData,text="...")
canvas.create_window(350,25,window=dirinfo)
canvas.create_window(35, 25, window=text)
canvas.create_window(620,25, window=dirbtn, width=50, height=20)
    
    
#Creating text elements
createText(0, 150, "Song Name:")
createText(0, 200, "Song Difficulty:")
createText(0, 250, "Score:")    


    
submitbtn = tk.Button(canvas,command=lambda: sh.checkIfSongDataExists(songname=songnameinput.get(), difficulty=songdifficultyinput.get(), score=songscoreinput.get(), savearray=rawdata, dir=filename),text="Update Save", font=(16))
canvas.create_window(330,380, window=submitbtn, width=150, height=100)

canvas.pack()
window.mainloop()