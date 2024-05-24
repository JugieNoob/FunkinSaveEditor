import tkinter as tk
import tkinter.filedialog as tkfd
import savehandler as sh
import updater
import info
import exehelper as exe

#TODO: MOVE AWAY FROM USING GRIDS AND USE TKINTER'S GRID SYSTEM https://www.tutorialspoint.com/align-buttons-and-labels-in-each-row-with-tkinter

#Non GUI Variables

songdata = []
tinydata = ""
score = 0
songname = ""
difficulty = ""
filename = "No directory"

window = tk.Tk()
window.iconbitmap(exe.resource_path("icon-hole.ico"))
window.resizable(False, False)
window.title("Funkin' Save Editor")
canvas = tk.Canvas(window, width=640, height=480, bg="White")


songnameinput = tk.Entry(window)
canvas.create_window(250,150,window=songnameinput, height=29)

songdifficultyinput = tk.Entry(window)
canvas.create_window(250,200,window=songdifficultyinput, height=29)

songscoreinput = tk.Entry(window)
canvas.create_window(250,250,window=songscoreinput, height=29)


submitbtn = tk.Button(canvas,command=lambda: sh.checkIfSongDataExists(songname=songnameinput.get(), difficulty=songdifficultyinput.get(), score=songscoreinput.get(), savearray=rawdata, dir=filename),text="Update Save", font=(16), state="disabled")
canvas.create_window(330,380, window=submitbtn, width=150, height=100)

def createText(x:int, y:int, text:str):
    text = tk.Label(window, text=text, font=("",16), anchor="w", width=15)
    canvas.create_window(x + 95, y,window=text)
    
def splitSongData(songdata):
    fetchedScore = ""
    fetchedDiff = ""
    fetchedName = ""
    
    #Clearing any inputted values
    songnameinput.delete(0, tk.END)
    songdifficultyinput.delete(0, tk.END)
    songscoreinput.delete(0, tk.END)
    
    
    #Get The Score
    for i in range(1, len(songdata)):
        if songdata[-i].isdigit():
            fetchedScore = fetchedScore + songdata[-i]    
        else:
            fetchedScore = fetchedScore[::-1]
            songdata = songdata.replace("i" + fetchedScore, "")
            break
    #Get the Difficulty
    for i in range(1, len(songdata)):
        if songdata[-i] != "-":
            fetchedDiff = fetchedDiff + songdata[-i]
        else:
            fetchedDiff = fetchedDiff[::-1]
            songdata = songdata.replace("-" + fetchedDiff, "")
            break
    #Get the Song Name
    for i in range(1, len(songdata)):
        if songdata[-i] != ":":
            fetchedName = fetchedName + songdata[-i]
        else:
            fetchedName = fetchedName[::-1]
            songdata = songdata.replace(fetchedName, "")
            break    
    
    songnameinput.insert(tk.INSERT, fetchedName)
    songdifficultyinput.insert(tk.INSERT, fetchedDiff)
    songscoreinput.insert(tk.INSERT, fetchedScore)
    

def loadRawData():

    filetypes = [("FNF Save File", "*.sol"), ("All Files", "*")]
    global rawdata 
    global filename
    rawdata = tkfd.askopenfile(filetypes=filetypes)
    filename = rawdata.name
    rawdata = open(filename, "r")
    rawdata = rawdata.read()
    dirinfo.delete(0, tk.END)
    songListUI.delete(0, tk.END)
    dirinfo.insert(tk.INSERT, filename)
    
    
    sh.fetchSongs(rawdata , 0)
    for i in range(sh.songScoreindex + 1, sh.numberofsongs):
        sh.fetchSongs(rawdata , i)
        if sh.fetchSongName[-1].isdigit() and not "week" in sh.fetchSongName:
            songListUI.insert(i, sh.fetchSongName)
    
    submitbtn.config(state="active")        
            

#List of Songs
songListUI = tk.Listbox(window, width=35, height=20)
songListUI.bind('<Double-Button>', lambda x: splitSongData(songListUI.get(songListUI.curselection())))
canvas.create_window(535,250,window=songListUI)

#Directory UI Stuff
text = tk.Label(window, text="Directory:", font=("VCR",8), anchor="w", width=10)
dirinfo = tk.Entry(window,font=("VCR",8),width=96, background="GRAY")   
dirbtn = tk.Button(window,command=loadRawData,text="...")
canvas.create_window(350,8,window=dirinfo)
canvas.create_window(35, 8, window=text)
canvas.create_window(620,8, window=dirbtn, width=50, height=20)
    
    
#Creating text elements
createText(0, 150, "Song Name:")
createText(0, 200, "Song Difficulty:")
createText(0, 250, "Score:")    

menuBar =  tk.Menu()
helpMenu = tk.Menu(menuBar, tearoff=False)
helpMenu.add_command(label="Info", accelerator="F1", command=info.loadInfoWindow)

updatesMenu = tk.Menu(menuBar, tearoff=False)
updatesMenu.add_command(label="Check For Updates", command=updater.checkforupdates)

menuBar.add_cascade(menu=updatesMenu, label="Tools")
menuBar.add_cascade(menu=helpMenu, label="Help")
    


canvas.pack()
window.bind_all("<F1>", info.loadInfoWindow)
window.config(menu=menuBar)
window.mainloop()