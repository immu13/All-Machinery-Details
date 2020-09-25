
# Qtdesigner

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

    def main_page_label(self,textinp,font, anchor):
        Label(self, text = textinp, bg ="#ffffff", fg = '#000000', font = font, anchor=anchor).pack(padx = 10)

    def gencode(self):
        self.newgencodeval.set(f'{self.newdivval.get()}/{self.newmaccodeval.get()}{self.newcapval.get()}-{self.newnomacval.get()}/{self.newserialval.get()}')

    def maccodesaved(self):
        with open('New Machine Code Entry.txt', 'a') as f:
            f.write(f'{self.newdivval.get()}/{self.newmaccodeval.get()}{self.newcapval.get()}/{self.newserialval.get()} - {self.newsupplierval.get()} - {self.newpurchasedval.get()}\n')
        # if f'{self.divval.get()}/{self.maccodeval.get()}{self.capval.get()}/{self.serialval.get()}' == TRUE:
        #     tmsg.showinfo('New Machine Entry', 'New Machine Code Successfully Created')
        # else:
        #     tmsg.showinfo('New Machine Entry', 'Enter All Fields')

        self.newgencodeval.set('')
        self.newdivval.set('')
        self.newmaccodeval.set('')
        self.newmacnameval.set('')
        self.newcapval.set('')
        self.newnomacval.set('')
        self.newserialval.set('')
        self.newpurchasedval.set('')
        self.newsupplierval.set('')

    def editgencode(self):
        self.editpreviousval.set(f'{self.editoldcode.get()}')
        self.editnewcodeval.set(f'{self.editdivval.get()}/{self.editmaccodeval.get()}{self.editcapval.get()}-{self.editnomacval.get()}/{self.editserialval.get()}')

    def newcodesaved(self):
        with open('Edit Machine Details.txt', 'a') as f:
            f.write(f'{self.editpreviousval.get()}-{self.editdivval.get()}/{self.editmaccodeval.get()}{self.editcapval.get()}-{self.editnomacval.get()}/{self.editserialval.get()} - {self.editsupplierval.get()} - {self.editpurchasedval.get()}\n')

    def machineentry(self):
        self.machineentrywindow = Toplevel(root)
        self.machineentrywindow.title('New Machine Entry')
        self.machineentrywindow.geometry('800x530')
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
        self.newnomaclist = ['1','1']
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

        DateEntry(self.machineentrywindow, width = 12, year = 2020, month = 9, day = 26, bg = 'darkblue', fg = 'white', bd = 2).grid(row = 3, column = 5)

        Button(self.machineentrywindow, command = self.gencode,  text = 'Generate Code', font ='Cambria 12 bold italic', bd = 5, relief = RAISED,bg ='#c1cdc1', width = 15).grid(row = 7, columnspan = 2)
        Button(self.machineentrywindow, command = self.maccodesaved,  text = 'Confirm', font ='Cambria 12 bold italic', bd = 5, relief = RAISED,bg ='#c1cdc1', width = 10).grid(row = 9, columnspan = 2)


    def editmachinecode(self):
        self.editmachinecode = Toplevel(root)
        self.editmachinecode.title('Edit Machine Code')
        self.editmachinecode.geometry('800x530')
        self.resizable(height=False, width=False)

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
        self.editoldcode = StringVar()

        self.editdivlist = ['Z1', 'Z2', 'Z3', 'Z4', 'Z5', 'Z6']
        self.editmacnamelist = ['Dyeing Drum', 'Compressor']
        self.editmaccodelist = ['DRM', 'CPR']
        self.editcaplist = ['800', '25.0']
        self.editnomaclist = ['1', '1']
        self.editseriallist = ['1001', '1014']
        self.editsupplierlist = ['Shaheen Enterprises', 'Western Engineering']

        Entry(self.editmachinecode, text=self.editoldcode, width = 22, font = 'Cambria 11 bold').grid(row=1, column=1)
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

        Button(self.editmachinecode, command=self.editgencode, text='Generate Code', font='Cambria 12 bold italic', bd=5,
               relief=RAISED, bg='#c1cdc1', width=15).grid(row=8, columnspan=2)
        Button(self.editmachinecode, command=self.newcodesaved, text='Confirm', font='Cambria 12 bold italic', bd=5,
               relief=RAISED, bg='#c1cdc1', width=10).grid(row=11, columnspan=2)



    def masterlistmachines(self):
        self.machineentrywindow = Toplevel(root)
        self.machineentrywindow.title('Master List of Machineries')
        self.machineentrywindow.geometry('999x444')

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











