from writer import Writer
from duplicate_hunter import DuplicateHunter
from duplicate_gui import DuplicateGUI

class Resolver():
    def __init__(self):
        self.writer = Writer()
        self.hunter = DuplicateHunter()
        self.gui = DuplicateGUI()
        self.targets = {}
        self.target_key = ''
        self.target_options = []

    def begin(self):
        self.targets = self.hunter.acquire_targets()
        self.display_next_target()
        self.gui.root.mainloop()
    
    def display_next_target(self):
        try:
            self.target_key = next(iter(self.targets))
        except:
            self.check_complete()

        self.target_options = self.targets.pop(self.target_key)
        self.gui.make_label(self.target_key)
        header_text = '\t'.join(self.hunter.headers)
        # self.gui.make_label(header_text) FIXME: align headers

        option_number = 2 # skip button is option 1
        for opt in self.target_options:
            self.gui.option_button(option_number, opt) # button to select option
            option_number += 1
        
        self.gui.skip_button() # button to skip item
        self.gui.select_button(self.select_option)
    
    def select_option(self):
        selected = self.gui.int_var.get()
        if selected > 1:
            self.hunter.resolve_item(selected, self.target_key)
        
        self.display_next_target()

    def check_complete(self):
        self.hunter.drop_all_duplicates()

        if self.hunter.is_finished():
            self.gui.show_complete()
        else:
            self.review_skipped()

    def review_skipped(self):
        self.targets = self.hunter.flagged
        self.display_next_target()

if __name__ == '__main__':
    resolver = Resolver()
    resolver.begin()

    first_key = next(iter(resolver.targets))
    resolver.targets = {first_key: resolver.targets.pop(first_key)}
