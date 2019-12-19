import csv

def synthesize(data, division):
    with open('Data/synthesis_' + division + '.csv', 'w', newline='\n') as out:
        writer = csv.writer(out)
        
        with open('Data/division_csv/division_' + division + '.csv', 'r') as f:
            reader = csv.reader(f)
            
            for row in reader:
                if row[0] in data:
                    writer.writerow(data[row[0]])
                else:
                    writer.writerow(row)
        

def get_data(division):
    data = {}
    with open('Data/nomenclature_' + division + '.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data[row[0]] = row
    
    return data


if __name__ == '__main__':
    for i in ['3', '6', '12']:
        data = get_data(i)
        synthesize(data, i)