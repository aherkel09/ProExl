from reader import Reader
from hardcodes import Hardcodes

class DuplicateHunter(Reader):
    def __init__(self):
        super().__init__()
        self.item_descriptions = {}
        self.duplicate_descriptions = {}
        self.safe_to_remove = {}
        self.flagged = {}
        self.selections = {}
        self.resolved = []

    def acquire_targets(self):
        self.find_duplicates()
        self.match_values()
        self.eliminate_hardcodes() # remove duplicates via hardcoded queries
        targets = self.flagged.copy() # make copy of data for use in gui
        return targets

    def find_duplicates(self):
        for d in self.data:
            if d[1] not in self.item_descriptions:
                self.item_descriptions[d[1]] = d
            else:
                self.duplicate_descriptions[d[1]] = d

    def match_values(self):
        for key, value in self.duplicate_descriptions.items():
            # remove unique item codes before matching
            item = self.item_descriptions[key].copy()
            item.pop(0)
            duplicate = value.copy()
            duplicate.pop(0)

            if item == duplicate:
                self.safe_to_remove[key] = value # safe to remove if all values match
            else:
                self.flagged[key] = [ # flag for user review
                        self.item_descriptions[key],
                        value
                        ]

    def eliminate_hardcodes(self):
        hardcodes = Hardcodes(self.flagged)
        eliminated = hardcodes.eliminate()
        
        for e in eliminated:
            # if eliminating by hardcoded values leaves 1 option, resolve item
            if len(eliminated[e]) == 1:
                self.item_descriptions[e] = eliminated[e][0]
                self.resolved += [e]

        self.drop_all_duplicates()

    def resolve_item(self, selection, item):
        user_choice = self.flagged[item][selection - 2] # get selected option
        self.item_descriptions[item] = user_choice
        self.resolved += [item]

    def is_finished(self):
        return len(self.item_descriptions) and not len(self.flagged)

    def drop_all_duplicates(self):
        for r in self.resolved:
            self.flagged.pop(r, None)

        for s in self.safe_to_remove:
            self.item_descriptions.pop(s, None)


if __name__ == '__main__':
    hunter = DuplicateHunter()
    hunter.acquire_targets()

    print(hunter.flagged['6x6 Rectangular - Bare'])
