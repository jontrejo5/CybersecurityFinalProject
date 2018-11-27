import json
import os
from tkinter import *
from tkinter import Menu
from tkinter import ttk
import tkinter.messagebox
import wordCheck
import returnDescription
import returnPortDescription

from tkinter.ttk import Progressbar

import portscan

class gui(object):

    # set up main page
    def __init__(self, master):
        self.master = master
        master.title("Jon T & Matt S - Advanced Port Scanner")

        self.statusVar = StringVar()  # Variable to store status bar messsage
        self.statusVar.set("Ready")  # Set status bar message

        self.frame3=Frame(self.master)
        self.frame3.pack(side=BOTTOM, fill=X)

        self.frame1=Frame(self.master)
        self.frame1.pack(side=LEFT, fill=X)

        self.frame2=Frame(self.master)
        self.frame2.pack(side=LEFT, fill=X)


        # *********StatusBar************
        self.status = Label(self.frame3, text=self.statusVar.get(), bd=1, relief=SUNKEN,anchor=W)  # Cool looking dynamic status bar
        self.status.pack(side=BOTTOM, fill=X)  # stuck to the bottom

        # *****menu setup*****
        self.dropDown = Menu(master)  # starts out dropdown menu
        master.config(menu=self.dropDown)
        self.fileMenu = Menu(self.dropDown, tearoff=False)
        self.dropDown.add_cascade(label="File", menu=self.fileMenu)  # Adds File submenu
        self.fileMenu.add_command(label="New", command=self.clearData)  # Adds New to file
        self.fileMenu.add_separator()  # Makes it pretty
        self.fileMenu.add_command(label="Exit", command=master.quit)  # Adds a quit function

        self.helpMenu = Menu(self.dropDown, tearoff=False)  # Creates a help submenu
        self.dropDown.add_cascade(label="Help", menu=self.helpMenu)  # adds menu options
 #       self.helpMenu.add_command(label="Help me!", command=self.sorry)
        self.helpMenu.add_command(label="About", command=self.signature)


        # *****gui elements*****
        #self.label=Label(self.frame2, text='Packet Sniffer', height=2)
        #self.label.grid(row=3, column=1)

        #create tabs
        self.tab_control = ttk.Notebook(self.master)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Port Scanner")
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
        self.openPorts=Listbox(self.tab1)
        self.openPorts.pack(expand=1, fill="both")
        #self.textbox.grid(row=8, column=0, rowspan=1, columnspan=2)

        #setup for port info
        self.openPorts.bind("<Double-Button-1>", self.portinfo)



#        self.statusFrame=Frame(self.frame1,width = 200, height =200)
#        self.statusFrame.grid(row=8, columnspan=2)
#        self.statusFrame.columnconfigure(0, weight=10)
#        self.statusFrame.grid_propagate(False)

#        self.statusText=Text(self.statusFrame)
#        self.statusText.grid(sticky="we")

        self.statusText=Listbox(self.frame1)
        self.statusText.grid(row=8, stick=N+S+E+W, columnspan=2)

        # enter button
        self.btn = Button(self.frame1, text='Submit', command=lambda: self.runportscan(self.entry1.get(), self.entry2.get(), self.entry3.get()))
        self.btn.grid(row=7,column=1)

        self.progressBar = tkinter.ttk.Progressbar(self.frame1, orient='horizontal', value=0, mode='determinate')
        self.progressBar.grid(row=12, stick=W+E, columnspan =2)

        self.progressUpdate=Label(self.frame1, text="0/0")
        self.progressUpdate.grid(row=13, stick=W)



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
        display = Label(newwin, text="Created by Jonathan Trejo and Matt Sullivan \n For CSCI 5742 Cybersecurity Programming \n University of Colorado Denver \n Fall 2018")
        display.pack()


    def portinfo(self, string):
        
        string = self.openPorts.get(ACTIVE)

        #set the dir where json file exists
        fileDir = os.path.dirname(os.path.realpath("__file__"))

        # where we save our result
        portinfo = ''
        vulnerabilityinfo = ''

        # get the out from the text line and save only the numbers(port) to x
        x = ''.join(c for c in string if c.isdigit())
        portinfo=returnPortDescription.returnPortDescription(int(x))
        print(portinfo)
        # open the json file
      #  with open(fileDir + "/json/ports.json") as f:
            # where the json info is stored
      #      data = json.load(f)

      #      if x not in str(data.get("ports",{}).get(x)):
      #          portinfo += "Port not found"
      #      else:
     #           portinfo += str(data.get("ports", {}).get(x).get("description", {}))

        # find keywords from the port description

        portwords = wordCheck.wordCheck(portinfo)
        print(portwords)

        # find in the database
        #if portwords == "Port not found":
        vulnerabilityinfo = returnDescription.returnDescription(portwords)

        numMessage, vulnerabilityinfo = returnDescription.returnDescription(portwords)

        stringresult = portinfo

