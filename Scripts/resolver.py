from writer import Writer
from duplicate_hunter import DuplicateHunter
from duplicate_gui import DuplicateGUI

class Resolver():
    def __init__(self):
        self.writer = Writer()
        self.hunter = DuplicateHunter()
        self.gui = DuplicateGUI()
        self.targets = {}
        self.current_target = None

    def begin(self):
        self.targets = self.hunter.acquire_targets()
        self.displayTarget()
        self.gui.root.mainloop()
    
    def displayTarget(self):
        target_key = next(iter(self.targets))
        self.current_target = self.targets.pop(target_key)
        
        self.gui.make_label(target_key)

        option_number = 2
        for opt in self.current_target:
            self.gui.option_button(option_number, opt) # button to select option
            option_number += 1
        
        self.gui.skip_button() # button to skip item
        self.gui.select_button(self.select_option)
    
    def select_option(self):
        selected = self.gui.int_var.get()
        print(selected)

if __name__ == '__main__':
    resolver = Resolver()
    resolver.begin()
