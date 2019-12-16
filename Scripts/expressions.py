import re

class Expressions:
    def __init__(self):
        self.division_3 = self.division_3()
        self.division_6 = self.division_6()
        self.division_12 = self.division_12()
        self.subtypes_12 = self.subtypes_12()
    
    def division_3(self):
        return None
    
    def division_6(self):
        return None
    
    def division_12(self):
        size_x_size = '[0-9]+[0-9]*"?[ ]?x[ ]?[0-9]+[0-9]*"?'
        
        return self.compile_division({
            'Straight Collar': '^straight collar',
            'Reducers': '^' + size_x_size + '([ ]*to[ ]*|[ ]*-[ ]*)' + size_x_size + '[ ]*-[ ]*reducer',
            'End Caps': '^' + size_x_size + ' - end cap',
            'Rectangular Duct': '^' + size_x_size + '( rectangular)? - (?!fire|bottom|side)',
            'Rectangular Tees': '^' + size_x_size + 'x[ ]?[0-9]+[0-9]*"? - rectangular tee',
            'Vertical Elbows': 'vertical duct elbow',
            'Horizontal Elbows': 'horizontal duct elbow',
            })
        
    def subtypes_12(self):
        return self.compile_division({
            'Straight Collar': '(bare|1" [w|l|i]*|2" [w|l|i]*)+',
            'Rectangular Duct': '(bare|1" [w|l|i]*|2" [w|l|i]*|mastic)+',
            'Vertical Elbows': '(bare|wrapped|lined)+',
            'Horizontal Elbows': '(bare|wrapped|lined)+',
            })
    
    def compile_division(self, division_data):
        for d in division_data:
            division_data[d] = re.compile(division_data[d], re.IGNORECASE)
        
        return division_data
    
    def all_divisions(self):
        return {
            '3': self.division_3,
            '6': self.division_6,
            '12': self.division_12
            }

if __name__ == '__main__':
    exp = Expressions()
    print(exp.all_divisions())