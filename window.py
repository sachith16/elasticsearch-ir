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
    
    T.config(state=NORMAL)
    T.delete('1.0', END)
    T.config(state=DISABLED)
    
    res=searchq(entry.get())
    global hits
    hits = res['hits']['hits']
    aggs=res['aggregations']
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
        
    Tface.config(state=NORMAL)
    Tface.delete('1.0', END)    
    yy = json.dumps(aggs)
    zz = json.loads(yy)
    
    Tface.insert(tk.END, "Artists\n")
    for f in zz["Artist"]["buckets"]:
        Tface.insert(tk.END, f["key"]+"-"+str(f["doc_count"])+'\n')
        
    Tface.insert(tk.END, "\nLyricists\n")
    for f in zz["Lyricist"]["buckets"]:
        Tface.insert(tk.END, f["key"]+"-"+str(f["doc_count"])+'\n')

    Tface.insert(tk.END, "\nMusicians\n")
    for f in zz["Music"]["buckets"]:
        Tface.insert(tk.END, f["key"]+"-"+str(f["doc_count"])+'\n')

    Tface.config(state=DISABLED)
    
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

listbox = Listbox(root, width=100, height=7)
listbox.bind("<Double-Button-1>", OnDouble)
listbox.pack(pady=10)

Tface = tk.Text(root, height=5, width=70)
Tface.pack()

T = tk.Text(root, height=15, width=70)
T.pack(padx=20,pady=10)
