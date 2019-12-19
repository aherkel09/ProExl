import re, csv
from expressions import Expressions
from match_rows import RowMatcher

class Nomenclature:
    def __init__(self, in_file, out_file, expressions, division_num):
        self.in_file = in_file
        self.out_file = out_file
        self.division_num = division_num
        self.regex_dict = expressions.divisions[division_num]
        self.subtypes = expressions.subtypes[division_num]
        self.revisions = expressions.revisions[division_num]
        self.subtype_revisions = expressions.subtype_revisions[division_num]
        self.matched = self.match_keys()
        self.max_row = 0
        
        
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
            result = data[key].findall(description)
        
            if result:
                return (key, result)
            
            return None
        
        
    def extract_size(self, description):
        digits = '([0-9]+(/[0-9]+)?(-[0-9]+(/[0-9]+)?)?"?)'
        size = re.compile(digits + '*[ ]?x?[ ]?' + digits + '*[ ]?x?[ ]?' + digits + '?', re.IGNORECASE)
        found = re.findall(size, description)
        
        size_list = []
        exclusions = ['11.25', '22.5', '45', '90', '125', '150', '180', '300', '921', '2000', '3000', '6000']
        for sizes in found:
            for size in sizes:
                if size != '' and not size.startswith('/') and not size.startswith('-') and size not in exclusions:
                    size_list += [size.replace('"', '')]
                
        return size_list
    
            
    def search_all(self):
        skipped = 0
        with open(self.in_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                
                if len(row[2]) > 0:                    
                    match = self.match_expression(row[1])
        
                    if match:
                        self.matched[match[0]] += [row]
                else:
                    skipped += 1
                    
        print('Skipped: ' + str(skipped))
                    
                    
    def revise_all(self):
        deleted = 0
        for m in self.matched:
            for row in self.matched[m]:
                
                if 'DELETE' not in row[1]:
                    size_list = self.extract_size(row[1])
                    key, subtypes = self.match_subtype(m, row[1])
            
                    if subtypes:
                        try:
                            subtypes = [s.lower() for s in subtypes]
                        except:
                            print(m, row[1], subtypes)
                            raise ValueError
                    
                    row[1] = self.rename(key, size_list, subtypes)
                else:
                    deleted += 1
                    
        print('Deleted: ' + str(deleted))
                
    
    def rename(self, key, size_list, subtypes):
        template = self.revisions[key]
        
        for i in range(len(size_list)):
            template = template.replace('SIZE' + str(i), size_list[i])
        
        if subtypes:
            substring = ''
            for s in subtypes:
                if s in self.subtype_revisions:
                    subtype = self.subtype_revisions[s]
                else:
                    subtype = s.upper()
                
                if subtype not in template and subtype not in substring:
                    substring += ' ' + subtype

            template = template.replace('_SUBTYPES', substring)
        else:
            template = template.replace('_SUBTYPES', '')
        
        return self.remove_extraneous(template)
    
    
    def remove_extraneous(self, string):
        size = re.compile('x*SIZE[0-9]*', re.IGNORECASE)
        found = re.findall(size, string)
        
        for f in found:
            string = string.replace(f, '')
        
        return string
    
                    
    def write_out(self):
        lines_written = 0
        with open(self.out_file, 'w', newline='\n') as f:
            writer = csv.writer(f)
            for key in self.matched:
                writer.writerows(self.matched[key])
                lines_written += len(self.matched[key])
        
        self.max_row = lines_written
        print('Finished writing', lines_written, 'lines.')
                
                                
if __name__ == '__main__':
    division = '12'
    in_file = 'Data/division_csv/division_' + division + '.csv'
    out_file = 'Data/nomenclature_' + division + '.csv'
    exp = Expressions()
    
    nom = Nomenclature(in_file, out_file, exp, division)
    nom.search_all()
    nom.revise_all()
    nom.write_out()
    
    matcher = RowMatcher(in_file, out_file, nom.max_row)
    matcher.write_results()
    