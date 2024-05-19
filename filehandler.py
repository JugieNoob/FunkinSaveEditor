import tkinter.filedialog as tkfd



filename = "No directory"

def loadRawData():

    #rawdata = "oy6:memoryfy12:middleScrollfy4:dfjkfy12:hasgenocidedfy8:boneshiti5y8:hudalphai1y11:accuracyModi1y15:accuracyDisplayty9:givenCodefy8:newInputty14:attackLeftBindy5:SHIFTy11:secretCharsafttttttthy10:gpleftBindy9:DPAD_LEFTy6:gjUsery9:JugieNooby5:ghostty10:brightnesszy15:attackRightBindR11y10:npsDisplayfy10:colorblindzy9:cpuStrumsfy13:gpatkLeftBindy12:LEFT_TRIGGERy6:offsetzy10:songScoresby15:Bonedoggle-hardzy14:Satanic-Funkinzy10:week1-easyzy10:week0-easyzy23:Technicolor-Tussle-hardi176862y18:Technicolor-Tusslezy14:Last-Reel-hardi191887y19:Satanic-Funkin-hardzy20:imminent-demise-hardi134287y15:Snake-Eyes-hardi129312y12:Whoopee-hardi134825y17:Terrible-Sin-hardi149162y10:week2-hardzy18:Final-Stretch-hardi185938y8:Knockoutzy16:Sansational-hardi190187y10:week1-hardi314912y10:week0-hardi306174y5:week0zy5:week1zy11:Sansationalzy13:Knockout-hardi256325y13:Final-Stretchzy5:week2zy10:Snake-Eyeszy7:Whoopeezhy7:gjTokeny6:47de7cy9:hitsoundsfy12:laneUnderlayfy7:versionzy4:mutefy10:songCombosbR27y0:R28R60R31y4:SDCBR32R60R33R61R34R60R37R61R36y2:FCR35R61R38R60R41R60R40R60y18:Nightmare-Run-hardR60R42R61R47R60y20:Burning-In-Hell-hardR60R49R60R48R61R52R60R51R60hy6:volumed1.38777878078145e-16y8:optimizefy7:fpsRainfy11:highqualityty12:songPositionty11:scoreScreenty10:focuspausety12:mechanicTypei1y11:seenCreditsfy10:cachestartty8:gpupBindy7:DPAD_UPy11:resetButtonfy11:memorycachety7:camzoomty6:showmsfy8:leftBindy1:Ay14:photosensitivefy16:laneTransparencyd0.5y17:sanessDeathQuoteszy6:framesi10y7:inkshiti12y5:gammai1y15:watchedTitleVidty9:inputShowfy11:shownalertsatffhy10:gpdownBindy9:DPAD_DOWNy3:fpsfy6:fpsCapi120y14:gpatkRightBindy13:RIGHT_TRIGGERy14:freeplaylockedaffthy11:gpdodgeBindR82y13:despairdeathszy5:mutedty10:resolutioni6y15:customStrumLinezy11:focusfreezefy10:downscrollfy8:showsubsfy11:gprightBindy10:DPAD_RIGHTy11:gotSaveDatazy9:dodgeBindy5:SPACEy13:haspacifistedty9:weeksbeatattfhy17:achievementsIndieau148396ffffftfu2ftnfffnfu9fu9338ffu464fhy6:upBindy1:Wy9:rightBindy1:Dy11:changedHitXi-1y11:changedHitYi-1y3:huhty7:botplayfy9:strumlinefy15:weeksbeatonhardattfhy8:downBindy1:Sy10:changedHitfg"
    #rawdata = open("", "r")
    #savearray = rawdata.split(":")
    filetypes = [("FNF Save File", "*.sol"), ("All Files", "*")]
    rawdata = tkfd.askopenfile(filetypes=filetypes)
    filename = rawdata.name
    savearray = rawdata.read().split(":")
    print(savearray)
    from main import updateDirInfo
    updateDirInfo(filename)
