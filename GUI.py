from tkinter import *
from tkinter import Menu
from tkinter import ttk

import sniffer

class GUI(object):

    # set up main page
    def __init__(self, master):
        self.master = master
        master.title("Jonathan T & Matt S Port Scanner")

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

        # text box label
        self.label1=Label(self.frame2,text='Enter IP Address')
        self.label2=Label(self.frame2,text='Enter start port')
        self.label3=Label(self.frame2,text='Enter end port')

        self.label1.grid(row=4,column=0)
        self.label2.grid(row=5,column=0)
        self.label3.grid(row=6,column=0)

        # text box
        self.entry1=Entry(self.frame2)
        self.entry2=Entry(self.frame2)
        self.entry3=Entry(self.frame2)

        self.entry1.grid(row=4, column=1)
        self.entry2.grid(row=5, column=1)
        self.entry3.grid(row=6, column=1)

        # text area box
        self.textbox=Text(self.frame2)
        self.textbox.configure(state="disabled")
        self.textbox.grid(row=8, column=0, rowspan=1, columnspan=2)

        # enter button
        self.btn = Button(self.frame2,text='Submit')
        self.btn.grid(row=7,column=1)


        # set window size
        self.master.geometry('750x500')


    def createTabs(self):
        self.tab_control = ttk.Notebook(self.master)
        tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab1, text="Page 1")
        tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(tab2, text="Page 2")


    #about information window
    def aboutWindow(self):
        newwin = Toplevel(master=None)
        newwin.geometry("500x100")
        display = Label(newwin, text="About section:\nApp made by Jonathan Trejo\nFor CSCI 5742 - Cybersecurity")
        display.pack()

    def runScan(self, ipaddr, startport, endport):
        portscan.portscanner(ipaddr, startport, endport)
        self.textbox.insert()


def runWindow():
    root = Tk()
    my_gui = GUI(root)
    root.mainloop()
