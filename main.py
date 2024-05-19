import tkinter as tk
import tkinter.font as tkfont
import tkinter.filedialog as tkfd

#TODO: MOVE AWAY FROM USING GRIDS AND USE TKINTER'S GRID SYSTEM https://www.tutorialspoint.com/align-buttons-and-labels-in-each-row-with-tkinter

#Non GUI Variables

savearray = []

window = tk.Tk()
window.resizable(False, False)
window.title("Funkin' Save Editor")

canvas = tk.Canvas(window, width=640, height=480, bg="White")

def createText(width:int, height:int, text:str):
    text = tk.Label(canvas, text=text, font=("VCR",16), justify=tk.LEFT)
    #text.grid(column=1, row=1)
    canvas.create_window(width, height,window=text)
    
def loadRawData():
    #rawdata = "oy6:memoryfy12:middleScrollfy4:dfjkfy12:hasgenocidedfy8:boneshiti5y8:hudalphai1y11:accuracyModi1y15:accuracyDisplayty9:givenCodefy8:newInputty14:attackLeftBindy5:SHIFTy11:secretCharsafttttttthy10:gpleftBindy9:DPAD_LEFTy6:gjUsery9:JugieNooby5:ghostty10:brightnesszy15:attackRightBindR11y10:npsDisplayfy10:colorblindzy9:cpuStrumsfy13:gpatkLeftBindy12:LEFT_TRIGGERy6:offsetzy10:songScoresby15:Bonedoggle-hardzy14:Satanic-Funkinzy10:week1-easyzy10:week0-easyzy23:Technicolor-Tussle-hardi176862y18:Technicolor-Tusslezy14:Last-Reel-hardi191887y19:Satanic-Funkin-hardzy20:imminent-demise-hardi134287y15:Snake-Eyes-hardi129312y12:Whoopee-hardi134825y17:Terrible-Sin-hardi149162y10:week2-hardzy18:Final-Stretch-hardi185938y8:Knockoutzy16:Sansational-hardi190187y10:week1-hardi314912y10:week0-hardi306174y5:week0zy5:week1zy11:Sansationalzy13:Knockout-hardi256325y13:Final-Stretchzy5:week2zy10:Snake-Eyeszy7:Whoopeezhy7:gjTokeny6:47de7cy9:hitsoundsfy12:laneUnderlayfy7:versionzy4:mutefy10:songCombosbR27y0:R28R60R31y4:SDCBR32R60R33R61R34R60R37R61R36y2:FCR35R61R38R60R41R60R40R60y18:Nightmare-Run-hardR60R42R61R47R60y20:Burning-In-Hell-hardR60R49R60R48R61R52R60R51R60hy6:volumed1.38777878078145e-16y8:optimizefy7:fpsRainfy11:highqualityty12:songPositionty11:scoreScreenty10:focuspausety12:mechanicTypei1y11:seenCreditsfy10:cachestartty8:gpupBindy7:DPAD_UPy11:resetButtonfy11:memorycachety7:camzoomty6:showmsfy8:leftBindy1:Ay14:photosensitivefy16:laneTransparencyd0.5y17:sanessDeathQuoteszy6:framesi10y7:inkshiti12y5:gammai1y15:watchedTitleVidty9:inputShowfy11:shownalertsatffhy10:gpdownBindy9:DPAD_DOWNy3:fpsfy6:fpsCapi120y14:gpatkRightBindy13:RIGHT_TRIGGERy14:freeplaylockedaffthy11:gpdodgeBindR82y13:despairdeathszy5:mutedty10:resolutioni6y15:customStrumLinezy11:focusfreezefy10:downscrollfy8:showsubsfy11:gprightBindy10:DPAD_RIGHTy11:gotSaveDatazy9:dodgeBindy5:SPACEy13:haspacifistedty9:weeksbeatattfhy17:achievementsIndieau148396ffffftfu2ftnfffnfu9fu9338ffu464fhy6:upBindy1:Wy9:rightBindy1:Dy11:changedHitXi-1y11:changedHitYi-1y3:huhty7:botplayfy9:strumlinefy15:weeksbeatonhardattfhy8:downBindy1:Sy10:changedHitfg"
    #rawdata = open("", "r")
    #savearray = rawdata.split(":")
    filetypes = [("FNF Save File", "*.sol"), ("All Files", "*")]
    
    rawdata = tkfd.askopenfile(filetypes=filetypes)
    savearray = rawdata.read().split(":")
    
    print(savearray)


createText(50, 125, "Song Name:")
createText(50, 175, "Song Difficulty:")
createText(50, 225, "Score:")

songnameinput = tk.Entry(window)
canvas.create_window(400,25,window=songnameinput)

songdifficultyinput = tk.Entry(window)
canvas.create_window(400,75,window=songdifficultyinput)

scoreinput = tk.Entry(window)
canvas.create_window(400,125,window=scoreinput)

songnameinput.insert(0,"Snake Eyes")
songdifficultyinput.insert(0, "hard")




def getInputs():
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
    tinydata = ""
    songdata = []
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
    
submitbtn = tk.Button(canvas,command=getInputs)
canvas.create_window(400,200,width=100, window=submitbtn)


canvas.pack()
window.mainloop()


