import re, csv

class Nomenclature:
    def __init__(self, data_file, regex_list):
        self.data_file = data_file
        self.regex_list = self.compile_expressions(regex_list)
        self.matched = {}

    def compile_expressions(self, regex_list):
        return [re.compile(exp) for exp in regex_list]

    def matches_expression(self, description):
        for exp in self.regex_list:
            result = exp.search(description)

            if result:
                return result

        return None

    def search_all(self):
        with open(self.data_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                match = self.matches_expression(row[0])

                if match:
                    self.matched[row[0]] = match

if __name__ == '__main__':
    regex_list = []
    nom = Nomenclature('match.csv', regex_list)
    nom.search_all()
