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
        targets = self.flagged
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

    def resolve_item(self, selection, item):
        print(self.flagged[item])
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
