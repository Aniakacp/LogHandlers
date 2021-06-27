import json
import csv
import sqlite3
from logentry import *
import datetime
from handlers import *
from profillogger import *

def FileHandlerWriter(file, logentry):
    with open(file, "a") as f:
        f.writelines(logentry)
    f.close()

def CSVHandlerWriter(file, logentry):
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow([logentry])
    f.close()

def JsonHandlerWriter(file, logentry):
    data = {}
    with open(file, 'a') as f:
        data["logs"].append({"date": "Anna", "level": "annabochenek.com", "msg": "Poland"})
        json.dump(data, f)
    f.close()

    data = {}
    data['logs'] = []
    with open('logs.json', 'w') as f:
        data["logs"].append({"date": "Anna", "level": "annabochenek.com", "msg": "Poland"})
        json.dump(data, f)
    f.close()

    with open('logs.json', 'r') as f:
        print(json.load(f))
    f.close()

def SQLLiteHandlerWriter(file):
    pass

if __name__ == '__main__':
    file_handler = FileHandler("logs.txt")  # file!
    csv_handler = CSVHandler("logs.csv")
    logger = ProfilLogger(handlers=[file_handler])  #obiekt
    logger.set_log_level(level="INFO")
    a= logger.info(msg= "Some info message")
    FileHandlerWriter("logs.txt", logentry=a)
    CSVHandlerWriter("logs.csv", logentry=a)
 #   JsonHandlerWriter("logs.json", logentry=a)
