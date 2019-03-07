import sys
from file_handler import FileHandler
from data_processing import CsvFileReader

file_info = FileHandler(sys.argv[1])

def valid(file):

    if file.file_ext() == ".csv":
        print("It's a csv file")
        return True
    else:
        print ("Unsupported data format!")
        return False


if __name__ == "__main__":
    if valid(file_info):
        csv = CsvFileReader(file_info.filename)
        csv.to_csv()

    