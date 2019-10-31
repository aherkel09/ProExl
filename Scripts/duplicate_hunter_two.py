from reader import Reader
from writer import Writer
from hardcodes import Hardcodes

class DuplicateHunter(Reader):
    def __init__(self):
        super().__init__()
        self.data_info = {}
        self.resolved = []
        # dict format: {description1: [[option1], [option2], ...], ...}
        self.unique = {}
        self.duplicates = {}
        self.flagged = {}

    def acquire_targets(self):
        self.find_duplicates()
        copies = self.check_exact_copies()
        self.initial_results(copies)
        self.eliminate_hardcodes()

    def find_duplicates(self):
        for d in self.data:
            description = d[1]

            if description not in self.unique:
                self.unique[description] = [d]
            elif description not in self.duplicates:
                self.duplicates[description] = [d]
            else:
                self.duplicates[description] += [d]

    def check_exact_copies(self):
        copies = 0
        for item in self.duplicates:
            for option in self.duplicates[item]:
                # make copies without unique item codes
                unique = self.unique[item][0].copy()[1:]
                exact_copy = option.copy()[1:]
                
                if unique == exact_copy:
                    self.resolved += [item]
                    copies += 1
                elif item in self.flagged:
                    self.flagged[item] += [option]
                else:
                    self.flagged[item] = [option]
                    
        return copies

    def eliminate_hardcodes(self):
        hardcodes = Hardcodes(self.flagged)
        (kept, trashed) = hardcodes.eliminate()

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
