import re
import tkinter.messagebox as mb


def updatefile(rawdata):
    file = open(datadir, "w")
    file.write(rawdata)
    file.close()
    mb.showinfo("Funkin' Save Editor: Save Data Updated!", "Successfully wrote new save data to " + datadir)

def translateArraytoSave(savedata):
    rawdata = ""
    for i in range(0,len(savedata)):
        rawdata = rawdata + savedata[i]
        
    updatefile(rawdata)

def translateSaveToArray(rawdata):
    
    regex = "[z][ozh]y\d{1,2}:|[ozh]y\d{1,2}:|y\d{1,2}:"
    prefixarray = re.findall(regex, rawdata)
    
    rawdata = checkForSaveProblems(rawdata)
        
    #Split the data into an array
    savedata = rawdata.split(":")
    for i in range(0, len(savedata)):
        savedata[i] = savedata[i] + ":"
    
    #Remove prefix that were split as a suffix.
    for i in range(0, len(prefixarray)):
        if savedata[i].endswith(prefixarray[i]):
            savedata[i] = savedata[i].replace(prefixarray[i], "")
    
    #Perfectly balanced...as all things should be.
    for i in range(0, len(savedata)):
        if "" in savedata:
            savedata.remove("")
    
    #Put the prefixes back to where they belong.
    for i in range(0, len(savedata)):
       savedata[i] = prefixarray[i] + savedata[i]
    
    return savedata


def checkIfSongDataExists(songname, difficulty, score, savearray, dir):
    global datadir
    datadir = dir 
    indexofsongdata = 0    
    
    #Recreate song data 
    if " " in songname: 
        snarray = songname.split(" ")
        songname = ""
        for i in range(0, len(snarray)):
            word = snarray[i].capitalize()
            songname = songname + "-" + word
            
    songname = songname.lstrip("-")
    songinfo = songname + "-" + difficulty
    songdata = "y" + str(len(songinfo)) + ":" + songinfo + "i"
    
    #Check the position of the song data
    for i in range(0, len(translateSaveToArray(savearray))):
        if translateSaveToArray(savearray)[i].startswith(songdata):
            print("Found a match!")
            indexofsongdata = i
            overwriteSongData(songdata, score, translateSaveToArray(savearray), indexofsongdata)
            
            break
        elif i + 1== len(translateSaveToArray(savearray)):
            print("Could not find a matching song!\nCreating new data...")
            addToSongScore(songdata, translateSaveToArray(savearray))
            
def overwriteSongData(songdata, score, savearray, index):
    savearray[index] = songdata + score
    translateArraytoSave(savearray)

def addToSongScore(songdata, savearray):
    for i in range(0, len(savearray)):
        if savearray[i].endswith("songScoresb"):
            songScoreindex = i
            break
    savearray.insert(songScoreindex + 1, songdata)
    
    translateArraytoSave(savearray)
    pass
            
def createSongData(songname, difficulty, score, savearray):
    #Add Song to the data
    if " " in songname: 
        snarray = songname.split(" ")
        songname = ""
        for i in range(0, len(snarray)):
            word = snarray[i].capitalize()
            songname = songname + "-" + word
            
    songname = songname.lstrip("-")

    finaldata = songname + "-" + difficulty
    
    #Reconstruct the song data
    finaldata = "y" + str(len(finaldata)) + ":" + finaldata + "i" + score


    print("\nSong Name: " + songname)
    print("Difficulty: " + difficulty)
    print("Score: " + score)
    print("\nFinal Data: " + finaldata)

    addToSongScore(finaldata, savearray)

def fetchSongs(rawdata, index):
    global songScoreindex
    global fetchSongName
    global numberofsongs
    numberofsongs = len(translateSaveToArray(rawdata))
    for i in range(0, len(translateSaveToArray(rawdata))):
        if translateSaveToArray(rawdata)[i].endswith("songScoresb"):
            songScoreindex = i
            break
    for i in range(songScoreindex, len(translateSaveToArray(rawdata))):
        if not translateSaveToArray(rawdata)[i].startswith("zhy"):
            numberofsongs = i
        else:
            break

        
    fetchSongName = translateSaveToArray(rawdata)[index]
    return 
        
def checkForSaveProblems(rawdata):
    if rawdata.endswith(":"):
        rawdata = rawdata[:-1]
        
    return rawdata    



