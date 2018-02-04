import tkinter as tk
from tkinter import StringVar
from makeDuct import DuctSizes

class ProExl():
    def __init__(self):
        #initial screen setup with user prompts.
        self.root = tk.Tk()
        self.root.title('ProExl 0.0.1 by Avery Herkel')
        self.root.geometry('800x600')
        self.font = ('Calibri', 12, 'bold') #sets default font.
        self.fg='#448D76'
        self.bg = '#F3F7D4' #sets default background color for windows and widgets.
        self.bbg = '#CBE432' #sets default background color for buttons.
        self.abg = '#EA202C' #sets default active background color for buttons.
        self.root.config(bg=self.bg)
        self.welcome()
    
    def welcome(self):
        #frame with initial widgets.
        self.welcomeFrame = tk.Frame(self.root, bg=self.bg)
        
        self.welcomeLabel = tk.Label(self.welcomeFrame,
                                     text='Enter A Fitting\nAnd Select A Duct Construction Type',
                                     font=self.font, fg=self.fg, bg=self.bg)
        
        #buttons for choosing duct type.
        self.type = StringVar()
        self.fitting = StringVar()
        self.rectButton = tk.Radiobutton(self.welcomeFrame, text='Rectangular', variable=self.type, value='Rectangular',
                                         fg=self.fg, bg=self.bbg, activebackground=self.abg, indicatoron=0, width=24, pady=8,
                                         font=self.font, command=self.chooseType)
        self.spiralButton = tk.Radiobutton(self.welcomeFrame, text='Spiral', variable=self.type, value='Spiral',
                                           fg=self.fg, bg=self.bbg, activebackground=self.abg, indicatoron=0, width=24, pady=8,
                                           font=self.font, command=self.chooseType)
        self.fittingEntry = tk.Entry(self.welcomeFrame, textvariable=self.fitting, width=30,
                                     fg=self.bbg, bg=self.fg, font=self.font, bd=4, justify='center')
        self.welcomeFrame.pack()
        self.welcomeLabel.pack()
        self.fitting.set('Duct')
        self.fittingEntry.pack()
        self.rectButton.pack()
        self.spiralButton.pack()
        
    
    def chooseType(self):
        try:
            self.stateLabel.pack_forget()
        except:
            None
        #disables buttons and displays request for duct sizes.
        self.rectButton.config(state='disabled')
        self.spiralButton.config(state='disabled')
        self.type = self.type.get()
        self.fitting = self.fitting.get()
        self.dimensionType(self.type)
    
    def dimensionType(self, type):
        #establishes dimension type for user input.
        if type == 'Rectangular':
            self.dimName = 'Width'
        elif type == 'Spiral':
            self.dimName = 'Diameter'
        self.inputSizeWidgets(self.type)
        
    def inputSizeWidgets(self, type):
        #frame for new widgets.
        self.sizeFrame = tk.Frame(self.root, bg=self.bg)
        self.sizeFrame.pack()
         
        self.smLabel = tk.Label(self.sizeFrame, text='Enter Smallest ' +
                                      self.dimName + ' for ' + self.type + ' ' + self.fitting + ':',
                                      font=self.font, fg=self.fg, bg=self.bg)
        self.lgLabel = tk.Label(self.sizeFrame, text='Enter Largest ' +
                                self.dimName + ' for ' + self.type + ' ' + self.fitting + ':',
                                font = self.font, fg=self.fg, bg=self.bg)
        
        self.smString = StringVar()
        self.smString.set('24')
        self.smEntry = tk.Entry(self.sizeFrame, width=30, textvariable=self.smString,
                                justify='center', font=self.font, fg=self.bbg, bg=self.fg)
        self.lgString = StringVar()
        self.lgString.set('48')
        self.lgEntry = tk.Entry(self.sizeFrame, width=30, textvariable=self.lgString,
                                    justify='center', font=self.font, fg=self.bbg, bg=self.fg)
        
        #button for generating duct sizes.
        self.genDuctButton = tk.Button(self.sizeFrame, text='Generate Duct Sizes',
                                 fg=self.fg, bg=self.bbg, activebackground=self.abg, font=self.font,
                                 command=self.generateDuct)
        
        self.smLabel.pack()
        self.smEntry.pack()
        self.lgLabel.pack()
        self.lgEntry.pack()
        self.genDuctButton.pack()
    
    def generateDuct(self):
        #defines size and type, creates duct objects.
        self.smDimension = self.smString.get()
        self.lgDimension = self.lgString.get()
        self.sizes = DuctSizes(self.type, self.smDimension, self.lgDimension, self.fitting)
        self.sizes.makeType()
        self.sizes.saveDuct()
        self.indicateSuccess()
    
    def indicateSuccess(self):
        self.sizeFrame.pack_forget()
        self.welcomeFrame.pack_forget()
        self.welcome()
        self.stateLabel = tk.Label(self.welcomeFrame, text='Ductwork Data Has Been Generated in the Templates Folder.',
                                   font=self.font, fg=self.fg, bg=self.bg)
        self.stateLabel.pack()
    
if __name__ == '__main__':
    app = ProExl()
    app.root.mainloop()
