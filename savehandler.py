import re

datawithzy = []
datawithy = []
savedata = []

def translateSaveToArray(rawdata):
    
    regex = "[z][ozhS]y\d{1,2}:|[ozhS]y\d{1,2}:|y\d{1,2}:"
    prefixarray = re.findall(regex, rawdata)
    
    rawdata = rawdata.split(":")
    for i in range(0, len(prefixarray)):
        rawdata[i] = rawdata[i] + ":"
        if rawdata[i].endswith(prefixarray[i]):
            savedata.append(rawdata[i].replace(prefixarray[i], ""))

    for i in range(0, len(savedata)):
        if "" in savedata:
            savedata.remove("")

    for i in range(0, len(savedata)):
        savedata[i] = prefixarray[i] + savedata[i]
    
    print(savedata)        

def overwritedata(savearray, toreplace, replacewith):
    stitchedstring = ""
    for i in range(0, len(savearray)):
        if savearray[i].startswith(toreplace):
            savearray.remove(savearray[i])
            savearray.append(replacewith)
            
    for i in range(0, len(savearray)):
        
        stitchedstring = stitchedstring + ":" + savearray[i]
        stitchedstring = stitchedstring.lstrip(":")
        
    print(stitchedstring)
    
            
def updSave(songname, difficulty, score, savearray):
    print(savearray)
    #Add Song to the data
    if " " in songname: 
        snarray = songname.split(" ")
        songname = ""
        for i in range(0, len(snarray)):
            word = snarray[i].capitalize()
            songname = songname + "-" + word
            
    songname = songname.lstrip("-")
    print("Song Name: " + songname)
    #Add Difficulty and "i" to the data (no idea why "i" is needed here)
    
    finaldata = songname + "-" + difficulty + "i"
    
    print("Difficulty: " + difficulty)
    #Add Score to the data
    
    print(score)
    #Get the songdata from savefile

    songdata = []
    tinydata = ""
    
    for i in range(0, len(savearray)):
        if (savearray[i].startswith(finaldata)):
            songdata = savearray[i]
            
            #Gets the final numbers of the data that distinguishes the data Example: Bopeebo-hardi25310y5 (in this case we will just get the 5)
    for i in range(1, len(songdata)):
                if songdata[-i].isdigit():
                    tinydata = tinydata + songdata[-i]
                else:
                    tinydata = "y" + tinydata[::-1]
                    finaldata = finaldata + score + tinydata    
                   # print(finaldata)
                    break
                          
    print(finaldata)
    
    overwritedata(savearray=savearray, toreplace=songname+"-"+difficulty, replacewith=finaldata)

#def fetchSongs(savearray):
#    
#    amountofsongs = ""
#    songScores = ""
#    indexofsongScores = 0
#    print("Fetching songs")
#    for i in range(0, len(savearray)):
#        if(savearray[i].startswith("songScores")):
#            #Gets the amount of songs in the save data
#            indexofsongScores = i + 1
#            songScores = savearray[i] 
#            print(songScores)
#            print(indexofsongScores)           
#            for j in range(1, len(songScores)):
#                if(songScores[-j]).isdigit():
#                    amountofsongs = amountofsongs + songScores[-j]
#                else:
#                    print("Found " + amountofsongs[::-1] + " songs!")
#                    amountofsongs = int(amountofsongs[::-1])
#                    break    
#    
#    if songScores != "":
#        for i in range(indexofsongScores, indexofsongScores+amountofsongs):
#            print(savearray[i])
#    else:
#        print("Could not find songs in save data!")

def fetchSongs(rawdata):
    translateSaveToArray(rawdata)