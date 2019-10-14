import csv
from datetime import datetime

class Writer():
    def __init__(self):
        self.out_file = 'Data/db_revisions_' + str(
                datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'

    def write_to_file(self, data):
        with open(self.out_file, 'w') as csv_out:
            writer = csv.writer(csv_out)
            
            index = 0
            for d in data:
                print(data[d])
                index += 1
                if index > 8:
                    break

                # writer.writerow(data[d])