#        string = self.openPorts.get(ACTIVE)

        #set the dir where json file exists
#        fileDir = os.path.dirname(os.path.realpath("__file__"))

        # where we save our result
#        portinfo = ''
 #       vulnerabilityinfo = ''

        # get the out from the text line and save only the numbers(port) to x
  #      x = ''.join(c for c in string if c.isdigit())



   #     portinfo = returnPortDescription.returnPortDescription(x)

        # open the json file
        # with open(fileDir + "/json/ports.json") as f:
        #     # where the json info is stored
        #     data = json.load(f)
        #
        #     if x not in str(data.get("ports",{}).get(x)):
        #         portinfo += "Port not found"
        #     else:
        #         if x not in str(data.get("ports", {}).get(x).get("description", {})):
        #             portinfo += "Port description not found"
        #         else:
        #             portinfo += str(data.get("ports", {}).get(x).get("description", {}))

        # find keywords from the port description

    #    portwords = wordCheck.wordCheck(portinfo)

        # find in the database
     #   if portwords == "Port not found":
      #      vulnerabilityinfo = returnDescription.returnDescription(portwords)


       # stringresult = str(portinfo) + str(vulnerabilityinfo)

        newwin = Toplevel(master=None)
        newwin.geometry("600x100")
        display = Label(newwin, text=stringresult)
        display.pack(side=TOP)
        numResults = Label(newwin, text=numMessage)
        numResults.pack(side=TOP)
        vulner = Listbox(newwin)
        for item in vulnerabilityinfo:
            vulner.insert(END, item)
        vulner.pack(side=BOTTOM, fill="both")


    # submit information and run
    def runportscan(self, ipaddr, startport, endport):

        #enable the text box to write into it
        #self.textbox.configure(state='enabled')
        self.counter = int(startport)
        self.end=int(endport)
        self.ratio=(100/(self.end-self.counter))
        self.numPorts=0
        self.barProgress=0
        self.statusVar.set("Scanning")  # updates the status in the GUI
        self.status.config(text="Scanning")
        self.statusText.insert(END, "Scanning ports from {0} to {1}".format(startport, endport))  # message to user#
        self.statusText.insert(END, "Using IP [0]".format(ipaddr))
        self.statusText.insert(END, "Starting")

        while self.counter < self.end:
            result = portscan.runportscan(ipaddr,self.counter,self.counter+1)
            if result[0] != "":
                self.openPorts.insert(END, result[0])
            self.counter=self.counter+1
            self.numPorts=self.numPorts+result[1]
            self.barProgress=self.barProgress+self.ratio
            self.progressBar.config(value=self.barProgress)  # updates the progressBar
            self.progressUpdate.config(text=str(self.counter) +"/"+str(self.end))
            self.progressUpdate.update_idletasks()
            self.openPorts.update_idletasks()  # Refreshes GUI
            self.progressBar.update_idletasks()

        #run port scanner from portscan.py
    #    result = portscan.runportscan(ipaddr,startport,endport)
    #    self.textbox.insert(INSERT, result)
        self.statusText.insert(END, "Scan Complete")
        self.statusText.insert(END, "{0} Total ports open in range {1} to {2}".format(self.numPorts, startport, endport))  # final message to user
        self.statusVar.set("Ready")  # Updates status
        self.status.config(text="Ready")  # Refreshes Status
        self.openPorts.update_idletasks()  # Refreshes GUI
        tkinter.messagebox.showinfo('Status', 'Scan Complete!')  # message to user

        # then disable the text box to not allow the user to write in it
        #self.textbox.configure(state="disabled")

    def clearData(self):  # Function for "New" option, clears all values and entry/textboxes

        self.statusText.delete(0,END)

        self.openPorts.delete(0, END)  # Clears the listbox

        self.progressBar.config(value=0)  # resets the progressBar
        self.progressBar.update_idletasks()

        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)


    def signature(self):
        tkinter.messagebox.showinfo('About', " Created by Jonathon Trejo and Matt Sullivan \n For CSCI 5742 Cybersecurity Programming \n University of Colorado Denver \n Fall 2018")  # Awesomeness



def runwindow():
    root = Tk()
    my_gui = gui(root)
    root.mainloop()
