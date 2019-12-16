import csv

class RowMatcher:
    def __init__(self, input_file, output_file):
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
                if (len(row[1]) > 0) and row_num < 15636: # end of rectangular items
                       codes += [row]
                
                row_num += 1
        
        return codes

    def get_diff(self, initial, final):
        diff = []
        for i in initial:
            if i not in final:
                diff += [i]
        
        return diff

if __name__ == '__main__':
    matcher = RowMatcher('Data/division_csv/division_12.csv', 'Data/nomenclature.csv')
    
    if matcher.initial == matcher.final:
        print('Initial:', len(initial), 'Final:', len(final), initial == final)
    else:
        for d in matcher.diff:
            print(d)