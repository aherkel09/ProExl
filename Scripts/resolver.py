from writer import Writer
from duplicate_hunter import DuplicateHunter
from duplicate_gui import DuplicateGUI

class Resolver():
    def __init__(self):
        self.writer = Writer()
        self.hunter = DuplicateHunter()
        self.gui = DuplicateGUI()
        self.targets = {}

    def begin(self):
        self.targets = self.hunter.acquire_targets()
        self.displayTarget()
        self.gui.root.mainloop()
    
    def displayTarget(self):
        target_key = next(iter(self.targets))
        target_options = self.targets.pop(target_key)
        
        self.gui.make_label(target_key)
        self.gui.skip_button() # button to skip item

        option_number = 2
        for opt in target_options:
            self.gui.option_button(option_number, opt) # button to select option
            option_number += 1

if __name__ == '__main__':
    resolver = Resolver()
    resolver.begin()
