import tkinter as tk
import tkinter.font as tkfont
import filehandler as fh
import tkinter.filedialog as tkfd
import savehandler as sh


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

def createText(x:int, y:int, text:str):
    text = tk.Label(window, text=text, font=("VCR",16), anchor="w", width=15)
    canvas.create_window(x + 95, y,window=text)

def updateDirInfo(info):
    text = tk.Label(window, text="Directory:", font=("VCR",8), anchor="w", width=10)
    dirinfo = tk.Entry(window,font=("VCR",8),width=96, background="GRAY")
    dirinfo.insert(tk.INSERT, info)
    canvas.create_window(350,25,window=dirinfo)
    canvas.create_window(35, 25, window=text)
    
    
    
updateDirInfo("")   
def loadRawData():

    filetypes = [("FNF Save File", "*.sol"), ("All Files", "*")]
    global rawdata 
    rawdata = tkfd.askopenfile(filetypes=filetypes)
    filename = rawdata.name
    rawdata = open(filename, "r")
    rawdata = rawdata.read()
    #Remove all data that starts with zy from rawdata
    #for i in range(0,len(datawithzy)):
    #    if datawithzy[i] in rawdata:
    #        rawdata.remove(datawithzy[i])
    #        datawithzy[i] = "zy" + datawithzy[i]

    sh.fetchSongs(rawdata)
    updateDirInfo(filename)  
    
createText(0, 150, "Song Name:")
createText(0, 200, "Song Difficulty:")
createText(0, 250, "Score:")    



songnameinput = tk.Entry(window)
canvas.create_window(250,150,window=songnameinput)

songdifficultyinput = tk.Entry(window)
canvas.create_window(250,200,window=songdifficultyinput)

songscoreinput = tk.Entry(window)
canvas.create_window(250,250,window=songscoreinput)

songnameinput.insert(0,"Snake Eyes")
songdifficultyinput.insert(0, "hard")



                    
    #Check if songname matches any data in the file
   # if songname in songdata:
    
   # file = open(filename, "a")
    #if in file.read()   
    
dirbtn = tk.Button(window,command=loadRawData,text="Save Directory")
canvas.create_window(500,380, window=dirbtn, width=75, height=50)
    


submitbtn = tk.Button(canvas,command=lambda: sh.updSave(songname=songnameinput.get(), difficulty=songdifficultyinput.get(), score=songscoreinput.get(), savearray=rawdata),text="Update Save")
canvas.create_window(330,380, window=submitbtn, width=150, height=100)






canvas.pack()
window.mainloop()