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
        copies = self.flag_or_resolve()
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

    def flag_or_resolve(self):
        copies = 0
        for item in self.duplicates:
            self.flagged[item] = self.unique[item]
            copies += self.flag_copies(item)
            self.check_resolved(item)

        return copies

    def flag_copies(self, item):
        copies = 0
        for option in self.duplicates[item]:
            # make copies without unique item codes
            unique = self.unique[item][0].copy()[1:]
            exact_copy = option.copy()[1:]
            
            if unique == exact_copy:
                # update item description
                option[1] += ' DELETE'
                copies += 1
            else:
                self.flagged[item] += [option]

        return copies


    def eliminate_hardcodes(self):
        hardcodes = Hardcodes(self.flagged.copy())
        (trash, keep) = hardcodes.eliminate()

    def check_resolved(self, item):
        if len(self.flagged[item]) == 1:
            self.flagged.pop(item, None)
            self.resolved += [item]

    def resolve_selection(self, selection, description):
        user_choice = selection - 2
        self.resolve_item(user_choice, description)

    def resolve_item(self, choice, description):
        user_choice = self.flagged[description].pop(choice)
        self.unique[description] = user_choice
        self.signal_deleted(description)

    def signal_deleted(self, item):
        for option in self.flagged[item]:
            option[1] += ' DELETE'

        self.duplicates[item] = item
        self.flagged.pop(item, None)
        self.resolved += [item]

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
    
    def writeout(self):
        writer = Writer()
        writer.write_to_file({'headers': self.headers})
        writer.write_to_file(self.get_final_data())
        writer.write_results(self.data_info)

if __name__ == '__main__':
    hunter = DuplicateHunter()
    hunter.acquire_targets()
