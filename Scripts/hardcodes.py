class Hardcodes():
    def __init__(self, flagged):
        self.items = flagged

    def eliminate_labor_65(self):
        for item in self.items:
            trash = []
            keep = []
            index = 0
            for option in self.items[item]:
                if option[6] == '65': # check labor column for 65
                    trash += [index]
                else:
                    keep += [index]

            if len(keep):
                for t in trash:
                    self.items[item].pop(t)
            else:
                print('no options kept!')
    
    def eliminate(self):
        self.eliminate_labor_65()
        return self.items

