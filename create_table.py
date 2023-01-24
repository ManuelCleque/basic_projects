# Python program to create an editable table
  
from tkinter import *
 
 
class Table:
     
    def __init__(self,root):


        # code for creating labels
        for j in range(total_columns):
            self.l = Label(root,text=header[j]).grid(row=0,column=j)
         
        # code for creating data table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=10,
                               font=('Arial',12))
                 
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, lst[i][j])
 


# take the data
lst = [('C01','Front loader','Caterpillar',0.85),
       ('V10','Dump truck','Komatsu',0.80),
       ('P03','Drill','Sandvik',0.76),
       ('V08','Dump truck','Terex',0.78),
       ('C03','Front loader','Caterpillar',0.82)]

header = ['Code','Type','Brand','Mec. Availability']
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0]) 
  
# create root window - starting code
root = Tk()
root.title("Equipment table")
t = Table(root)
root.mainloop()