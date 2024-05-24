# How It Works

## FNF Save Data (Pre 0.3.0)
  
  ### Take "y12:Bopeebo-hardi25310" as an example.

  - **y** is the separator character that separates one piece of data from another, sometimes one or two more characters can be found before the separator character such as **"o"**, **"z"** or **"h"**. **(red)**

  - **12** is the length of the songname and the difficulty **(including the - ).** **(orange)**

  - **:** is the character that separates the **y12** data from the rest of the data. **(yellow)**

  - **Bopeebo** is the name of the song that the data belongs to. **(lime)**

  - **-hard** is the difficulty of the song. **(green)**

  - **i** shows that the next piece of data is going to be an integer value. **(blue)**

  - **25310** is the score of the song that you got. **(dark blue)**

  <p align="center">
  <img width="50%" height="50%"  
  src="https://github.com/JugieNoob/FunkinSaveEditor/blob/main/markdownstuff/images/dataexample.png">
  </p>
  
  
  **Font taken from [FNF font (PhantomMuff)](https://gamebanana.com/tools/7763) on GameBanana**

## The Save Editor

  - When a user presses the **Update Save** button, the program starts a process to update the save data with the new data:

  1. The program will translate the raw save data into an array which allows it to be read easily by the program.

  2. The program will check if data exists for the existing song by comparing the inputted data with the data that the program has from the save file.

  3. If the save file doesn't have the song data the program will recreate it and put it into the save file. If it does, then it will replace the song data that is already there.

  4. The program will then translate the save data from the array back into raw data.

  5. Finally, the program will overwrite the save file with a new save file that has the correct data.
