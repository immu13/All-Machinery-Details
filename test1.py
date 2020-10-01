
from tkinter import *
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
import tkinter.messagebox as tmsg

class machine_details(Tk):
    def __init__(self):
        super().__init__()
        self.title('Machinery Details')
        self.geometry('666x500')
        self.resizable(height=False, width=False)
        self.configure(background = '#ffffff')

    # main page label
    def main_page_label(self,textinp,font, anchor):
        Label(self, text = textinp, bg ="#ffffff", fg = '#000000', font = font, anchor=anchor).pack(padx = 10)

    # new purchased machine enter date button
    def enterdate(self):
        self.newpurchasedval.set(self.newmacpurdate.get_date())

    # edit machine details enter date button
    def entereditdate(self):
        self.editpurchasedval.set(self.editmacpurdate.get_date())

    # new entry coe generate button
    def gencode(self):
        self.newgencodeval.set(f'{self.newdivval.get()}/{self.newmaccodeval.get()}{self.newcapval.get()}-{self.newnomacval.get()}/{self.newserialval.get()}')

    # new entry code save button
    def maccodesaved(self):

        # if (f'{self.newdivval.get()}/{self.newmaccodeval.get()}{self.newcapval.get()}/{self.newserialval.get()}') != '':
        #     tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
            # if self.newmacnameval.get() != '':
            #     tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
            #     if self.newmaccodeval.get() != '':
            #         tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
            #         if self.newcapval.get() != '':
            #             tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
            #             if self.newserialval.get() != '':
            #                 tmsg.showinfo('New Machine Entry', 'Enter Missing Field')
        # else:
        #     tmsg.showinfo('New Machine Entry', 'New Machine Code Successfully Created')

        with open('New Machine Code Entry.txt', 'a') as f:
            f.write(f'{self.newdivval.get()}/{self.newmaccodeval.get()}{self.newcapval.get()}/{self.newserialval.get()} - {self.newsupplierval.get()} - {self.newpurchasedval.get()}\n')

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
        self.editpreviousval.set(f'{self.editoldcodeval.get()}')
        self.editnewcodeval.set(f'{self.editdivval.get()}/{self.editmaccodeval.get()}{self.editcapval.get()}-{self.editnomacval.get()}/{self.editserialval.get()}')

    # edit machine details save button
    def newcodesaved(self):
        with open('Edit Machine Details.txt', 'a') as f:
            f.write(f'{self.editpreviousval.get()}-{self.editdivval.get()}/{self.editmaccodeval.get()}{self.editcapval.get()}-{self.editnomacval.get()}/{self.editserialval.get()} - {self.editsupplierval.get()} - {self.editpurchasedval.get()}\n')

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

    # button for printing tannnery machine list
    # #def printtanlist(self):
    #     if (self.var1==0 ):
    #         Label(self.tan, text="Enter Year - From :", font='candara 12 bold', height=2, width=15).grid(row=3,column=0)
    #         Label(self.tan, text="Enter Year - To :", font='candara 12 bold', height=2, width=15).grid(row=4, column=0)
    #         start = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
    #         start.grid(row=3, column=1)
    #         end = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
    #         end.grid(row=4, column=1)
    #         self.yearstart = start
    #         self.yearend = end
    #         print(self.yearstart.get_date())
    #         print(self.yearend.get_date())
    #     else:
    #         print('feeeg')


    def Checked(self):
        if self.var1.get()==1:
            start = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            start.grid(row=3, column=1)
            end = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
            end.grid(row=4, column=1)
            self.yearstart = start
            self.yearend = end
            print(self.yearstart.get_date())
            print(self.yearend.get_date())
        else:
            print("Else")

            l1 = Label(self.tan, text="Enter Year - From :", font='candara 12 bold', height=2, width=15)
            l1.grid(row=3, column=0)
            l2 = Label(self.tan, text="Enter Year - To :", font='candara 12 bold', height=2, width=15)
            l2.grid(row=4, column=0)
            l1.grid_forget()
            l2.grid_forget()


