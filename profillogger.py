from handlers import *
from logentry import *

list_level = {
            "CRITICAL": 10,
            "ERROR": 20,
            "WARNING": 30,
            "INFO": 40,
            "DEBUG": 50
        }

class ProfilLogger:
    def __init__(self, handlers):
        self.handlers = handlers
        self.level= ""
        self.msg=""
        self.min_level= "CRITICAL"

    def set_log_level(self, level):
        self.min_level= level
        return self.min_level

    def info(self, msg):
        if list_level["INFO"] >= list_level[self.min_level]:
            self.level='INFO'
            log= LogEntry(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), level=self.level, msg=msg)
            return f"{log.date},{log.level},{log.msg}\n"
        else:
            return f"Minimal level is {self.min_level}, only LogEntries with higher level can be saved"

    def warning(self, msg):
        if list_level["WARNING"] >= list_level[self.min_level]:
            self.level = 'WARNING'
            log = LogEntry(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), level=self.level, msg=msg)
            return f"{log.date},{log.level},{log.msg}\n"
        else:
            return f"Minimal level is {self.min_level}, only LogEntries with higher level can be saved"

    def debug(self, msg):
        if list_level["DEBUG"] >= list_level[self.min_level]:
            self.level = 'DEBUG'
            log = LogEntry(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), level=self.level, msg=msg)
            return f"{log.date},{log.level},{log.msg}\n"
        else:
            return f"Minimal level is {self.min_level}, only LogEntries with higher level can be saved"

    def critical(self, msg):
        if list_level["CRITICAL"] >= list_level[self.min_level]:
            self.level = 'CRITICAL'
            log = LogEntry(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), level=self.level, msg=msg)
            return f"{log.date},{log.level},{log.msg}\n"
        else:
            return f"Minimal level is {self.min_level}, only LogEntries with higher level can be saved"

    def error(self, msg):
        if list_level["ERROR"] >= list_level[self.min_level]:
            self.level = 'ERROR'
            log = LogEntry(datetime.now().strftime("%m/%d/%Y %H:%M:%S"), level=self.level, msg=msg)
            return f"{log.date},{log.level},{log.msg}\n"
        else:
            return f"Minimal level is {self.min_level}, only LogEntries with higher level can be saved"

if __name__ == '__main__':
    csv_handler = CSVHandler("data_files/logs.csv")
    file_handler = FileHandler("data_files/logs.txt")
    logger = ProfilLogger(handlers=[file_handler,csv_handler])

    logger.set_log_level(level="INFO")
    a= logger.info(msg= "Some info message")
    print(f'New LogEntry (not saved): {a}')




