import csv
from datetime import datetime
from writer import Writer

def compare_all(in_file, out_file):
    in_data = read_file(in_file)
    out_data = read_file(out_file)

    results = {
        'Input Rows': len(in_data),
        'Output Rows': len(out_data),
        'All Codes Match': in_data == out_data,
    }

    return results

def read_file(file):
    data = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data += row[0] # column containing item code

    return data
        

if __name__ == '__main__':
    in_file = "Data/db_items.csv"
    out_file = "Data/db_revisions_2019-11-06_09-24-10.csv"

    results = compare_all(in_file, out_file)

    writer = Writer()
    writer.results_file = 'Data/comparison_results_' + str(
                datetime.today().strftime('%Y-%m-%d_%H-%M-%S')) + '.txt'
    writer.write_results(results)
    
