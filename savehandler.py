import re

datawithzy = []
datawithy = []
savedata = []


def updatefile(rawdata):
    file = open(datadir, "w")
    file.write(rawdata)
    file.close()
    print("Successfully wrote to " + datadir)

def translateArraytoSave(savedata):
    rawdata = ""
    for i in range(0,len(savedata)):
        rawdata = rawdata + savedata[i]
        
    updatefile(rawdata)

def translateSaveToArray(rawdata):
    
    regex = "[z][ozh]y\d{1,2}:|[ozh]y\d{1,2}:|y\d{1,2}:"
    prefixarray = re.findall(regex, rawdata)
    
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
    print(songdata)
    
    #Check the position of the song data
    for i in range(0, len(translateSaveToArray(savearray))):
        if translateSaveToArray(savearray)[i].startswith(songdata):
            print("Found a match!")
            indexofsongdata = i
            overwriteSongData(songdata, score, translateSaveToArray(savearray), indexofsongdata)
            break
        else:
            print("Could not find a matching song!\nCreating new data...")
            
def overwriteSongData(songdata, score, savearray, index):
    savearray[index] = songdata + score
    translateArraytoSave(savearray)

def addToSongScore(songdata, score, savearray, index):
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

def fetchSongs(rawdata):
    songScoreindex = 0
    translateSaveToArray(rawdata)
    

    for i in range(0, len(savedata)):
        if savedata[i].endswith("songScoresb"):
            songScoreindex = i
            break
    for i in range(songScoreindex, len(savedata)):
        if not savedata[i].startswith("zhy"):
            print(savedata[i])
        else:
            break