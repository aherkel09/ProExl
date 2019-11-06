class Hardcodes():
    def __init__(self, flagged):
        self.flagged = flagged
        self.choices = {}
        self.columns = {
            'code': 0,
            'description': 1,
            'unit': 2,
            'mat_cost': 3,
            'labor_cost': 6,
            'labor_prod': 7,
            'other_cost': 13,
        }        
            
    def eliminate_by_value(self, item, column, value):
        keep = []
        index = 0
        
        for option in self.flagged[item]:
            if option[self.columns[column]] != value:
                keep += [index]

            index += 1

        if len(keep) == 1:
            # add 2 to index to align with GUI choices
            self.choices[item] = keep[0] + 2
    
    def eliminate(self):
        for item in self.flagged:
            self.eliminate_by_value(item, 'unit', 'LB')
            self.eliminate_by_value(item, 'labor_cost', '65')
            self.eliminate_by_value(item, 'mat_cost', '0')
            self.eliminate_by_value(item, 'labor_prod', '0')
            self.eliminate_by_value(item, 'labor_prod', '1')
            self.eliminate_by_value(item, 'labor_prod', '12')
            self.eliminate_by_value(item, 'labor_prod', '6')
            self.eliminate_by_value(item, 'other_cost', '0.88')

        return self.choices                
