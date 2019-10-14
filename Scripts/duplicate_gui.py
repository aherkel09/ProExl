from tkinter import *
import tkinter as tk

class DuplicateGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('ProExl Duplicate Hunter')
        self.root.configure(bg='black')
        self.item_frame = None
        self.int_var = IntVar()
        self.colors = {
            'brand': '#4bee8f',
            'light': '#b5fdaf',
            'accent': '#74b6b5',
            'dark': '#676087',
            'grey': '#f2f2f2'
        }
        self.make_frame()

    def make_frame(self):
        self.item_frame = tk.Frame(bg='black')
        self.item_frame.pack(fill=BOTH)

    def make_button(self, button_text, callback=None):
        button = tk.Button(self.item_frame, text=button_text, bg=self.colors['dark'],
                fg=self.colors['grey'],activebackground=self.colors['accent'])
        if callback:
            button.configure(command=callback)
        button.pack()

    def make_radio_button(self, button_text, button_val):
        radio = tk.Radiobutton(self.item_frame, text=button_text, variable=self.int_var,
                value=button_val, bg='black', fg=self.colors['grey'],
                selectcolor=self.colors['accent'], indicatoron=True)
        radio.pack(anchor=W)

    def make_label(self, label_text):
        label = tk.Label(self.item_frame, text=label_text, bg='black', fg='#f2f2f2')
        label.pack()

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

if __name__ == '__main__':
    gui = DuplicateGUI()
    gui.skip_button()
    gui.option_button(2, ['click', 'me', 'please'])
    gui.root.mainloop()
