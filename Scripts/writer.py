import csv
from datetime import datetime

class Writer():
    def __init__(self):
        self.out_file = 'Data/db_revisions_' + str(
                datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
        self.results_file = 'Data/analysis_results_' + str(
                datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.txt'

    def write_to_file(self, data):
        with open(self.out_file, 'w', newline='') as csv_out:
            writer = csv.writer(csv_out)
            
            for d in data:
                writer.writerow(data[d])

    def write_results(self, results):
        with open(self.results_file, 'w') as file:
            for r in results:
                file.write(r + ': ' + results[r] + '\n')


