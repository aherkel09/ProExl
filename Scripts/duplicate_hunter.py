from reader import Reader
from hardcodes import Hardcodes

class DuplicateHunter(Reader):
    def __init__(self):
        super().__init__()
        self.data_info = {}
        self.items = {}
        self.duplicates = []
        self.safe_to_remove = {}
        self.flagged = {}
        self.resolved = []

    def acquire_targets(self):
        self.find_duplicates()
        self.match_values()
        self.eliminate_hardcodes() # remove duplicates via hardcoded queries
        targets = self.flagged.copy() # make copy of data for use in gui
        return targets

    def find_duplicates(self):
        for data_row in self.data:
            description = data_row[1]
            if description not in self.items:
                self.items[description] = data_row
            else:
                self.duplicates += [data_row]

    def match_values(self):
        num_copies = 0
        for d in self.duplicates:
            description = d[1]
            # remove unique item codes before matching
            item = self.items[description].copy()
            item.pop(0)
            exact_copy = d.copy()
            exact_copy.pop(0)

            if item == exact_copy:
                num_copies += 1
                self.safe_to_remove[description] = d
            else:
                self.flagged[description] = [self.items[description], d]

        self.initial_results(num_copies)

    def eliminate_hardcodes(self):
        hardcodes = Hardcodes(self.flagged)
        eliminated = hardcodes.eliminate()
        
        for e in eliminated:
            # if eliminating by hardcoded values leaves 1 option, resolve item
            if len(eliminated[e]) == 1:
                self.items[e] = eliminated[e][0]
                self.resolved += [e]

        self.drop_all_duplicates()

    def resolve_item(self, selection, item):
        user_choice = self.flagged[item][selection - 2] # get selected option
        self.items[item] = user_choice
        self.resolved += [item]

    def is_finished(self):
        return len(self.items) and not len(self.flagged)

    def drop_all_duplicates(self):
        for r in self.resolved:
            self.flagged.pop(r, None)

        for s in self.safe_to_remove:
            self.items.pop(s, None)

        self.analyze_results()

    def initial_results(self, copies):
        self.data_info = {
            'All Data': str(len(self.data)),
            'Unique Items': str(len(self.items)),
            'Duplicates': str(len(self.duplicates)),
            'Resolved': str(copies),
        }

    def analyze_results(self):
        num_resolved = int(self.data_info['Resolved'])
        num_resolved += len(self.resolved)
        self.resolved = []
        self.data_info['Resolved'] = str(num_resolved)

if __name__ == '__main__':
    hunter = DuplicateHunter()
    hunter.acquire_targets()
    print(hunter.data_info)
