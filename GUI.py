import tkinter as t
from operations import database_operations as op
from tkinter import simpledialog as sd
class gui_book:
    def __init__(self):
        self.m = t.Tk()
        self.x,self.y = op.connection("sql_database/book.db")  
        self.gui()
        """----------------------------------GUI-----------------------------------"""
    def gui(self):
        # labels
        l1= t.Label(self.m,text="Title");l2= t.Label(self.m,text="Author");l3= t.Label(self.m,text="Year");l4= t.Label(self.m,text="ISBN")
        # entry box
        self.e1_val=t.StringVar();self.e2_val=t.StringVar();self.e3_val=t.StringVar();self.e4_val=t.StringVar()
        self.e1 = t.Entry(self.m,textvariable=self.e1_val);self.e2 = t.Entry(self.m,textvariable=self.e2_val)
        self.e3 = t.Entry(self.m,textvariable=self.e3_val);self.e4 = t.Entry(self.m,textvariable=self.e4_val)
        # text area
        self.t1= t.Text(self.m,height=10,width=55)
        #Buttons
        self.b1= t.Button(self.m,text="View all",height=1,width=10,command = self.view_all);self.b2= t.Button(self.m,text="Search entry",height=1,width=10,command = self.search_entry)
        self.b3= t.Button(self.m,text="Add entry",height=1,width=10,command=self.add_entry);self.b4= t.Button(self.m,text="Update selected",height=1,width=10,command=self.update_entry)
        self.b5= t.Button(self.m,text="Delete selected",height=1,width=10,command = self.delete_entry);self.clear= t.Button(self.m,text="Clear All",height=1,width=10,command = self.clear_all)
        # scroll bar
        scrollb = t.Scrollbar(self.m, command=self.t1.yview)
        scrollb.grid(row=4, column=2,columnspan=3)
        self.t1['yscrollcommand'] = scrollb.set
        #adjusting
        #Row =0
        l1.grid(row=0);self.e1.grid(row=0,column=1)
        l2.grid(row=0,column=2);self.e2.grid(row=0,column=3)
        #Row = 1 
        l3.grid(row=1);self.e3.grid(row=1,column=1)
        l4.grid(row=1,column=2);self.e4.grid(row=1,column=3)
        # Text
        self.t1.grid(row=2,column=0,columnspan = 3,rowspan=6,sticky=t.S)
        #Buttons
        self.b1.grid(row=2,column=3,sticky = t.E);self.b2.grid(row=3,column=3,sticky = t.E)
        self.b3.grid(row=4,column=3,sticky = t.E);self.b4.grid(row=5,column=3,sticky = t.E)
        self.b5.grid(row=6,column=3,sticky = t.E);self.clear.grid(row=7,column=3,sticky = t.E)
        
        """------------------------------OPERATIONS------------------------------------"""        
   
    def add_entry(self):
        print('add_started')
        op.insert(self.x,self.y,self.e1_val.get(),self.e2_val.get(),self.e3_val.get(),self.e4_val.get())
    
    def view_all(self):
        v = op.view(self.x,self.y)
        self.t1.insert(t.END,'\n'.join(map(str,[('ID','Title','Author','Year','ISBN')])))
        self.t1.insert(t.END,'\n')
        self.t1.insert(t.END,'\n'.join(map(str, v)))
        self.t1.configure(state= t.DISABLED)
    
    def search_entry(self):
        ids= sd.askinteger(title='SEARCH',prompt='Enter the ID :',parent= self.m )
        v=op.search(self.x,self.y,ids)
        self.t1.insert(t.END,'\n'.join(map(str,[('ID','Title','Author','Year','ISBN')])))
        self.t1.insert(t.END,'\n')
        self.t1.insert(t.END,'\n'.join(map(str, v)))
    
    def update_entry(self):
        ids= sd.askinteger(title='UPDATE',prompt='Enter the ID  :',parent= self.m )
        op.update(self.x,self.y,ids,self.e1_val.get(),self.e2_val.get(),self.e3_val.get(),self.e4_val.get())
    
    def delete_entry(self):
        ids= sd.askinteger(title='DELETE',prompt='Enter the ID  :',parent= self.m )
        op.delete(self.x,self.y,ids)
    def clear_all(self):
        self.t1.configure(state= t.NORMAL)
        self.t1.delete(1.0,'end');self.e1.delete(0,'end');self.e2.delete(0,'end')
        self.e3.delete(0,'end');self.e4.delete(0,'end')

gui = gui_book()
gui.m.mainloop()        