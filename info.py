import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

curversion = "1.0.0"

def openGithub():
    webbrowser.open("https://github.com/JugieNoob/FunkinSaveEditor/releases/latest")
def openTwitter():
    webbrowser.open("https://x.com/JugieNoob")

def loadInfoWindow(event=None):
    infowin = tk.Toplevel()
    infowin.title("Funkin' Save Editor: Information")
    infowin.iconbitmap("images/icon-hole.ico")
    
    canvas = tk.Canvas(infowin, width=370, height=320, bg="White")
    infowin.resizable(False, False)
    
    logo = Image.open("images/icon-hole.png")
    logo = logo.resize(size=(200, 200), resample=Image.Resampling.BILINEAR)
    logo = ImageTk.PhotoImage(logo)
    
    canvas.create_image(370/2, 320/2, image=logo)
    
    namelabel = tk.Label(infowin, text="Funkin' Save Editor", font=("",16),width=65, anchor="center")
    canvas.create_window(175, 15, window=namelabel)
    
    canvas.create_text(175, 40, text=curversion, font=("",10), anchor="center")
    
    githublogo = Image.open("images/github.png")
    githublogo = githublogo.resize(size=(50, 50), resample=Image.Resampling.BILINEAR)
    githublogo = ImageTk.PhotoImage(githublogo)   
    
    githubbtn = tk.Button(infowin, image=githublogo, command=openGithub)
    canvas.create_window(35, 290, window=githubbtn)
    
    twitterlogo = Image.open("images/twitter.png")
    twitterlogo = twitterlogo.resize(size=(50, 50), resample=Image.Resampling.BILINEAR)
    twitterlogo = ImageTk.PhotoImage(twitterlogo)   
    
    twitterbtn = tk.Button(infowin, image=twitterlogo, command=openTwitter)
    canvas.create_window(340, 290, window=twitterbtn)
    
    canvas.pack(side = "top", fill = "both", expand = True)
    infowin.mainloop()