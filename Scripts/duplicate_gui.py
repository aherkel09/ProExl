from tkinter import *
import tkinter as tk

class DuplicateGUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('ProExl Duplicate Hunter')
        self.root.configure(background='black')
        self.int_var = IntVar()

    def make_button(self, button_text):
        button = tk.Button(self.root, text=button_text, bg='#676087', fg='#f2f2f2',
                activebackground='#74b6b5')
        button.pack()

    def make_radio_button(self, button_text, button_val):
        radio = tk.Radiobutton(self.root, text=button_text, variable=self.int_var,
                value=button_val, bg='black', fg='#f2f2f2', activeforeground='#4bee8f',
                command=self.show_value)
        radio.pack(anchor=W)

    def make_label(self, label_text):
        label = tk.Label(self.root, text=label_text, bg='black', fg='#f2f2f2')
        label.pack()

    def skip_button(self):
        self.make_radio_button('Option 1:\nSkip This Item', 1)

    def option_button(self, opt_num, opt_list):
        option_text = '\t'.join(opt_list)
        button = self.make_radio_button(
                'Option ' + str(opt_num) + ':\n' + option_text,
                opt_num)

    def show_value(self):
        print(self.int_var.get())

if __name__ == '__main__':
    gui = DuplicateGUI()
    gui.skip_button()
    gui.option_button(2, ['click', 'me', 'please'])
    gui.root.mainloop()
