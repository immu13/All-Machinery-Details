
from os import times
from tkinter import *
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
import tkinter.messagebox as tmsg
import time
import pyodbc

conn = pyodbc.connect('Driver={SQL SERVER};'
                      'Server=IMRAN_KHAN;'
                      'Database=Mac_Details;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

class machine_details(Tk):
    def __init__(self):
        super().__init__()
        self.title('Machinery Details')
        self.geometry('666x480')
        self.resizable(height=False, width=False)
        self.configure(background = '#ffffff')

    # main page date widget
    def times(self):
        current_time = time.strftime('%H:%M:%S')
        self.l1.config(text = current_time)
        self.l1.after(200, times)

    # main page help menu command
    def Help(self):
        tmsg.showinfo("Help", 'Contact Mr. Imran Khan - +91 9025925441')


    # main page label
    def main_page_label(self,textinp,font, anchor):
        Label(self, text = textinp, bg ="#ffffff", fg = '#000000', font = font, anchor=anchor).pack(padx = 10)

    # main page frame
    def main_page_frame(self):
        f1 = Frame(self, bg = '#36648c', height = 25)
        f1.pack(side =  BOTTOM, fill = X)

        self.l2 = Label(f1, text='Time:', font="constantia 11 bold italic", bg='#36648c', fg='white')
        self.l2.pack(side=LEFT)

        self.l1 = Label(f1, font = 'constantia 11 bold ', bg = '#36648c', fg = 'white')
        self.l1.pack(side = LEFT, padx = 3)

        self.l3 = Label(f1, text = 'Designed by Imran Khan', font='constantia 11 bold italic', bg='#36648c', fg='white')
        self.l3.pack(side = LEFT, padx = 115)

        self.l3 = Label(f1, text='Date:', font='constantia 11 bold italic', bg='#36648c', fg='white')
        self.l3.pack(side=LEFT, padx=2)

        self.mainpage_date = DateEntry(f1, bg='#36648c', fg='black', date_pattern='dd/mm/y')
        self.mainpage_date.pack(side = RIGHT)
        self.mainpage_date.config(state=DISABLED)

    # mai page help function
    def help_window(self):
        main_menu = Menu(self)
        help_menudrop =Menu(main_menu, tearoff = 0)
        help_menudrop.add_command(label = 'Help', command = self.Help)
        root.config(menu = main_menu)
        main_menu.add_cascade(label = 'Help', menu = help_menudrop)


    # new purchased machine enter date button
    def enterdate(self):
        self.newpurchasedval.set(self.newmacpurdate.get_date())

    # edit machine details enter date button
    def entereditdate(self):
        self.editpurchasedval.set(self.editmacpurdate.get_date())

    # new entry code generate button
    def gencode(self):
        self.newgencodeval.set(f'{self.newdivval.get().upper()}/{self.newmaccodeval.get().upper()}{self.newcapval.get().upper()}-{self.newnomacval.get()}/{self.newserialval.get()}')

    # new entry code save button
    def maccodesaved(self):
        if self.newdivval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.newmacnameval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.newmaccodeval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.newcapval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.newnomacval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.newserialval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        else:
            tmsg.showinfo('New Machine Entry', 'New Machine Code Successfully Created')

            Division = self.newdivval.get().upper()
            Machine_Name = self.newmacnameval.get().upper()
            Capacity = self.newcapval.get().upper()
            Machine_Code = self.newmaccodeval.get().upper()
            No_of_Machines = self.newnomacval.get().upper()
            Serial_No = self.newserialval.get()
            Purchased_Date = self.newpurchasedval.get()
            Supplier_Name = self.newsupplierval.get().upper()
            Final_Machine_Code = f'{self.newdivval.get().upper()}/{self.newmaccodeval.get().upper()}{self.newcapval.get().upper()}-{self.newnomacval.get()}/{self.newserialval.get()}'

            cursor.execute('insert into Machine_Details (Division, Machine_Name, Capacity, Machine_Code, No_of_Machines, Serial_No, Purchased_Date, Supplier_Name, Final_Machine_Code) values (?,?,?,?,?,?,?,?,?)',(Division, Machine_Name, Capacity, Machine_Code, No_of_Machines, Serial_No, Purchased_Date, Supplier_Name, Final_Machine_Code))
            conn.commit()

            self.newgencodeval.set('')
            self.newdivval.set('')
            self.newmaccodeval.set('')
            self.newmacnameval.set('')
            self.newcapval.set('')
            self.newnomacval.set('')
            self.newserialval.set('')
            self.newpurchasedval.set('')
            self.newsupplierval.set('')

    # edit machine detail generate code button
    def editgencode(self):
        self.editpreviousval.set(f'{self.editoldcodeval.get().upper()}')
        self.editnewcodeval.set(f'{self.editdivval.get().upper()}/{self.editmaccodeval.get().upper()}{self.editcapval.get().upper()}-{self.editnomacval.get()}/{self.editserialval.get()}')

    # edit machine details save button
    def newcodesaved(self):
        if self.editdivval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.editmacnameval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.editmaccodeval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.editcapval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.editnomacval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        elif self.editserialval.get() == '':
            tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        else:
            tmsg.showinfo('New Machine Entry', 'Machine Code Successfully Updated')

            Division = self.editdivval.get().upper()
            Machine_Name = self.editmacnameval.get().upper()
            Capacity = self.editcapval.get().upper()
            Machine_Code = self.editmaccodeval.get().upper()
            No_of_Machines = self.editnomacval.get().upper()
            Serial_No = self.editserialval.get()
            Purchased_Date = self.editpurchasedval.get()
            Supplier_Name = self.editsupplierval.get().upper()
            Old_Machine_Code = self.editoldcodeval.get().upper()
            Final_Machine_Code = f'{self.editdivval.get().upper()}/{self.editmaccodeval.get().upper()}{self.editcapval.get().upper()}-{self.editnomacval.get()}/{self.editserialval.get()}'

            cursor.execute('update Machine_Details set Division=?, Machine_Name=?, Capacity=?, Machine_Code=?, No_of_Machines=?, Serial_No=?, Purchased_Date=?, Supplier_Name=?, Final_Machine_Code=? where Final_Machine_Code=?',(Division, Machine_Name, Capacity, Machine_Code, No_of_Machines, Serial_No, Purchased_Date,Supplier_Name, Final_Machine_Code, Old_Machine_Code))
            conn.commit()

            # cursor.execute('update Machine_Details set Final_Machine_Code=? where Final_Machine_Code=?',(Final_Machine_Code,Old_Machine_Code))
            #
            # cursor.execute('update Machine_Details set Division=? where Division=?',(Division,Division))
            # cursor.execute('update Machine_Details set Machine_Name=? where Machine_Name=?',(Machine_Name,Machine_Name))
            # cursor.execute('update Machine_Details set Capacity=? where Capacity=?',(Capacity,Capacity))
            # cursor.execute('update Machine_Details set Machine_Code=? where Machine_Code=?',(Machine_Code,Machine_Code))
            # cursor.execute('update Machine_Details set No_of_Machines=? where No_of_Machines=?',(No_of_Machines,No_of_Machines))
            # cursor.execute('update Machine_Details set Serial_No=? where Serial_No=?',(Serial_No,Serial_No))
            # cursor.execute('update Machine_Details set Purchased_Date=? where Purchased_Date=?',(Purchased_Date,Purchased_Date))
            # cursor.execute('update Machine_Details set Supplier_Name=? where Supplier_Name=?',(Supplier_Name,Supplier_Name))
            # cursor.execute('update Machine_Details set Final_Machine_Code=? where Final_Machine_Code=?',(Final_Machine_Code,Final_Machine_Code))
            # conn.commit()

            self.editdivval.set('')
            self.editmacnameval.set('')
            self.editmaccodeval.set('')
            self.editcapval.set('')
            self.editnomacval.set('')
            self.editserialval.set('')
            self.editpurchasedval.set('')
            self.editsupplierval.set('')
            self.editpreviousval.set('')
            self.editnewcodeval.set('')
            self.editoldcodeval.set('')


    # checkbutton command for printing tannery machinery list
    def tanChecked(self):
        if self.var1.get() == 0:
            l1 = Label(self.tan, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l1.config(state = DISABLED)

            l2 = Label(self.tan, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            l2.config(state=DISABLED)

            start = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            start.config(state=DISABLED)
            self.startdate = start

            end = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            end.config(state=DISABLED)
            self.enddate = end

        else:
            l1 = Label(self.tan, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l2 = Label(self.tan, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            start = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            self.startdate = start
            end = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            self.enddate = end

    # button for printing tannnery machine list
    def printtanlist(self):
        self.newmacnamelist = ['Dyeing Drum', 'Compressor']
        if self.var1.get() == 1:
            print(self.startdate.get_date())
            print(self.enddate.get_date())
        else:
            print(self.newmacnamelist)

    # checkbutton command for printing cutting machinery list
    def cutChecked(self):
        if self.var1.get() == 0:
            l1 = Label(self.cut, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l1.config(state = DISABLED)

            l2 = Label(self.cut, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            l2.config(state=DISABLED)

            start = DateEntry(self.cut, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            start.config(state=DISABLED)
            self.startdate = start

            end = DateEntry(self.cut, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            end.config(state=DISABLED)
            self.enddate = end

        else:
            l1 = Label(self.cut, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l2 = Label(self.cut, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            start = DateEntry(self.cut, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            self.startdate = start
            end = DateEntry(self.cut, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            self.enddate = end

    # button for printing cutting machine list
    def printcutlist(self):
        self.newmacnamelist = ['Dyeing Drum', 'Compressor']
        if self.var1.get() == 1:
            print(self.startdate.get_date())
            print(self.enddate.get_date())
        else:
            print(self.newmacnamelist)

    # checkbutton command for printing tannery machinery list
    def fdChecked(self):
        if self.var1.get() == 0:
            l1 = Label(self.fd, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l1.config(state = DISABLED)

            l2 = Label(self.fd, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            l2.config(state=DISABLED)

            start = DateEntry(self.fd, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            start.config(state=DISABLED)
            self.startdate = start

            end = DateEntry(self.fd, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            end.config(state=DISABLED)
            self.enddate = end

        else:
            l1 = Label(self.fd, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l2 = Label(self.fd, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            start = DateEntry(self.fd, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            self.startdate = start
            end = DateEntry(self.fd, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            self.enddate = end


    # button for printing fd machine list
    def printfdlist(self):
        self.newmacnamelist = ['Dyeing Drum', 'Compressor']
        if self.var1.get() == 1:
            print(self.startdate.get_date())
            print(self.enddate.get_date())
        else:
            print(self.newmacnamelist)

    # checkbutton command for printing sd machinery list
    def sdChecked(self):
        if self.var1.get() == 0:
            l1 = Label(self.sd, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l1.config(state = DISABLED)

            l2 = Label(self.sd, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            l2.config(state=DISABLED)

            start = DateEntry(self.sd, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            start.config(state=DISABLED)
            self.startdate = start

            end = DateEntry(self.sd, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            end.config(state=DISABLED)
            self.enddate = end

        else:
            l1 = Label(self.sd, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l2 = Label(self.sd, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            start = DateEntry(self.sd, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            self.startdate = start
            end = DateEntry(self.sd, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            self.enddate = end

    # button for printing sd machine list
    def printsdlist(self):
        self.newmacnamelist = ['Dyeing Drum', 'Compressor']
        if self.var1.get() == 1:
            print(self.startdate.get_date())
            print(self.enddate.get_date())
        else:
            print(self.newmacnamelist)

    # checkbutton command for printing fs machinery list
    def fsChecked(self):
        if self.var1.get() == 0:
            l1 = Label(self.fs, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l1.config(state = DISABLED)

            l2 = Label(self.fs, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            l2.config(state=DISABLED)

            start = DateEntry(self.fs, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            start.config(state=DISABLED)
            self.startdate = start

            end = DateEntry(self.fs, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            end.config(state=DISABLED)
            self.enddate = end

        else:
            l1 = Label(self.fs, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l2 = Label(self.fs, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            start = DateEntry(self.fs, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            self.startdate = start
            end = DateEntry(self.fs, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            self.enddate = end

    # button for printing fs machine list
    def printfslist(self):
        self.newmacnamelist = ['Dyeing Drum', 'Compressor']
        if self.var1.get() == 1:
            print(self.startdate.get_date())
            print(self.enddate.get_date())
        else:
            print(self.newmacnamelist)

    # checkbutton command for printing bug machinery list
    def bugChecked(self):
        if self.var1.get() == 0:
            l1 = Label(self.bug, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l1.config(state = DISABLED)

            l2 = Label(self.bug, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            l2.config(state=DISABLED)

            start = DateEntry(self.bug, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            start.config(state=DISABLED)
            self.startdate = start

            end = DateEntry(self.bug, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            end.config(state=DISABLED)
            self.enddate = end

        else:
            l1 = Label(self.bug, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l2 = Label(self.bug, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            start = DateEntry(self.bug, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            self.startdate = start
            end = DateEntry(self.bug, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            self.enddate = end

    # button for printing bug machine list
    def printbuglist(self):
        self.newmacnamelist = ['Dyeing Drum', 'Compressor']
        if self.var1.get() == 1:
            print(self.startdate.get_date())
            print(self.enddate.get_date())
        else:
            print(self.newmacnamelist)

    # checkbutton command for printing lfs machinery list
    def lfsChecked(self):
        if self.var1.get() == 0:
            l1 = Label(self.lfs, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l1.config(state = DISABLED)

            l2 = Label(self.lfs, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            l2.config(state=DISABLED)

            start = DateEntry(self.lfs, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            start.config(state=DISABLED)
            self.startdate = start

            end = DateEntry(self.lfs, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            end.config(state=DISABLED)
            self.enddate = end

        else:
            l1 = Label(self.lfs, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l2 = Label(self.lfs, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            start = DateEntry(self.lfs, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            self.startdate = start
            end = DateEntry(self.lfs, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            self.enddate = end

    # button for printing lfs machine list
    def printlfslist(self):
        self.newmacnamelist = ['Dyeing Drum', 'Compressor']
        if self.var1.get() == 1:
            print(self.startdate.get_date())
            print(self.enddate.get_date())
        else:
            print(self.newmacnamelist)


# master list of machine button
    def tan(self):
        self.tan = Toplevel(root)
        self.tan.title('Master List of Machineries - Tannery Division')
        self.tan.geometry('500x450')
        self.tan.resizable(height=False, width=False)

        self.var1 = IntVar()

        Label(self.tan, text="Master List of Machineries - Tannery", font='candara 12 bold underline', height=2).grid(row=1, columnspan = 3)
        Checkbutton(self.tan, text = 'Yearly Purchase Details',command=self.tanChecked ,variable = self.var1,font = 'candara 12 bold', height = 2).grid(row=2, column =0)

        Button(self.tan, text = 'Print',command = self.printtanlist, font = 'candara 12 bold italic', bd = 5,relief = RAISED,bg ='#36648c',fg ='#ffffff', width = 15).grid(row = 6, columnspan = 2)

    def cut(self):
        self.cut = Toplevel(root)
        self.cut.title('Master List of Machineries - Cutting Department')
        self.cut.geometry('500x450')
        self.cut.resizable(height=False, width=False)

        self.var1 = IntVar()

        Label(self.cut, text="Master List of Machineries - Cutting Department", font='candara 12 bold', height=2).grid(row=1,
                                                                                                            columnspan=10)
        Checkbutton(self.cut, text='Yearly Purchase Details', command=self.cutChecked, variable=self.var1,
                    font='candara 12 bold', height=2).grid(row=2, column=0)

        Button(self.cut, text='Print', command=self.printcutlist, font='candara 12 bold italic', bd=5, relief=RAISED,
               bg='#36648c',fg ='#ffffff', width=15).grid(row=6, columnspan=2)

    def fd(self):
        self.fd = Toplevel(root)
        self.fd.title('Master List of Machineries - Footwear Division')
        self.fd.geometry('500x450')
        self.fd.resizable(height=False, width=False)

        self.var1 = IntVar()

        Label(self.fd, text="Master List of Machineries - Footwear Division", font='candara 12 bold', height=2).grid(row=1,
                                                                                                            columnspan=10)
        Checkbutton(self.fd, text='Yearly Purchase Details', command=self.fdChecked, variable=self.var1,
                    font='candara 12 bold', height=2).grid(row=2, column=0)

        Button(self.fd, text='Print', command=self.printfdlist, font='candara 12 bold italic', bd=5, relief=RAISED,
               bg='#36648c',fg ='#ffffff', width=15).grid(row=6, columnspan=2)

    def sd(self):
        self.sd = Toplevel(root)
        self.sd.title('Master List of Machineries - Shoe Division')
        self.sd.geometry('500x450')
        self.sd.resizable(height=False, width=False)

        self.var1 = IntVar()

        Label(self.sd, text="Master List of Machineries - Shoe Division", font='candara 12 bold', height=2).grid(row=1,
                                                                                                            columnspan=10)
        Checkbutton(self.sd, text='Yearly Purchase Details', command=self.sdChecked, variable=self.var1,
                    font='candara 12 bold', height=2).grid(row=2, column=0)

        Button(self.sd, text='Print', command=self.printsdlist, font='candara 12 bold italic', bd=5, relief=RAISED,
               bg='#36648c',fg ='#ffffff', width=15).grid(row=6, columnspan=2)

    def fs(self):
        self.fs = Toplevel(root)
        self.fs.title('Master List of Machineries - FullShoe Division')
        self.fs.geometry('500x450')
        self.fs.resizable(height=False, width=False)

        self.var1 = IntVar()

        Label(self.fs, text="Master List of Machineries - FullShoe Division", font='candara 12 bold', height=2).grid(row=1,
                                                                                                            columnspan=10)
        Checkbutton(self.fs, text='Yearly Purchase Details', command=self.fsChecked, variable=self.var1,
                    font='candara 12 bold', height=2).grid(row=2, column=0)

        Button(self.fs, text='Print', command=self.printfslist, font='candara 12 bold italic', bd=5, relief=RAISED,
               bg='#36648c',fg ='#ffffff', width=15).grid(row=6, columnspan=2)

    def bug(self):
        self.bug = Toplevel(root)
        self.bug.title('Master List of Machineries - Bugatti')
        self.bug.geometry('500x450')
        self.bug.resizable(height=False, width=False)

        self.var1 = IntVar()

        Label(self.bug, text="Master List of Machineries - Bugatti Division", font='candara 12 bold', height=2).grid(row=1,
                                                                                                            columnspan=10)
        Checkbutton(self.bug, text='Yearly Purchase Details', command=self.bugChecked, variable=self.var1,
                    font='candara 12 bold', height=2).grid(row=2, column=0)

        Button(self.bug, text='Print', command=self.printbuglist, font='candara 12 bold italic', bd=5, relief=RAISED,
               bg='#36648c',fg ='#ffffff', width=15).grid(row=6, columnspan=2)

    def lfs(self):
        self.lfs = Toplevel(root)
        self.lfs.title('Master List of Machineries - Ladies FUllShoe Division')
        self.lfs.geometry('500x450')
        self.lfs.resizable(height=False, width=False)

        self.var1 = IntVar()

        Label(self.lfs, text="Master List of Machineries - Ladies FullShoe Division", font='candara 12 bold', height=2).grid(row=1,
                                                                                                            columnspan=10)
        Checkbutton(self.lfs, text='Yearly Purchase Details', command=self.lfsChecked, variable=self.var1,
                    font='candara 12 bold', height=2).grid(row=2, column=0)

        Button(self.lfs, text='Print', command=self.printlfslist, font='candara 12 bold italic', bd=5, relief=RAISED,
               bg='#36648c',fg ='#ffffff', width=15).grid(row=6, columnspan=2)

    # new machine entry window
    def machineentry(self):
        self.machineentrywindow = Toplevel(root)
        self.machineentrywindow.title('New Machine Entry')
        self.machineentrywindow.geometry('1000x530')
        self.machineentrywindow.resizable(height=False, width=False)
        # print(self.machineentrywindow.winfo_height())
        # print(self.machineentrywindow.winfo_width())

        Label(self.machineentrywindow, text = "Division", font = 'candara 12 bold', width = 10, height = 2).grid(row = 1, column = 0)
        Label(self.machineentrywindow, text = "Machine Name", font = 'candara 12 bold',width = 20, height = 2).grid(row = 2, column = 0)
        Label(self.machineentrywindow, text = "Machine Code", font = 'candara 12 bold',width = 20, height = 2).grid(row = 3, column = 0)
        Label(self.machineentrywindow, text = "Capacity", font = 'candara 12 bold',width = 20, height = 2).grid(row = 4, column = 0)
        Label(self.machineentrywindow, text = "No. of Machines", font = 'candara 12 bold',width = 20, height =2).grid(row = 5, column = 0)
        Label(self.machineentrywindow, text = "Serial No", font = 'candara 12 bold',width = 20, height = 2).grid(row = 6, column = 0)
        Label(self.machineentrywindow, text = "NEW MACHINE ENTRY", font = 'Constantia 14 bold underline', height = 3).grid(row =  0, columnspan = 6)
        Label(self.machineentrywindow, text = "Generated Code", font = 'candara 12 bold',width = 20, height = 3).grid(row = 8, column = 0)
        Label(self.machineentrywindow, text = "Purchased Date", font = 'candara 12 bold',width = 20, height = 2).grid(row = 3, column = 3)
        Label(self.machineentrywindow, text = "Supplier Name", font = 'candara 12 bold',width = 20, height = 2).grid(row = 4, column = 3)

        self.newdivval = StringVar()
        self.newmacnameval = StringVar()
        self.newmaccodeval = StringVar()
        self.newcapval = StringVar()
        self.newnomacval = StringVar()
        self.newserialval = StringVar()
        self.newgencodeval = StringVar()
        self.newpurchasedval = StringVar()
        self.newsupplierval = StringVar()

        self.newdivlist = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6']
        self.newmacnamelist = cursor.execute('SELECT Distinct Machine_Name FROM Machine_Details').fetchall()
        self.newmaccodelist = cursor.execute('select Distinct Machine_Code from Machine_Details').fetchall()
        # self.newcaplist = ['800','25.0']
        # self.newnomaclist = ['01','02']
        self.newseriallist = cursor.execute('select Serial_No from Machine_Details').fetchall()
        self.newsupplierlist = cursor.execute('select Distinct Supplier_Name from Machine_Details').fetchall()

        Combobox(self.machineentrywindow, text = self.newdivval, values = self.newdivlist, font = 'Cambria 11 bold').grid(row = 1, column = 1)
        Combobox(self.machineentrywindow,text = self.newmacnameval, values = self.newmacnamelist, font = 'Cambria 11 bold').grid(row = 2, column = 1)
        Combobox(self.machineentrywindow,text = self.newmaccodeval, values = self.newmaccodelist, font = 'Cambria 11 bold').grid(row = 3, column = 1)
        Combobox(self.machineentrywindow,text = self.newcapval, font = 'Cambria 11 bold').grid(row = 4, column = 1)
        Combobox(self.machineentrywindow,text = self.newnomacval, font = 'Cambria 11 bold').grid(row = 5, column = 1)
        Combobox(self.machineentrywindow,text = self.newserialval, values = self.newseriallist, font = 'Cambria 11 bold').grid(row = 6, column = 1)
        Entry(self.machineentrywindow,text = self.newpurchasedval,state = DISABLED, width = 22, font = 'Cambria 11 bold').grid(row = 3, column = 4)
        Combobox(self.machineentrywindow,text = self.newsupplierval, values = self.newsupplierlist, font = 'Cambria 11 bold').grid(row = 4, column = 4)
        Entry(self.machineentrywindow, text = self.newgencodeval, state = DISABLED, width = 22, font = 'Cambria 11 bold').grid(row = 8, column = 1)

        purdate = DateEntry(self.machineentrywindow, bg = 'darkblue', fg = 'white', date_pattern = 'dd/mm/y')
        purdate.grid(row = 3, column = 5)
        # purdate._set_text(purdate._date.strftime('%d/%m/%y'))
        self.newmacpurdate = purdate

        Button(self.machineentrywindow, command = self.gencode,  text = 'Generate Code', font ='Cambria 12 bold italic', bd = 5, relief = RAISED,bg = '#36648c',fg ='#ffffff', width = 15).grid(row = 7, columnspan = 2)
        Button(self.machineentrywindow, command = self.maccodesaved,  text = 'Confirm', font ='Cambria 12 bold italic', bd = 5, relief = RAISED,bg = '#36648c',fg ='#ffffff', width = 10).grid(row = 9, columnspan = 2)
        Button(self.machineentrywindow, command = self.enterdate,  text = 'Enter', font ='Cambria 10 bold italic', bd = 3, relief = RAISED,bg = '#36648c',fg ='#ffffff', width = 5).grid(row = 3, column = 6)

    # edit mahcine details window
    def editmachinecode(self):
        self.editmachinecode = Toplevel(root)
        self.editmachinecode.title('Edit Machine Code')
        self.editmachinecode.geometry('1000x580')
        self.editmachinecode.resizable(height=False, width=False)

        Label(self.editmachinecode, text='EDIT MACHINE DETAILS', font = 'Constantia 14 bold underline', height = 3).grid(row=0, columnspan=10)
        Label(self.editmachinecode, text="Enter Machine Code", font='candara 12 bold', width=20, height=2).grid(row=1, column=0)
        Label(self.editmachinecode, text="Division", font='candara 12 bold', width=20, height=2).grid(row=2, column=0)
        Label(self.editmachinecode, text="Machine Name", font='candara 12 bold', width=20, height=2).grid(row=3,column=0)
        Label(self.editmachinecode, text="Machine Code", font='candara 12 bold', width=20, height=2).grid(row=4,column=0)
        Label(self.editmachinecode, text="Capacity", font='candara 12 bold', width=20, height=2).grid(row=5,column=0)
        Label(self.editmachinecode, text="No. of Machines", font='candara 12 bold', width=20, height=2).grid(row=6,column=0)
        Label(self.editmachinecode, text="Serial No", font='candara 12 bold', width=20, height=2).grid(row=7, column=0)
        Label(self.editmachinecode, text="Purchased Date", font='candara 12 bold', width=20, height=2).grid(row=4, column=3)
        Label(self.editmachinecode, text="Supplier Name", font='candara 12 bold', width=20, height=2).grid(row=5, column=3)
        Label(self.editmachinecode, text="Previous M/c Code", font='candara 12 bold', width=20, height=2).grid(row=9, column=0)
        Label(self.editmachinecode, text="New M/c Code", font='candara 12 bold', width=20, height=2).grid(row=10, column=0)


        self.editdivval = StringVar()
        self.editmacnameval = StringVar()
        self.editmaccodeval = StringVar()
        self.editcapval = StringVar()
        self.editnomacval = StringVar()
        self.editserialval = StringVar()
        self.editpurchasedval = StringVar()
        self.editsupplierval = StringVar()
        self.editpreviousval = StringVar()
        self.editnewcodeval = StringVar()
        self.editoldcodeval = StringVar()

        self.editoldcodelist = cursor.execute('select Distinct Final_Machine_Code from Machine_Details').fetchall()
        self.editdivlist = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6']
        self.editmacnamelist = cursor.execute('select Distinct Machine_Name from Machine_Details').fetchall()
        self.editmaccodelist = cursor.execute('SELECT Distinct Machine_Code FROM Machine_Details').fetchall()
        # self.editcaplist = ['800', '25.0']
        # self.editnomaclist = ['01', '02']
        self.editseriallist = cursor.execute('select Serial_No from Machine_Details').fetchall()
        self.editsupplierlist = cursor.execute('select Distinct Supplier_Name from Machine_Details').fetchall()

        Combobox(self.editmachinecode, text=self.editoldcodeval, values = self.editoldcodelist, font = 'Cambria 11 bold').grid(row=1, column=1)
        Combobox(self.editmachinecode, text=self.editdivval, values=self.editdivlist, font = 'Cambria 11 bold').grid(row=2, column=1)
        Combobox(self.editmachinecode, text=self.editmacnameval, values=self.editmacnamelist, font = 'Cambria 11 bold').grid(row=3, column=1)
        Combobox(self.editmachinecode, text=self.editmaccodeval, values=self.editmaccodelist, font = 'Cambria 11 bold').grid(row=4, column=1)
        Combobox(self.editmachinecode, text=self.editcapval, font = 'Cambria 11 bold').grid(row=5, column=1)
        Combobox(self.editmachinecode, text=self.editnomacval, font = 'Cambria 11 bold').grid(row=6, column=1)
        Combobox(self.editmachinecode, text=self.editserialval, values=self.editseriallist, font = 'Cambria 11 bold').grid(row=7, column=1)
        Entry(self.editmachinecode, text=self.editpurchasedval,state = DISABLED, width = 22, font = 'Cambria 11 bold').grid(row=4, column=4)
        Combobox(self.editmachinecode, text=self.editsupplierval, values=self.editsupplierlist, font = 'Cambria 11 bold').grid(row=5, column=4)
        Entry(self.editmachinecode, text=self.editpreviousval, state = DISABLED, width = 22, font = 'Cambria 11 bold').grid(row=9, column=1)
        Entry(self.editmachinecode, text=self.editnewcodeval, state = DISABLED, width = 22, font = 'Cambria 11 bold').grid(row=10, column=1)

        pureditdate = DateEntry(self.editmachinecode, bg='darkblue', fg='white', date_pattern='dd/mm/y')
        pureditdate.grid(row=4, column=5)
        self.editmacpurdate = pureditdate

        Button(self.editmachinecode, command=self.editgencode, text='Generate Code', font='Cambria 12 bold italic',bd=5,relief=RAISED, bg = '#36648c',fg ='#ffffff', width=15).grid(row=8, columnspan=2)
        Button(self.editmachinecode, command=self.newcodesaved, text='Confirm', font='Cambria 12 bold italic', bd=5,
               relief=RAISED, bg = '#36648c',fg ='#ffffff', width=10).grid(row=11, columnspan=2)
        Button(self.editmachinecode, command=self.entereditdate, text='Enter', font='Cambria 10 bold italic', bd=3,
               relief=RAISED, bg = '#36648c',fg ='#ffffff', width=5).grid(row=4, column=6)

    # master list of machine window
    def masterlistmachines(self):
        self.mastermachinewindow = Toplevel(root)
        self.mastermachinewindow.title('Master List of Machineries')
        self.mastermachinewindow.geometry('500x450')
        self.mastermachinewindow.resizable(height=False, width=False)

        Label(self.mastermachinewindow, text='MASTER LIST OF MACHINES', font = 'candara 14 bold ', height = 2).pack(pady = 4)

        Button(self.mastermachinewindow, command=self.tan, text='Tannery Division', font='constantia 12 bold italic', bd=5,relief=RAISED, bg = '#36648c',fg ='#ffffff', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.cut, text='Cutting Department', font='constantia 12 bold italic', bd=5,relief=RAISED, bg = '#36648c',fg ='#ffffff', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.fd, text='Footwear Division', font='constantia 12 bold italic', bd=5,relief=RAISED, bg = '#36648c',fg ='#ffffff', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.sd, text='Shoe Division',font='constantia 12 bold italic', bd=5,relief=RAISED, bg = '#36648c',fg ='#ffffff', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.fs, text='FullShoe Division',font='constantia 12 bold italic', bd=5,relief=RAISED, bg = '#36648c',fg ='#ffffff', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.bug, text='Bugatti Division',font='constantia 12 bold italic', bd=5,relief=RAISED, bg = '#36648c',fg ='#ffffff', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.lfs, text='Ladies FullShoe Division',font='constantia 12 bold italic', bd=5,relief=RAISED, bg = '#36648c',fg ='#ffffff', width=20).pack(pady = 5)

    def machinecode(self):
        self.machineentrywindow = Toplevel(root)
        self.machineentrywindow.title('Machine Codes')
        self.machineentrywindow.geometry('999x444')

    def machinecodedesign(self):
        self.machineentrywindow = Toplevel(root)
        self.machineentrywindow.title('Machine Code Design')
        self.machineentrywindow.geometry('999x444')



    def main_page_button(self):
        Button(self, text = 'New Machine Entry', font = 'constantia 14 bold', bd = 8, bg = '#36648c',fg ='#ffffff', relief = RAISED, command = self.machineentry, width = 25).pack(pady = 4)
        Button(self, text = 'Edit Machine Code', font = 'constantia 14 bold', bd = 8, bg = '#36648c',fg ='#ffffff', relief = RAISED, command = self.editmachinecode, width = 25).pack(pady = 4)
        Button(self, text = 'Master List of Machineries', font = 'constantia 14 bold', bd = 8,bg = '#36648c',fg ='#ffffff', relief = RAISED, command = self.masterlistmachines, width = 25).pack(pady = 4)
        Button(self, text = 'Machine Codes', font = 'constantia 14 bold', bd = 8, bg = '#36648c',fg ='#ffffff', relief = RAISED, command = self.machinecode, width = 25).pack(pady = 4)
        Button(self, text = 'Machine Codes Design', font = 'constantia 14 bold', bd = 8, bg = '#36648c',fg ='#ffffff', relief = RAISED, command = self.machinecodedesign, width = 25).pack(pady = 4)
        Button(self, text = 'Exit', font = 'constantia 14 bold', bd = 8, bg = '#36648c',fg ='#ffffff', relief = RAISED, command = self.quit, width = 25).pack(pady = 4)










if __name__ == '__main__':
    root = machine_details()
    root.main_page_label('N.M.ZACKRIAH &CO', 'candara 18 bold', "n")
    root.main_page_label('ALL DEPARTMENT MACHINERY DETAILS', 'candara 18 bold','n')
    # root.main_page_label('Designed by Imran Khan', 'candara 13 bold italic','s')

    root.main_page_button()

    root.main_page_frame()

    root.times()

    root.help_window()



    root.mainloop()
