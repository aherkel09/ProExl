from reader import Reader

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
        return self.flagged

    def find_duplicates(self):
        for d in self.data:
            if d[1] not in self.item_descriptions:
                self.item_descriptions[d[1]] = d
            else:
                self.duplicate_descriptions[d[1]] = d

    def match_values(self):
        for key, value in self.duplicate_descriptions.items():
            # remove unique item codes before matching
            item = self.item_descriptions[key]
            item.pop(0)
            duplicate = value
            duplicate.pop(0)

            if item == duplicate:
                self.safe_to_remove[key] = value # safe to remove if all values match
            else:
                self.flagged[key] = [ # flag for user review
                        self.item_descriptions[key],
                        value
                        ]
    
    def select_duplicates(self):
        for f in self.flagged:
            self.make_choice(f, self.flagged[f])
        
        for r in self.resolved:
            self.flagged.pop(r) # remove resolved from list of flagged

    def make_choice(self, item, options):
        print('\n\nSelect an option for ' + item)
        print('\nOption 1:\nSkip this item')
        
        choice = 2
        for o in options:
            print('\nOption ' + str(choice) + ':')
            print(o)
            choice += 1

        selection = input('\nYour choice (option #): ')
        try:
            selection = int(selection)
            if selection == 1:
                return
            else:
                self.resolve_item(selection, item)
        except:
            print('Error: please enter only valid number choices')
            self.make_choice(item, options) # try again to get valid selection

    def resolve_item(self, selection, item):
        user_choice = self.flagged[item][selection - 2] # get selected option
        self.item_descriptions[item] = user_choice
        self.resolved += [item]

    def is_finished(self):
        return len(self.item_descriptions) and not len(self.flagged)

    def drop_all_duplicates(self):
        for s in self.safe_to_remove:
            self.item_descriptions.pop(s, None)

        return self.item_descriptions


if __name__ == '__main__':
    hunter = DuplicateHunter()
    hunter.find_duplicates()
    hunter.match_values()

    print(next(iter(hunter.flagged.values())))
