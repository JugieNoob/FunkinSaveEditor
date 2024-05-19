import tkinter as tk
import tkinter.font as tkfont
import filehandler as fh


#TODO: MOVE AWAY FROM USING GRIDS AND USE TKINTER'S GRID SYSTEM https://www.tutorialspoint.com/align-buttons-and-labels-in-each-row-with-tkinter

#Non GUI Variables

savearray = []
songdata = []
tinydata = ""
score = 0
songname = ""
difficulty = ""

def main():
    window = tk.Tk()
    window.resizable(False, False)
    window.title("Funkin' Save Editor")
    canvas = tk.Canvas(window, width=640, height=480, bg="White")
    
def createText(x:int, y:int, text:str):
    text = tk.Label(window, text=text, font=("VCR",16), anchor="w", width=15)
    canvas.create_window(x + 95, y,window=text)


createText(0, 150, "Song Name:")
createText(0, 200, "Song Difficulty:")
createText(0, 250, "Score:")


def updateDirInfo(info):
    dirinfo = tk.Label(window, text="Current Directory" + info, font=("VCR",16), anchor="w", width=15)
    canvas.create_window(10, 10,window=dirinfo)

updateDirInfo(fh.loadRawData())

songnameinput = tk.Entry(window)
canvas.create_window(250,150,window=songnameinput)

songdifficultyinput = tk.Entry(window)
canvas.create_window(250,200,window=songdifficultyinput)

scoreinput = tk.Entry(window)
canvas.create_window(250,250,window=scoreinput)

songnameinput.insert(0,"Snake Eyes")
songdifficultyinput.insert(0, "hard")


def updSave():
    #Add Song to the data
    songname = songnameinput.get()
    if " " in songname: 
        snarray = songname.split(" ")
        songname = ""
        for i in range(0, len(snarray)):
            word = snarray[i].capitalize()
            songname = songname + "-" + word
            
    songname = songname.lstrip("-")
    
    #Add Difficulty and "i" to the data (no idea why "i" is needed here)
    
    difficulty = songdifficultyinput.get()
    finaldata = songname + "-" + difficulty + "i"
    
    
    #Add Score to the data
    score = scoreinput.get()
    
    #Get the songdata from savefile

    for i in range(0, len(savearray)):
        if (savearray[i].startswith(finaldata)):
            songdata = savearray[i]
            
            #Gets the final numbers of the data that distinguishes the data Example: Bopeebo-hardi25310y5 (in this case we will just get the 5)
    for i in range(1, len(songdata)):
                if songdata[-i].isdigit():
                    tinydata = tinydata + songdata[-i]
                if not songdata[-i].isdigit():
                    tinydata = "y" + tinydata[::-1]
                    finaldata = finaldata + score + tinydata    
                    print(finaldata)
                    break
    
submitbtn = tk.Button(window,command=updSave,text="Update Save")
canvas.create_window(330,380, window=submitbtn, width=150, height=100)


dirbtn = tk.Button(window,command=fh.loadRawData,text="Save Directory")
canvas.create_window(500,380, window=dirbtn, width=75, height=50)



canvas.pack()
window.mainloop()

