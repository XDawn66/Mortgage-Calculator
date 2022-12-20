'''
Function Name: makeform
Function description: this function will make the table for displaying data.
@param: root - the tkinter object
@param: fields - the list that holds the name of each line 
@return: the list that holds all the line we created    
'''
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg
import print_me_first
import graph

fields = ('Loan Amount','Interest Rate %','Loan Term(Years)',\
          'Monthly Payment', 'Total Paid')

def makeform(root, fields):
    lines = {}
    for field in fields:
        row = Frame(root) 
        lab = Label(row,width=22, text=field+':',anchor='w')
        line = Entry(row) #we create a new line with specs we set
        
        line.insert(0,"0")
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        lab.pack(side = LEFT)#setting the location for the label
        line.pack(side = RIGHT, expand = YES, fill = X)
        lines[field] = line #put the new line into the list
    return lines

'''
Function Name: error_message
Function description: this function will return the error message when users
give invalid input
@param: error - the message
@return: none  
'''
def error_message(error):
    msg.showwarning('Invalid input', error)

'''
Function Name: monthly_payment
Function description: This function is going to use data from the list we created
to calculate the monthly and total payments for the user.
@param: none
@return: none
'''
def monthly_payment():
    try:
        loanAmount = float(lines['Loan Amount'].get()) #getting data
        loanTerm = float(lines['Loan Term(Years)'].get())
        yearly_rate = float(lines['Interest Rate %'].get())

        if loanAmount <= 0 or loanTerm <= 0 or yearly_rate <= 0:
            error_message("Need a postive number!")
        
        else:
            monthlyRate = (yearly_rate/100)/12 #monthly calculation from the old lab
            numPayments = loanTerm*12
            monthlyPayment = loanAmount*monthlyRate\
                 *pow((1+monthlyRate),numPayments)\
                 /(pow((1+monthlyRate),numPayments)-1)
            totalPayment = monthlyPayment*(loanTerm*12)
            
            payment_text = ('${:,.2f}'.format(monthlyPayment))
            paid_text = ('${:,.2f}'.format(totalPayment))
            
            lines['Monthly Payment'].configure(state='normal') #putting the reuslt to that line
            lines['Monthly Payment'].delete(0,END)
            lines['Monthly Payment'].insert(0,payment_text)
            
            lines['Total Paid'].configure(state='normal')
            lines['Total Paid'].delete(0,END)
            lines['Total Paid'].insert(0,paid_text)
        
    except ValueError: #when the user is giving invalid number
        error_message("Need a postive number >0!")
    
    finally:
        lines['Monthly Payment'].configure(state='readonly') #set those field to read only                                       
        lines['Total Paid'].configure(state='readonly')
                                    
    
    #interestPaid = totalPayment - loanAmount
    

'''
Function Name: main
Function description: this function will call functions that we created to
make the mortgage calculator
@param: none
@return: none  
'''
if __name__ == '__main__':
    personal_info = print_me_first.printinfo()
    root = Tk()
    root.title("Mortgage Calculator")
    root.configure(background='light green') #changing the color of the window
    root.resizable(0,0) #making the window unadjustable
    lines = makeform(root,fields)
    root.bind('<Return>', (lambda event, e = lines:fetch(e)))

#setting styles for lines
    lines['Monthly Payment'].configure(state='readonly',\
                                       font = ("Arial", 14, "bold", "italic"))
    lines['Total Paid'].configure(state='readonly',\
                                            font = ("Arial", 14, "bold", "italic"))

    b1 = Button(root, bg = 'light blue', text = 'Calculate', \
                command=(lambda e = lines:monthly_payment()))
    b1.pack(side = LEFT, padx = 5, pady = 5)

    b2 = Button(root,text = 'Chart',\
                command= (lambda e = lines: graph.display()))
    b2.pack(side = LEFT, padx = 5, pady = 5)

    b3 = Button(root, text = 'Quit', command = root.destroy)
    b3.pack(side = LEFT, padx = 5, pady = 5)

    tbox = tk.Text(root, height=2, width=30)
    tbox.pack()
    tbox.insert(tk.END, personal_info)
    tbox.configure(state='disabled')

    root.mainloop()
