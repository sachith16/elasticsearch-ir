import tkinter as tk;
from tkinter import *
import os
from search import searchq
import json,re

root = tk.Tk()

label_search = tk.Label(text="Enter query here")
label_search.pack(pady=(15,0))
entry = tk.Entry(fg="black", bg="white", width=100)
entry.pack(padx=20, pady=(0,10))

def search():
    #print(entry.get())
    #T.insert(tk.END, "S")
    listbox.delete(0,'end')
    T.delete('1.0', END)
    res=searchq(entry.get())
    global hits
    hits = res['hits']['hits']
    for i in range(len(hits)):
        y = json.dumps(hits[i])
        z=json.loads(y)
        item= z["_source"]["title"]+" -"

        if type(z["_source"]["artist"]) is not str:
            for art in z["_source"]["artist"]:
                item=item+" "+art
        else:
            item=item+" "+z["_source"]["artist"]
            
        listbox.insert(END, item)    

def OnDouble(event):
        T.config(state=NORMAL)
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        #print (selection[0])
        global hits
        y = json.dumps(hits[selection[0]])
        z=json.loads(y)
        T.delete('1.0', END)
        T.insert(tk.END, z["_source"]["title"])
        T.insert(tk.END, "\nLyrics-"+z["_source"]["lyricist"])
        T.insert(tk.END, "\nMusic-"+z["_source"]["music"])
        T.insert(tk.END, '\n\n'+z["_source"]["lyrics"])
        T.config(state=DISABLED)
        

searchbutton = tk.Button(
    text="Search",
    width=5,
    height=1,
    bg="#D8D8D8",
    fg="black",
    command=search
)

searchbutton.pack()

listbox = Listbox(root, width=100, height=10)
listbox.bind("<Double-Button-1>", OnDouble)
listbox.pack(pady=10)

T = tk.Text(root, height=20, width=70)
T.pack(padx=20,pady=10)
