import csv

class CsvFileReader:
    data = []
    
    def __init__(self, filename):
        self.filename = filename

    def to_list(self):
        with open(self.filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i==0: 
                    self.data.append(row) 
                    continue
                new_row = []
                row = (row[0].split(";"))
                del(row[-1])
                
                for j in row:
                    new_row.append(int(j)/50000)
                self.data.append(new_row)                

        return self.data
    
    def to_csv(self):
        with open("output_file.csv", 'w') as csvfile:
            writer = csv.writer(csvfile)    
            for i in self.to_list():
                writer.writerow(i)
        return None
    
