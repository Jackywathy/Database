import Database as base
from tkinter import *
import string
database = base.Database()
# initatve variables



#
def close(event):
    root.quit()

def clear_content():
    global content
    content.pack_forget()
    content.pack()

def read_date1(*args):
    global date1
    global date1_frame
    global date1_error
    global dateitem

    date1 = date1In.get()
    stripped = date1
    if stripped:
        for i in string.punctuation:
            stripped = stripped.replace(i,'')

        print(stripped)
        if len(stripped) == 4:
            dateitem = (int(stripped[:2]),int(stripped[2:]))
        elif len(stripped) == 6:
            dateitem = (int(stripped[:2]), int(stripped[2:4]),int('20' + stripped[4:]))
        elif len(stripped) == 8:
            dateitem = (int(stripped[:2]), int(stripped[2:4]),int(stripped[4:]))

        else:
            date1_error = Button(date1_frame, text="Error-Length wrong", command=lambda: date1_error.grid_forget())
            date1_error.grid(row=2)
    try:
        print(dateitem)
    except:
        pass




def find():
    findFrame.pack()
    addFrame.pack_forget()
    clear_content()

def bind_all(event):
    read_date1()
    read_money()

def new():
    global date1In
    global date1_frame
    global date_label
    global dateLabel
    global moneyframe

    print('newhere')
    addFrame.pack()
    findFrame.pack_forget()

    clear_content()

    date1_frame.pack()
    moneyframe.pack()
    infoframe.pack()
    root.bind('<Return>', bind_all)







def sel():
    pass

def start_buy():
    global isbuy
    isbuy.set('Buy Order')
    print(isbuy)

def start_sell():
    global isbuy
    isbuy.set('Sell Order')
    print(isbuy)



root = Tk()
isbuy = StringVar()
isbuy.set('Buy Order')


# buy = True, sell = False

root.minsize(width=600,height=500)
root.maxsize(width=600,height=500)


content = Frame(root)



#############################################################
# top from containing find/new - always on!
topframe = Frame(root)
topframe.pack()
#buttons
tf1 = Button(topframe, text="FIND IN DATABASE",command=find)
tf1.grid(row=0)
tf2 = Button(topframe, text="ADD NEW",command=new)
tf2.grid(row=0,column=1)
#############################################################

###########################################################
# Frame for buy sell
addFrame = Frame(root)
buy_sell = IntVar()
R1 = Radiobutton(addFrame, text="BUY", variable=buy_sell, value=0, command=start_buy)
R1.grid(row=0)
R2 = Radiobutton(addFrame, text="SELL", variable=buy_sell, value=1,command=start_sell)
R2.grid(row=0,column=1)
#############################################################

#############################################################
# DATE ENTRY
# init the Frame
date1_frame = Frame(content)
# first label
date_label = Label(date1_frame, text='DATE', justify=CENTER)
date_label.grid(row=0)
# date entry
date1In = Entry(date1_frame)
date1In.grid(row=1,column=0)
# date entry button
date1Button = Button(date1_frame, text = 'Enter', width = 20, command = read_date1)
date1Button.grid(row=1,column=1)
##############################################################
def read_money():
    global moneyframe
    global moneyIn
    global money_error
    global moneyitem
    val = moneyIn.get()
    for i in string.punctuation:
        val = val.replace(i,'')

    if val:
        if int(val) < 0:
            money_error = Button(date1_frame, text="Error-Enter Absolute Values", command=lambda: money_error.grid_forget())
            money_error.grid(row=2)
        else:
            moneyitem = (isbuy.get(), int(val))

        print(moneyitem)


#############################################################
# frame containing asking for money
moneyframe = Frame(content)
#first label
money_label = Label(moneyframe,text="AMOUNT")
money_label.grid(row=0)
#money entry
moneyIn = Entry(moneyframe)
moneyIn.grid(row=1,column=0)
#money entry button
moneyButton = Button(moneyframe, text='Enter', width = 20, command = read_money)
moneyButton.grid(row=1,column = 1)
#############################################################

#############################################################
# frane containing the addition information
infoframe = Frame(content)
# Label

info_label = Label(infoframe, textvariable=isbuy,width=40, font=("Helvetica", 36))
info_label.grid(row=0)

#############################################################




















# frame for retrieving from database
findFrame = Frame(root)
all_buy_sell = IntVar()
F1 = Radiobutton(findFrame, text="ALL", variable=all_buy_sell, value=0, command=sel)
F1.grid(row=0)

F2 = Radiobutton(findFrame, text="BUY", variable=all_buy_sell, value=1,command=sel)
F2.grid(row=0,column=1)

F3 = Radiobutton(findFrame, text="SELL", variable=all_buy_sell, value=2,command=sel)
F3.grid(row=0,column=2)


#Button(root,text='QUIT!', bg='red', command=root.quit).grid(row=2)

root.bind('<Escape>', close)
root.lift ()



root.mainloop()