import csv
from datetime import datetime

class Writer():
    def __init__(self):
        self.out_file = 'Data/db_revisions_' + str(
                datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'

    def write_to_file(self, data):
        with open(self.out_file, 'w', newline='') as csv_out:
            writer = csv.writer(csv_out)
            
            for d in data:
                writer.writerow(data[d])


