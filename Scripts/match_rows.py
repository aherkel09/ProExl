import csv

class RowMatcher:
    def __init__(self, input_file, output_file, max_row):
        self.max_row = max_row
        self.initial = self.get_codes(input_file, initial=True)
        self.final = self.get_codes(output_file)
        self.diff = self.get_diff(self.initial, self.final)
    
    def get_codes(self, filename, initial=False):
        row_num = 1
        codes = []
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            
            if initial:
                next(reader)
                row_num += 1
                
            for row in reader:
                if (len(row[1]) > 0) and row_num < self.max_row:
                       codes += [row[0]]
                
                row_num += 1
        
        return codes

    def get_diff(self, initial, final):
        diff = []
        for i in initial:
            if i not in final:
                diff += [i]
        
        return diff
    
    def show_results(self):
        if self.initial == self.final:
            print('Initial:', len(self.initial), 'Final:', len(self.final), 'Matched:', self.initial == self.final)
        else:
            print('Unmatched (' + str(len(self.diff)) + '):', [d for d in self.diff])

if __name__ == '__main__':
    division = '6'
    
    max_rows = {
        '12': 15636,
        '6': 5738,
    }
    max_row = max_rows[division]
    
    matcher = RowMatcher(
        'Data/division_csv/division_' + division + '.csv',
        'Data/nomenclature_' + division + '.csv',
        max_row
    )
    
    matcher.show_results()
    