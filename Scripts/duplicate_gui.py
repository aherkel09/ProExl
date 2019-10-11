from tkinter import *
import tkinter as tk

class DuplicateGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('ProExl Duplicate Hunter')
        self.root.configure(background='black')
        self.int_var = IntVar()
        self.colors = {
            'brand': '#4bee8f',
            'light': '#b5fdaf',
            'accent': '#74b6b5',
            'dark': '#676087',
            'grey': '#f2f2f2'
        }

    def make_button(self, button_text, callback=None):
        button = tk.Button(self.root, text=button_text, bg=self.colors['dark'], fg=self.colors['grey'],
                activebackground=self.colors['accent'])
        if callback:
            button.configure(command=callback)
        button.pack()

    def make_radio_button(self, button_text, button_val):
        radio = tk.Radiobutton(self.root, text=button_text, variable=self.int_var,
                value=button_val, bg='black', fg=self.colors['grey'],
                selectcolor=self.colors['accent'], indicatoron=True)
        radio.pack(anchor=W)

    def make_label(self, label_text):
        label = tk.Label(self.root, text=label_text, bg='black', fg='#f2f2f2')
        label.pack()

    def skip_button(self):
        self.make_radio_button('Skip This Item', 1)

    def option_button(self, opt_num, opt_list):
        option_text = '\t'.join(opt_list)
        button = self.make_radio_button(option_text, opt_num)
    
    def select_button(self, command):
        button = self.make_button('Select', command)

    def show_complete(self):
        self.root.pack_forget()

if __name__ == '__main__':
    gui = DuplicateGUI()
    gui.skip_button()
    gui.option_button(2, ['click', 'me', 'please'])
    gui.root.mainloop()
