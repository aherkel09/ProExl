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
        self.flag_or_resolve()
        self.initial_results()
        self.eliminate_hardcodes()
        self.analyze_results()
        
        return self.flagged.copy()
    

    def find_duplicates(self):
        for d in self.data:
            if len(d[1]): # skip division names
                description = d[1]

                if description not in self.unique:
                    self.unique[description] = [d]
                elif description not in self.duplicates:
                    self.duplicates[description] = [d]
                else:
                    self.duplicates[description] += [d]
                

    def flag_or_resolve(self):
        for item in self.duplicates:
            self.flagged[item] = self.unique[item].copy()
            self.flag_copies(item)
            self.check_resolved(item)


    def flag_copies(self, item):
        for option in self.duplicates[item]:
            # make copies without unique item codes
            unique = self.unique[item][0].copy()[1:]
            exact_copy = option.copy()[1:]
            
            if unique == exact_copy:
                # update item description
                option[1] += ' DELETE'
            else:
                self.flagged[item] += [option]
    

    def eliminate_hardcodes(self):
        hardcodes = Hardcodes(self.flagged)
        eliminated = hardcodes.eliminate()

        for e in eliminated:
            self.resolve_selection(eliminated[e], e)
        

    def resolve_selection(self, selection, description):
        user_choice = selection - 2
        self.resolve_item(user_choice, description)
        

    def resolve_item(self, choice, description):
        user_choice = self.flagged[description].pop(choice)
        self.unique[description] = [user_choice]
        self.signal_deleted(description)


    def check_resolved(self, item):
        if len(self.flagged[item]) <= 1 or self.all_deleted(item):
            self.flagged.pop(item, None)
            self.resolved += [item]


    def all_deleted(self, item):
        all_deleted = True
        for option in self.flagged[item]:
            if 'DELETE' not in option[1]:
                all_deleted = False

        return all_deleted
        

    def signal_deleted(self, item):
        for option in self.flagged[item]:
            option[1] += ' DELETE'
            
        self.duplicates[item] = self.flagged[item]
        self.check_resolved(item)
        

    def initial_results(self):
        self.data_info = {
            'All Data': str(len(self.data)),
            'Unique Items': str(len(self.unique)),
            'Duplicates': str(len(self.duplicates)),
            'Resolved': str(0),
        }
        
        self.analyze_results()
        

    def analyze_results(self):
        num_resolved = int(self.data_info['Resolved'])
        num_resolved += len(self.resolved)
        self.resolved = []
        self.data_info['Resolved'] = str(num_resolved)
        
        
    def is_finished(self):
        return len(self.flagged) == 0


    def get_final_data(self):
        item_codes = {}
        
        for u in self.unique:
            for option in self.unique[u]:
                item_codes[option[0]] = option
            
        for d in self.duplicates:
            for option in self.duplicates[d]:
                item_codes[option[0]] = option

        for d in self.data:
            code = d[0]
            if code in item_codes: 
                d = item_codes[code]

        return self.data
        
        
    def writeout(self):        
        writer = Writer()
        writer.write_to_file([self.headers])
        writer.write_to_file(self.get_final_data())
        writer.write_results(self.data_info)
        

def show_sample(data, lines):
    if lines == 'all':
        lines = len(data)
        
    print('showing', lines, 'of', len(data), '...')
    displayed = 0

    while displayed < lines:
        print(list(data.values())[displayed])
        displayed += 1
        

if __name__ == '__main__':
    hunter = DuplicateHunter()
    targets = hunter.acquire_targets()
    hunter.writeout()

    