# master list of machine button
    def tan(self):
        self.tan = Toplevel(root)
        self.tan.title('Master List of Machineries - Tannery')
        self.tan.geometry('500x450')
        self.tan.resizable(height=False, width=False)

        self.var1 = IntVar()
        # self.var2 = IntVar()

        Label(self.tan, text="Master List of Machineries - Tannery", font='candara 12 bold', height=2).grid(row=1, columnspan = 10)
        Checkbutton(self.tan, text = 'Yearly Purchase Details',command=self.Checked ,variable = self.var1,font = 'candara 12 bold', height = 2).grid(row=2, column =0)
        # Checkbutton(self.tan,  text = 'List of Tannery Machineries ',variable = self.var2,font = 'candara 12 bold', height = 2).grid(row=5, column =0)
        # Label(self.tan, text="Enter Year - From :", font='candara 12 bold', height=2, width = 15).grid(row=3, column=0)
        # Label(self.tan, text="Enter Year - To :", font='candara 12 bold', height=2, width = 15).grid(row=4, column=0)

        # start = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
        # start.grid(row=3, column=1)
        # end = DateEntry(self.tan, bg='darkblue', fg='white', date_pattern='dd/mm/y')
        # end.grid(row=4, column=1)
        # self.yearstart = start
        # self.yearend = end

        #Button(self.tan, text = 'Print',command = self.printtanlist, font = 'candara 12 bold italic', bd = 5,relief = RAISED,bg ='#c1cdc1', width = 15).grid(row = 6, columnspan = 2)



    def cut(self):
        pass
    def fd(self):
        pass
    def sd(self):
        pass
    def fs(self):
        pass
    def bug(self):
        pass
    def lfs(self):
        pass

    # machine entry window
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
        Label(self.machineentrywindow, text = "New Machine Entry", font = 'Constantia 13 bold').grid(row =  0, columnspan = 5)
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

        self.newdivlist = ['Z1','Z2','Z3','Z4','Z5','Z6']
        self.newmacnamelist = ['Dyeing Drum','Compressor']
        self.newmaccodelist = ['DRM','CPR']
        self.newcaplist = ['800','25.0']
        self.newnomaclist = ['01','02']
        self.newseriallist = ['1001','1014']
        self.newsupplierlist = ['Shaheen Enterprises','Western Engineering']

        Combobox(self.machineentrywindow, text = self.newdivval, values = self.newdivlist, font = 'Cambria 11 bold').grid(row = 1, column = 1)
        Combobox(self.machineentrywindow,text = self.newmacnameval, values = self.newmacnamelist, font = 'Cambria 11 bold').grid(row = 2, column = 1)
        Combobox(self.machineentrywindow,text = self.newmaccodeval, values = self.newmaccodelist, font = 'Cambria 11 bold').grid(row = 3, column = 1)
        Combobox(self.machineentrywindow,text = self.newcapval, values = self.newcaplist, font = 'Cambria 11 bold').grid(row = 4, column = 1)
        Combobox(self.machineentrywindow,text = self.newnomacval, values = self.newnomaclist, font = 'Cambria 11 bold').grid(row = 5, column = 1)
        Combobox(self.machineentrywindow,text = self.newserialval, values = self.newseriallist, font = 'Cambria 11 bold').grid(row = 6, column = 1)
        Entry(self.machineentrywindow,text = self.newpurchasedval, width = 22, font = 'Cambria 11 bold').grid(row = 3, column = 4)
        Combobox(self.machineentrywindow,text = self.newsupplierval, values = self.newsupplierlist, font = 'Cambria 11 bold').grid(row = 4, column = 4)
        Entry(self.machineentrywindow, text = self.newgencodeval, state = DISABLED, width = 22, font = 'Cambria 11 bold').grid(row = 8, column = 1)

        purdate = DateEntry(self.machineentrywindow, bg = 'darkblue', fg = 'white', date_pattern = 'dd/mm/y')
        purdate.grid(row = 3, column = 5)
        # purdate._set_text(purdate._date.strftime('%d/%m/%y'))
        self.newmacpurdate = purdate

        Button(self.machineentrywindow, command = self.gencode,  text = 'Generate Code', font ='Cambria 12 bold italic', bd = 5, relief = RAISED,bg ='#c1cdc1', width = 15).grid(row = 7, columnspan = 2)
        Button(self.machineentrywindow, command = self.maccodesaved,  text = 'Confirm', font ='Cambria 12 bold italic', bd = 5, relief = RAISED,bg ='#c1cdc1', width = 10).grid(row = 9, columnspan = 2)
        Button(self.machineentrywindow, command = self.enterdate,  text = 'Enter', font ='Cambria 12 bold italic', bd = 3, relief = RAISED,bg ='#c1cdc1', width = 5).grid(row = 3, column = 6)

    # edit mahcine details window
    def editmachinecode(self):
        self.editmachinecode = Toplevel(root)
        self.editmachinecode.title('Edit Machine Code')
        self.editmachinecode.geometry('1000x530')
        self.editmachinecode.resizable(height=False, width=False)

        Label(self.editmachinecode, text='Edit Machine Details', font='Constantia 13 bold').grid(row=0, columnspan=10)
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

        self.editdivlist = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6']
        self.editmacnamelist = ['Dyeing Drum', 'Compressor']
        self.editmaccodelist = ['DRM', 'CPR']
        self.editcaplist = ['800', '25.0']
        self.editnomaclist = ['01', '02']
        self.editseriallist = ['1001', '1014']
        self.editsupplierlist = ['Shaheen Enterprises', 'Western Engineering']

        Entry(self.editmachinecode, text=self.editoldcodeval, width = 22, font = 'Cambria 11 bold').grid(row=1, column=1)
        Combobox(self.editmachinecode, text=self.editdivval, values=self.editdivlist, font = 'Cambria 11 bold').grid(row=2, column=1)
        Combobox(self.editmachinecode, text=self.editmacnameval, values=self.editmacnamelist, font = 'Cambria 11 bold').grid(row=3, column=1)
        Combobox(self.editmachinecode, text=self.editmaccodeval, values=self.editmaccodelist, font = 'Cambria 11 bold').grid(row=4, column=1)
        Combobox(self.editmachinecode, text=self.editcapval, values=self.editcaplist, font = 'Cambria 11 bold').grid(row=5, column=1)
        Combobox(self.editmachinecode, text=self.editnomacval, values=self.editnomaclist, font = 'Cambria 11 bold').grid(row=6, column=1)
        Combobox(self.editmachinecode, text=self.editserialval, values=self.editseriallist, font = 'Cambria 11 bold').grid(row=7, column=1)
        Entry(self.editmachinecode, text=self.editpurchasedval, width = 22, font = 'Cambria 11 bold').grid(row=4, column=4)
        Combobox(self.editmachinecode, text=self.editsupplierval, values=self.editsupplierlist, font = 'Cambria 11 bold').grid(row=5, column=4)
        Entry(self.editmachinecode, text=self.editpreviousval, state = DISABLED, width = 22, font = 'Cambria 11 bold').grid(row=9, column=1)
        Entry(self.editmachinecode, text=self.editnewcodeval, state = DISABLED, width = 22, font = 'Cambria 11 bold').grid(row=10, column=1)

        pureditdate = DateEntry(self.editmachinecode, bg='darkblue', fg='white', date_pattern='dd/mm/y')
        pureditdate.grid(row=4, column=5)
        # purdate._set_text(purdate._date.strftime('%d/%m/%y'))
        self.editmacpurdate = pureditdate

        Button(self.editmachinecode, command=self.editgencode, text='Generate Code', font='Cambria 12 bold italic',bd=5,relief=RAISED, bg='#c1cdc1', width=15).grid(row=8, columnspan=2)
        Button(self.editmachinecode, command=self.newcodesaved, text='Confirm', font='Cambria 12 bold italic', bd=5,
               relief=RAISED, bg='#c1cdc1', width=10).grid(row=11, columnspan=2)
        Button(self.editmachinecode, command=self.entereditdate, text='Enter', font='Cambria 12 bold italic', bd=3,
               relief=RAISED, bg='#c1cdc1', width=5).grid(row=4, column=6)

    # master list of machine window
    def masterlistmachines(self):
        self.mastermachinewindow = Toplevel(root)
        self.mastermachinewindow.title('Master List of Machineries')
        self.mastermachinewindow.geometry('500x450')
        self.mastermachinewindow.resizable(height=False, width=False)

        Label(self.mastermachinewindow, text='Master List of Machines', font='Constantia 13 bold').pack(pady = 4)

        Button(self.mastermachinewindow, command=self.tan, text='Tannery Division', font='Cambria 12 bold italic', bd=5,relief=RAISED, bg='#c1cdc1', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.cut, text='Cutting Department', font='Cambria 12 bold italic', bd=5,relief=RAISED, bg='#c1cdc1', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.fd, text='Footwear Division', font='Cambria 12 bold italic', bd=5,relief=RAISED, bg='#c1cdc1', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.sd, text='Shoe Division',font='Cambria 12 bold italic', bd=5,relief=RAISED, bg='#c1cdc1', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.fs, text='FullShoe Division',font='Cambria 12 bold italic', bd=5,relief=RAISED, bg='#c1cdc1', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.bug, text='Bugatti Division',font='Cambria 12 bold italic', bd=5,relief=RAISED, bg='#c1cdc1', width=20).pack(pady = 5)
        Button(self.mastermachinewindow, command=self.lfs, text='Ladies FullShoe Division',font='Cambria 12 bold italic', bd=5,relief=RAISED, bg='#c1cdc1', width=20).pack(pady = 5)

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
    root.main_page_label('Designed by Imran Khan', 'candara 14 bold italic','s')

    root.main_page_button()



    root.mainloop()
