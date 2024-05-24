import requests
import webbrowser
import info
import tkinter.messagebox as mb
from github import Github

repoPath = "JugieNoob/FunkinSaveEditor"

def checkforupdates():
    github = Github()
    repo = github.get_repo(repoPath)
    latest = repo.get_latest_release()
    if info.curversion != latest.tag_name:
        updatefound = mb.askyesno("Funkin' Save Editor: Update Available!", "A new update was found, do you want to be taken to the GitHub page?")
        if updatefound == True:
            webbrowser.open("https://github.com/JugieNoob/FunkinSaveEditor/releases/latest")
        else:
            print("No")
    else:
        mb.showinfo("Funkin' Save Editor: No Updates", "No updates were found, you are on the latest version.")