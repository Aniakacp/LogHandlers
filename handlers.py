import json
import csv
import sqlite3
from profillogger import *

class Handler():
    def __init__(self, file):
        self.file=file

    def read(self):
        pass

    def write(self, logentry):
        pass

class CSVHandler(Handler):
    def __init__(self, file):
        super().__init__(file)

    def read(self):
        table_logs=[]
        with open(self.file, "r") as f:
            lines = f.readlines()
            for line in lines:
                args= line.replace('\n', '').split(',')

                lg= LogEntry(date=args[0], level= args[1],  msg=args[2])
                table_logs.append(lg)
        f.close()
        return table_logs

    def write(self, logentry):
        with open(self.file, "a") as f:
            f.writelines(logentry)
        f.close()

class FileHandler(Handler):
    def __init__(self, file):
        super().__init__(file)

    def read(self):
        table_logs = []
        with open(self.file, "r") as f:
            lines = f.readlines()
            for line in lines:
                args = line.replace('\n', '').split(',')
                lg = LogEntry(date=args[0], level=args[1], msg=args[2])
                table_logs.append(lg)
        f.close()
        return table_logs

    def write(self, logentry):
        with open(self.file, "a") as f:
            f.writelines(logentry)
        f.close()

class JsonHandler(Handler):
    def __init__(self, file):
        super().__init__(file)

    def read(self):
        table_logs = []
        with open(self.file, 'r') as f:
            data = json.load(f)
            print(data)
                #lg = LogEntry(date= line['date'], level = line['level'], msg = line['msg'])
                #table_logs.append(lg)
        f.close()
        return table_logs

    def write(self, logentry):
        with open(self.file, "a+") as f:
            logentry= {"date": "06/26/2021 18:16:19", "level": "INFO", "msg": "Some info message"}
            json.dump(logentry, f)
            f.write("\n")
        f.close()

def SQLLiteHandler(file):
    con = sqlite3.connect("db.sqlite")
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM django_session;'):
        print(row)
    con.close()

if __name__ == '__main__':
    # files
    csv_handler = CSVHandler("data_files/logs.csv")
    file_handler = FileHandler("data_files/logs.txt")
    json_handler = JsonHandler("data_files/logs.json")

    # read files:
    for logentry in csv_handler.read():
        print(logentry.date, logentry.level, logentry.msg)

    for logentry in file_handler.read():
        print(logentry.date, logentry.level, logentry.msg)


    for logentry in json_handler.read():
        print(logentry.date, logentry.level, logentry.msg)

    # create logs:
    logger = ProfilLogger(handlers=[file_handler, csv_handler])

    # set minimal level:
    logger.set_log_level(level="INFO")

    # create LogEntries:
    a = logger.info(msg="Some info message")

    # write logs into files:
    csv_handler.write(a)
    file_handler.write(a)
    json_handler.write(a)

#STEPS
#   logentry - how log looks like
#   handlers - reads form different format files (all have the same format)
#   ProfilLogger - set minimal level; create object LogEntries ready to save
#   handlers - writes LogEntries created in ProfilLogger
#   ProfilLoggerReader - find logs that meet the criteria


