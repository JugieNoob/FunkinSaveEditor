# How It Works

## FNF Save Data (Pre 0.3.0)
  
  ### Take "y12:Bopeebo-hardi25310" as an example.

  - **y** is the separator character that separates one piece of data from another, sometimes one or two more characters can be found before the separator character such as **"o"**, **"z"** or **"h"**.

  - **12** is the length of the songname and the difficulty **(including the -).**

  - **:** is the character that separates the **y12** data from the rest of the data.

  - **Bopeebo** is the name of the song that the data belongs to.

  - **-hard** is the difficulty of the song.

  - **i** shows that the next piece of data is going to be an integer value.

  - **25310** is the score of the song that you got.

## The Save Editor

  - When a user presses the **Update Save** button, the program starts a process to update the save data with the new data:

  1. The program will translate the raw save data into an array which allows it to be read easily by the program.

  2. The program will check if data exists for the existing song by comparing the inputted data with the data that the program has from the save file.

  3. If the save file doesn't have the song data the program will recreate it and put it into the save file. If it does, then it will replace the song data that is already there.

  4. The program will then translate the save data from the array back into raw data.

  5. Finally, the program will overwrite the save file with a new save file that has the correct data.