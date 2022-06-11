from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download =0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value'] +=(speed/GB)*100
        download +=1
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" tasks completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=500)
bar.pack(pady=10)

percentlabel = Label(window,textvariable=percent).pack()
textlabel = Label(window, textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()
