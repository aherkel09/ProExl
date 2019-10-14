from writer import Writer
from duplicate_hunter import DuplicateHunter
from duplicate_gui import DuplicateGUI

class Resolver():
    def __init__(self, test=False):
        self.test = test
        self.writer = Writer()
        self.hunter = DuplicateHunter()
        self.gui = DuplicateGUI()
        self.targets = {}
        self.target_key = ''
        self.undo = {}
        self.last = []

    def begin(self):
        self.targets = self.hunter.acquire_targets()
        self.display_next_target()
        self.gui.root.mainloop()
    
    def display_next_target(self, key=None):
        if key:
            self.target_key = key
        else:
            try:
                self.target_key = next(iter(self.targets))
            except:
                self.check_complete()

        self.gui.make_label(self.target_key)
        header_text = '\t'.join(self.hunter.headers)
        # self.gui.make_label(header_text) FIXME: align headers

        option_number = 2 # skip button is option 1
        for opt in self.targets[self.target_key]:
            self.gui.option_button(option_number, opt) # button to select option
            option_number += 1
        
        self.gui.skip_button() # button to skip item
        self.gui.command_button('Select', self.select_option)
        self.gui.command_button('Undo', self.undo_last)
    
    def select_option(self):
        selected = self.gui.int_var.get()
        if selected > 1:
            self.hunter.resolve_item(selected, self.target_key)
        
        self.undo[self.target_key] = self.targets.pop(self.target_key)
        self.last += [self.target_key]
        self.gui.clear_item()

        if self.test:
            self.check_complete()
        else:
            self.display_next_target()

    def undo_last(self):
        if len(self.last):
            last_key = self.last[len(self.last) - 1]
            self.hunter.resolved.remove(last_key)
            self.targets[last_key] = self.undo[last_key]
            self.undo.pop(last_key)
            self.last.pop(len(self.last) - 1)
            self.gui.clear_item()
            self.display_next_target(last_key)
        else:
            print('nothing to undo')

    def check_complete(self):
        self.hunter.drop_all_duplicates()

        if self.hunter.is_finished() or self.test:
            self.writer.write_to_file(self.hunter.item_descriptions)
            self.gui.show_complete()
        else:
            self.review_skipped()

    def review_skipped(self):
        self.targets = self.hunter.flagged
        self.display_next_target()

if __name__ == '__main__':
    resolver = Resolver(test=True)
    resolver.begin()
