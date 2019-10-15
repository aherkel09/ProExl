import random

from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

class DuplicateGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('ProExl Duplicate Hunter')
        self.root.configure(bg='black')
        self.item_frame = None
        self.int_var = IntVar()
        self.pady = 4
        self.font = tkFont.Font(family='Palatino Linotype', size=12)
        self.colors = {
            'brand': '#4bee8f',
            'accent': '#74b6b5',
            'dark': '#676087',
        }
        self.grey = '#f2f2f2'
        self.make_frame()

    def make_frame(self):
        self.item_frame = tk.Frame(bg='black')
        self.item_frame.pack(fill=BOTH)

    def make_button(self, button_text, callback=None):
        button = tk.Button(self.item_frame, text=button_text, 
                bg=self.colors[random.choice(list(self.colors.keys()))],
                fg=self.grey,activebackground=self.colors['accent'], font=self.font)
        
        if callback:
            button.configure(command=callback)

        button.pack(pady=self.pady)

    def make_radio_button(self, button_text, button_val):
        radio = tk.Radiobutton(self.item_frame, text=button_text, variable=self.int_var,
                value=button_val, bg='black', fg=self.grey,
                selectcolor=self.colors['dark'], font=self.font, indicatoron=True)
        radio.pack(anchor=W)

    def make_label(self, label_text):
        label = tk.Label(self.item_frame, text=label_text, bg='black', fg=self.grey,
                font=self.font)
        label.pack(pady=self.pady)

    def skip_button(self):
        self.make_radio_button('Skip This Item', 1)

    def option_button(self, opt_num, opt_list):
        option_text = '\t'.join(opt_list)
        button = self.make_radio_button(option_text, opt_num)
    
    def command_button(self, button_text, command):
        button = self.make_button(button_text, command)
    
    def clear_item(self):
        self.item_frame.destroy()
        self.make_frame()

    def show_complete(self):
        self.clear_item()
        self.make_label('Duplicate Hunter is finished. Check the Data folder for database revisions.')
        self.command_button('Exit', self.root.destroy)

if __name__ == '__main__':
    gui = DuplicateGUI()
    gui.make_label('Welcome to the GUI')
    gui.option_button(2, ['click', 'me', 'please'])
    gui.root.mainloop()
