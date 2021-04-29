from tkinter import filedialog
import codecs

import os
from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("1250x950") 
root.configure(bg='palegreen')
root.title("TEXT TO SPEECH")


Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='palegreen').pack()
Label(text ="pnr", font = 'arial 15 bold', bg ='palegreen' , width = '20').pack(side = 'bottom')
Msg = StringVar()
lang = StringVar()
label1=Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='palegreen').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)
label2=Label(root,text ="Enter Language (hindi=hi marathi= mr english =en )", font = 'arial 15 bold', bg ='palegreen').place(x=20,y=140)
entry_field1 = Entry(root, textvariable = lang ,width ='50')
entry_field1.place(x=20,y=180)


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "D:/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    return filename
      
    # Change label contents
   # label_file_explorer.configure(text="File Opened: "+filename)






def Text_to_speech_file():

    lang=entry_field1.get()
    with codecs.open(browseFiles(), encoding='utf-8') as f:
        file=f.read().replace("\n"," ")
    speech = gTTS(text = str(file), lang = lang, slow = False)
    speech.save('speech.mp3')
    playsound('speech.mp3')
    os.remove('speech.mp3')

def Text_to_speech():
    lang=entry_field1.get()
    Message = entry_field.get()
    speech = gTTS(text = entry_field.get(),
                lang = entry_field1.get(), 
                slow = False)
    speech.save('speech.mp3')
    playsound('speech.mp3',True)
    os.remove('speech.mp3')

      
# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="New", command=Text_to_speech_file)
# filemenu.add_separator()

# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)
# editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", command=Text_to_speech_file)

# editmenu.add_separator()
# root.config(menu=menubar)
	

'''label_file_explorer = Label(root,
                            text = "File Explorer using Tkinter",
                            width = 10, height = 2,
                            fg = "blue").place(x=250,y=250)'''


def Exit():
    root.destroy()
    
def Reset():
    Msg.set("")
    os.remove('speech.mp3')
    
def stop():
   # Msg.set("")
    os.stop('speech.mp3')
    
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '6',bg='spring Green').place(x=25,y=220)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '6' , command = Exit, bg = 'Red').place(x=130 , y = 220)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset,bg='salmon').place(x=235 , y = 220)
# button_explore = Button(root,
                        # text = "Browse Files",
                        # command = browseFiles,width = '4').place(x=285,y=260)
Button(root, text = "PLAY_Text File", font = 'arial 15 bold' , command = Text_to_speech_file ,width = '15',bg='gold').place(x=25,y=300)
Button(root, text = "Pause File", font = 'arial 15 bold' , command = stop ,width = '10',bg='turquoise').place(x=235,y=300)
root.mainloop()
# Importing Tkinter module

# from tkinter import *

# def sel():
   # selection = var.get()
   # label.config(text = selection)

# root = Tk()
# var = StringVar()
# var.set("en")
# R1 = Radiobutton(root, text="English", variable=var, value=
# 'en',command=sel)
# R1.pack( anchor = W )

# R2 = Radiobutton(root, text="Hindi", variable=var, value='hi',command=sel)
# R2.pack( anchor = W )

# R3 = Radiobutton(root, text="Marathi", variable=var, value='mr',command=sel)
# R3.pack( anchor = W)

# label = Label(root)
# label.pack()

# print(label.cget("label"))
# root.mainloop()