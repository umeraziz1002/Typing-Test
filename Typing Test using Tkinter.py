from tkinter import *
import threading
from Texts import text_list
import time
import math
import random

root = Tk()

time_limit = 30
total_words = 0
etime = 0
etime_in_minute = 0
wpm = 0
accuracy = 0 
gross_wpm = 0
remaining_time = time_limit

def start_time():
    global etime
    for ttime in range(1,time_limit+1):
        etime = ttime
        label_timer["text"] = etime
        remaining_time = time_limit - etime
        label_remaintime['text'] = remaining_time
        time.sleep(1)
    else:
        entry.config(state="disabled")
        btn_reset.config(state="normal")


def check():
    global total_words
    global etime
    global etime_in_minute

    entry.config(state="normal")
    btn_start.config(state="disabled")
    mistakes = 0
    para_words = label_paragraph['text'].split()
    while etime!=time_limit:
        enteredParagraph = entry.get(1.0,'end-1c').split()
        total_words = len(enteredParagraph)

    
    s = list(zip(para_words,enteredParagraph))
    for pair in s:
        if pair[0] != pair[1]:
            mistakes +=1

    etime_in_minute = etime /60
    correct_words = total_words - mistakes
    wpm = (total_words - mistakes) / etime_in_minute
    gross_wpm = total_words/etime_in_minute
    accuracy = (wpm/gross_wpm)*100
    accuracy= math.floor(accuracy)
    label_wpm["text"] = wpm
    label_accuracy['text'] = accuracy
    label_correct_words['text'] = correct_words
    label_wrong_words['text'] = mistakes


def start():
    tr_1=threading.Thread(target=start_time)
    tr_1.start()
    tr = threading.Thread(target=check)
    tr.start()

def stop():
    pass

def reset():
    global remaining_Time
    global elpasedTime

    btn_reset.config(state='disabled')
    btn_start.config(state='normal')
    
    entry.config(state='normal')
    entry.delete(1.0,END)
    entry.config(state='disabled')

    remaining_Time = time_limit
    elpasedTime = 0

    selected_para = random.choice(paragraphs_list)
    label_paragraph['text'] = selected_para
    label_timer['text'] = 0
    label_remaintime['text'] = 30
    label_wpm['text'] = 0
    label_accuracy['text'] = 0
    label_correct_words['text'] = 0
    label_wrong_words['text'] = 0



#Typing Window
root.geometry("1200x700")
root.title("Robin Typing Test")

#HEADER
titleframe = Frame(root,height=100,border=9,relief=SUNKEN)
titleframe.propagate(FALSE)
titleframe.pack(fill=X)
Label(titleframe,text="ROBIN TYPING TEST",font=("Cooper Black",30,"italic"),bg="#73FBFD",padx=33,pady=44).pack(fill=BOTH)

#SElected Paragrap
paragraphs_list = text_list()
selected_para = random.choice(paragraphs_list)
label_paragraph = Label(text=selected_para,font=("arial",16),width=60,wraplength=1100,background= "lightgrey",height=7)
label_paragraph.propagate(FALSE)
label_paragraph.pack(fill=X)

#Input typing text Field
entry_frame = Frame(root)
entry_frame.pack(fill=X)
entry = Text(entry_frame,height=6,border=4,borderwidth=4,font="arial 16")
entry.config(state="disabled")

entry.pack(fill=X,padx=50,pady=50)

#RESULT
summary = Frame(root,relief=SUNKEN,border=7,bg="#73FBFD",height=210,padx=33,pady=33)
summary.propagate(FALSE)
summary.pack(fill=BOTH)

btn_start = Button(summary,text="Start",command=start,width=10,height=2,background="red",foreground="white",font="arial 15 bold")
btn_start.grid(row=0,column=0,padx=10)

btn_reset = Button(summary,text="Reset",command=reset,width=10,height=2,background="red",foreground="white",font="arial 15 bold")
btn_reset.grid(row=0,column=2,padx=10)

result = Frame(summary,bg="#73FBFD")
result.grid(row=0,column=3,padx=5)

Label(result,text="WPM",font="arial 16 bold",bg="#73FBFD",fg="black",width=6,borderwidth=3,relief=SOLID).grid(row=0,column=0)
label_wpm = Label(result,text="0",width=11,height=3,bg="#73FBFD",fg="black",borderwidth=4)
label_wpm.grid(row=1,column=0,padx=10)

Label(result,text="Accuracy",font="arial 16 bold",bg="#73FBFD",fg="black",borderwidth=3,relief=SOLID).grid(row=0,column=1,padx=10)
label_accuracy = Label(result,text="0",width=13,height=3,bg="#73FBFD",fg="black")
label_accuracy.grid(row=1,column=1,padx=10)

Label(result,text="Timer",font="arial 16 bold",bg="#73FBFD",fg="black",borderwidth=3,relief=SOLID).grid(row=0,column=2,padx=10)
label_timer = Label(result,text="0",width=10,height=3,bg="#73FBFD",fg="black")
label_timer.grid(row=1,column=2,padx=10)

Label(result,text="Remaining Time",font="arial 16 bold",bg="#73FBFD",fg="black",borderwidth=3,relief=SOLID).grid(row=0,column=3,padx=5)
label_remaintime = Label(result,text="30",width=10,height=3,bg="#73FBFD",fg="black")
label_remaintime.grid(row=1,column=3,padx=10)


Label(result,text="Correct Words",font="arial 16 bold",bg="#73FBFD",fg="black",borderwidth=3,relief=SOLID).grid(row=0,column=4,padx=5)
label_correct_words = Label(result,text="0",width=10,height=3,bg="#73FBFD",fg="black")
label_correct_words.grid(row=1,column=4,padx=10)


Label(result,text="Wrong Words",font="arial 16 bold",bg="#73FBFD",fg="black",borderwidth=3,relief=SOLID).grid(row=0,column=5)
label_wrong_words = Label(result,text="0",width=10,height=3,bg="#73FBFD",fg="black")
label_wrong_words.grid(row=1,column=5,padx=15)

root.mainloop()