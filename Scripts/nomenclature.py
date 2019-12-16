import re, csv
from expressions import Expressions

class Nomenclature:
    def __init__(self, data_file, regex_dict, subtypes):
        self.data_file = data_file
        self.regex_dict = regex_dict
        self.subtypes = subtypes
        self.matched = self.match_keys()
        
    def match_keys(self):
        matched = {}
        for key in self.regex_dict:
            matched[key] = []
        
        return matched

    def match_expression(self, description):
        for key in self.regex_dict:
            result = self.find_match(self.regex_dict, key, description)

            if result:
                return result

        return None
    
    def match_subtype(self, key, description):
        result = self.find_match(self.subtypes, key, description)
        
        if result:
            return result
        
        return (key, None)
    
    def find_match(self, data, key, description):
        if key in data:
            result = data[key].search(description)
        
            if result:
                return (key, result)
            
            return None
            

    def search_all(self):
        with open(self.data_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                match = self.match_expression(row[1])

                if match:
                    self.matched[match[0]] += [row]
                    
    def revise_all(self):
        sub_count = 0
        total_count = 0
        for m in self.matched:
            for row in self.matched[m]:
                key, subtype = self.match_subtype(m, row[1])
                
                # TODO: generate new descriptions, accounting for subtype
                
                if subtype:
                    sub_count += 1
                
                total_count += 1
        
        print('sub_count:', sub_count, 'total_count', total_count)
                    
    def write_out(self):
        with open('Data/nomenclature.csv', 'w', newline='\n') as f:
            writer = csv.writer(f)
            for key in self.matched:
                writer.writerows(self.matched[key])
                
                                
if __name__ == '__main__':
    exp = Expressions()
    regex_dict = exp.division_12
    subtypes = exp.subtypes_12
    
    nom = Nomenclature('Data/division_csv/division_12.csv', regex_dict, subtypes)
    nom.search_all()
    nom.revise_all()
    