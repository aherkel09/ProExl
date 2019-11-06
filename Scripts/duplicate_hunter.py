from reader import Reader
from writer import Writer
from hardcodes import Hardcodes

class DuplicateHunter(Reader):
    def __init__(self):
        super().__init__()
        self.data_info = {}
        self.unique = {}
        self.duplicates = {}
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
            if description not in self.unique:
                self.unique[description] = [data_row]
            else:
                if description in self.duplicates.keys():
                    self.duplicates[description] += [data_row]
                else:
                    self.duplicates[description] = [data_row]

    def match_values(self):
        num_copies = 0
        for d in self.duplicates:
            # remove unique item codes before matching
            item = self.unique[d].copy()
            item[0].pop(0)
            print(item)
            break
            exact_copy = self.duplicates[d].copy()
            exact_copy.pop(0)

            if item == exact_copy:
                num_copies += 1
            else:
                self.flagged[d] = self.unique[d]

        self.initial_results(num_copies)

    def eliminate_hardcodes(self):
        hardcodes = Hardcodes(self.flagged)
        (kept, trashed) = hardcodes.eliminate()
        
        for k in kept:
            # if eliminating by hardcoded values leaves 1 option, resolve item
            if len(kept[k]) == 1:
                self.unique[k] = kept[k]
                self.resolved += [k]

        for t in trashed:
            if len(trashed[t]):
                self.duplicates[t] = trashed[t]

        self.drop_all_duplicates()

    def resolve_item(self, selection, item):
        user_choice = self.flagged[item].pop(selection - 2) # get selected option
        self.unique[item] = user_choice
        self.duplicates[item] = self.flagged[item]
        self.resolved += [item]

    def is_finished(self):
        return len(self.unique) and not len(self.flagged)

    def drop_all_duplicates(self):
        for r in self.resolved:
            self.flagged.pop(r, None)

        self.analyze_results()

    def initial_results(self, copies):
        self.data_info = {
            'All Data': str(len(self.data)),
            'Unique Items': str(len(self.unique)),
            'Duplicates': str(len(self.duplicates)),
            'Resolved': str(copies),
        }
        
        print(self.data_info)

    def analyze_results(self):
        num_resolved = int(self.data_info['Resolved'])
        num_resolved += len(self.resolved)
        self.resolved = []
        self.data_info['Resolved'] = str(num_resolved)
        
        print(self.data_info)

    def get_final_data(self):
        for d in self.data:
            if self.data[d] == self.duplicates[d]:
                self.signal_deleted(d)

        return self.data

    def signal_deleted(self, item):
        deleted = []
        for option in self.data[item]:
            item[1] += ' DELETE'
            deleted += [item]

        self.data[item] = deleted
    
    def writeout(self):
        writer = Writer()
        writer.write_to_file({'headers': self.headers})
        writer.write_to_file(self.get_final_data())
        writer.write_results(self.data_info)

if __name__ == '__main__':
    hunter = DuplicateHunter()
    hunter.acquire_targets()
