from reader import Reader

class DuplicateHunter(Reader):
    def __init__(self):
        super().__init__()
        self.item_descriptions = {}
        self.duplicate_descriptions = {}
        self.flagged = {}
        self.safe_to_remove = {}

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
                self.flagged[key] = [
                        self.item_descriptions[key],
                        value
                        ]



def show_sample(data, min_index, max_index):
    index = min_index
    while index < max_index:
        print(data[index])
        index += 1

if __name__ == '__main__':
    hunter = DuplicateHunter()
    hunter.find_duplicates()
    hunter.match_values()

    print(next(iter(hunter.flagged.values())))
