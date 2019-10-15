from duplicate_hunter import DuplicateHunter
from duplicate_gui import DuplicateGUI

class Resolver():
    def __init__(self, test=False):
        self.test = test
        self.hunter = DuplicateHunter()
        self.gui = DuplicateGUI()
        self.targets = {}
        self.target_key = ''
        self.undo = {}
        self.last = []
        self.skipped = 0

    def begin(self):
        self.targets = self.hunter.acquire_targets()
        self.display_next_target()
        self.gui.root.mainloop()
    
    def display_next_target(self, key=None):
        if key:
            self.target_key = key
            self.fill_gui()
        else:
            self.check_next_key()
    
    def check_next_key(self):
        try:
            self.target_key = next(iter(self.targets))
            self.fill_gui()
        except:
            self.check_complete()
    
    def fill_gui(self):
        self.show_info()
        self.show_remaining()
        self.gui.make_label('')
        self.gui.make_label(self.target_key)
        header_text = '\t'.join(self.hunter.headers)
        # self.gui.make_label(header_text) FIXME: align headers

        option_number = 2 # option 1 reserved for skip button
        for opt in self.targets[self.target_key]:
            self.gui.option_button(option_number, opt)
            option_number += 1
        
        self.gui.skip_button() # button to skip item
        self.gui.command_button('Select', self.select_option)
        self.gui.command_button('Undo', self.undo_last)

    def show_info(self):
        for i in self.hunter.data_info:
            self.gui.make_label(i + ': ' + self.hunter.data_info[i])
    
    def show_remaining(self):
        self.gui.make_label(str(len(self.targets) + self.skipped) +
                            ' Unresolved Duplicates')
    
    def select_option(self):
        selected = self.gui.int_var.get()
        if selected > 1:
            self.hunter.resolve_item(selected, self.target_key)
        else:
            self.skipped += 1
        
        self.undo[self.target_key] = self.targets.pop(self.target_key)
        self.last += [self.target_key]
        self.gui.clear_item()

        if self.test:
            self.hunter.flagged = self.undo # set to last item for testing
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

        if self.hunter.is_finished():
            self.hunter.analyze_results()
            self.hunter.writeout()
            self.gui.show_complete()
        else:
            self.review_skipped()

    def review_skipped(self):
        self.targets = self.hunter.flagged
        self.skipped = 0 # reset skipped count
        self.display_next_target()

if __name__ == '__main__':
    resolver = Resolver(test=False)
    resolver.begin()
