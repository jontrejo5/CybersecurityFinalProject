from tkinter import *
from tkinter import Menu
from tkinter import ttk

import portscan

class gui(object):

    # set up main page
    def __init__(self, master):
        self.master = master
        master.title("Jonathan T & Matt S - Advanced Port Scanner")

        self.frame1=Frame(self.master)
        self.frame1.pack(side=TOP, fill=X)

        self.frame2=Frame(self.master)
        self.frame2.pack(side=TOP, fill=X)

        # *****menu setup*****
        self.m=Menu(self.frame1)
        self.master.config(menu=self.m)

        self.submenu=Menu(self.m, tearoff=0)
        self.m.add_cascade(label='File', menu=self.submenu)
        self.submenu.add_command(label='About', command=self.aboutwindow)

        # *****gui elements*****
        self.label=Label(self.frame2, text='Packet Sniffer', height=2)
        self.label.grid(row=3, column=1)

        #create tabs
        self.tab_control = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Port Scanner")
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text="Page 2")
        self.tab_control.pack(expand=1, fill="both")

        # text box label
        self.label1=Label(self.frame1,text='Enter IP Address')
        self.label2=Label(self.frame1,text='Enter start port')
        self.label3=Label(self.frame1,text='Enter end port')

        self.label1.grid(row=4,column=0)
        self.label2.grid(row=5,column=0)
        self.label3.grid(row=6,column=0)

        # text box
        self.entry1=Entry(self.frame1)
        self.entry2=Entry(self.frame1)
        self.entry3=Entry(self.frame1)

        self.entry1.grid(row=4, column=1)
        self.entry2.grid(row=5, column=1)
        self.entry3.grid(row=6, column=1)

        # text area box
        self.textbox=Text(self.tab1)
        self.textbox.grid(row=8, column=0, rowspan=1, columnspan=2)

        # enter button
        self.btn = Button(self.frame1, text='Submit', command=lambda: self.runportscan(self.entry1.get(), self.entry2.get(), self.entry3.get()))
        self.btn.grid(row=7,column=1)

        #then disable the text box to not allow the user to write in it
        #self.textbox.configure(state="disabled")





        # set window size
        self.master.geometry('650x600')

    def valueGET(self, val1, val2, val3):
        print(val1, val2, val3)


    #about information window
    def aboutwindow(self):
        newwin = Toplevel(master=None)
        newwin.geometry("600x100")
        display = Label(newwin, text="About section:")
        display.pack()

    # submit information and run
    def runportscan(self, ipaddr, startport, endport):

        #enable the text box to write into it
        #self.textbox.configure(state='enabled')

        #run port scanner from portscan.py
        result = portscan.runportscan(ipaddr,startport,endport)
        self.textbox.insert(INSERT, result)

        # then disable the text box to not allow the user to write in it
        #self.textbox.configure(state="disabled")



def runwindow():
    root = Tk()
    my_gui = gui(root)
    root.mainloop()
