from tkinter import *


class LoanCalculator:
    def __init__(self):

        window = Tk() 
      
        window.title("Home Loan Calculator")
        window.geometry("400x200") 
        
        Label(window, text="Annual Interest Rate").grid(row=1,
                                                     column=1, sticky=W)
        Label(window, text="Number of Years").grid(row=2,
                                                   column=1, sticky=W)
        Label(window, text="Loan Amount").grid(row=3,
                                               column=1, sticky=W)
        Label(window, text="Simple or Compound").grid(row=4,
                                                      column=1, sticky=W)
        Label(window, text="Monthly Payment").grid(row=5,
                                                   column=1, sticky=W)
        Label(window, text="Total Payment").grid(row=6,
                                                 column=1, sticky=W)
   
                                                      

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar,
              justify=LEFT).grid(row=1, column=2)

        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar,
              justify=LEFT).grid(row=2, column=2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar,
              justify=LEFT).grid(row=3, column=2)
        
        self.simpleorcompoundVar = StringVar()
        Entry(window, textvariable=self.simpleorcompoundVar,
              justify=LEFT).grid(row=4, column=2)


        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=5,
                                                                                    column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable=self.totalPaymentVar).grid(row=6,
                                                                                column=2, sticky=E)

      
        btComputePayment = Button(window, text="Calculate",
                                  command=self.computePayment).grid(
            row=6, column=3, sticky=E)
        window.mainloop() 

    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
            * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        monthlyPayment = loanAmount * monthlyInterestRate / \
            (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

        root = Tk()

LoanCalculator()
