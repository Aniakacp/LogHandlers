import json
import csv
import sqlite3
from logentry import *
import datetime
from handlers import *
from profillogger import *
from re import search, match, I

class ProfilLoggerReader():
    def __init__(self, handler):
        self.handler=handler

    def find_by_text(self, text, start_date= None, end_date=None):
        log_list=[]
        for logs in self.handler.read():
            if start_date and end_date==None:
                if start_date <= logs.date:
                    log_list.append(logs)
            if end_date and start_date==None:
                if end_date >= logs.date:
                    log_list.append(logs)
            if start_date and end_date:
                if start_date > end_date:
                    return print("error dates")
                else:
                    if end_date >= logs.date and start_date <= logs.date:
                        log_list.append(logs)
            else:
                if text in logs.msg and logs not in log_list:
                    log_list.append(logs)
        return log_list

    def find_by_regex(self, regex, start_date= None, end_date= None):
        log_list = []
        for logs in self.handler.read():
            if start_date and end_date == None:
                if start_date <= logs.date:
                    result = search(f"{regex}", logs.msg)
                    if result != None:
                        if result.group() in logs.msg and logs not in log_list:
                            log_list.append(logs)
            elif end_date and start_date==None:
                if end_date >= logs.date:
                    result = search(f"{regex}", logs.msg)
                    if result != None:
                        if result.group() in logs.msg and logs not in log_list:
                            log_list.append(logs)
            elif start_date and end_date:
                if start_date > end_date:
                    return print("error dates")
                else:
                    if end_date >= logs.date and start_date <= logs.date:
                        result = search(f"{regex}", logs.msg)
                        if result != None:
                            if result.group() in logs.msg and logs not in log_list:
                                log_list.append(logs)
            else:
                result = search(f"{regex}", logs.msg)
                if result != None:
                    if result.group() in logs.msg and logs not in log_list:
                        log_list.append(logs)
        if log_list == []:
            return print("regex not found in LogEntries")
        return log_list

    def groupby_level(self, start_date = None, end_date= None):
        levels={'CRITICAL':[], 'ERROR':[], 'WARNING':[], 'INFO':[], 'DEBUG':[]}
        for logs in self.handler.read():
            if start_date and end_date == None:
                if start_date <= logs.date:
                    if "CRITICAL" in logs.level and logs not in levels:
                        print(logs.date, logs.level)
                        levels['CRITICAL'].append(logs)
                    elif "ERROR" in logs.level and logs not in levels:
                        levels['ERROR'].append(logs)
                    elif "WARNING" in logs.level and logs not in levels:
                        levels['WARNING'].append(logs)
                    elif "INFO" in logs.level and logs not in levels:
                        levels['INFO'].append(logs)
                    elif "DEBUG" in logs.level and logs not in levels:
                        levels['DEBUG'].append(logs)
            elif end_date and start_date == None:
                if end_date >= logs.date:
                    if "CRITICAL" in logs.level:
                        levels['CRITICAL'].append(logs)
                    elif "ERROR" in logs.level:
                        levels['ERROR'].append(logs)
                    elif "WARNING" in logs.level:
                        levels['WARNING'].append(logs)
                    elif "INFO" in logs.level:
                        levels['INFO'].append(logs)
                    elif "DEBUG" in logs.level:
                        levels['DEBUG'].append(logs)
            elif start_date and end_date:
                if start_date > end_date:
                    return print("error dates")
                else:
                    if end_date >= logs.date and start_date <= logs.date:
                        if "CRITICAL" in logs.level:
                            levels['CRITICAL'].append(logs)
                        elif "ERROR" in logs.level:
                            levels['ERROR'].append(logs)
                        elif "WARNING" in logs.level:
                            levels['WARNING'].append(logs)
                        elif "INFO" in logs.level:
                            levels['INFO'].append(logs)
                        elif "DEBUG" in logs.level:
                            levels['DEBUG'].append(logs)
            else:
                if "CRITICAL" in logs.level:
                    levels['CRITICAL'].append(logs)
                elif "ERROR" in logs.level:
                    levels['ERROR'].append(logs)
                elif "WARNING" in logs.level:
                    levels['WARNING'].append(logs)
                elif "INFO" in logs.level:
                    levels['INFO'].append(logs)
                elif "DEBUG" in logs.level:
                    levels['DEBUG'].append(logs)
        return levels

    def groupby_month(self, start_date= None, end_date = None):
        year = { 'jan': [], 'feb': [], 'mar': [], 'apr':[], 'may': [], 'jun':[], 'jul':[], 'aug':[], 'sep':[], 'oct':[],'nov':[], 'dec':[]}
        for logs in self.handler.read():
            logs_month = int(logs.date.split(' ')[0].split('/')[0])
            if start_date and end_date == None:
                if start_date <= logs.date:
                    if logs_month==1:
                        year['jan'].append(logs)
                    if logs_month==2:
                        year['feb'].append(logs)
                    if logs_month==3:
                        year['mar'].append(logs)
                    if logs_month==4:
                        year['apr'].append(logs)
                    if logs_month==5:
                        year['may'].append(logs)
                    if logs_month==6:
                        year['jun'].append(logs)
                    if logs_month==7:
                        year['jul'].append(logs)
                    if logs_month==8:
                        year['aug'].append(logs)
                    if logs_month==9:
                        year['sep'].append(logs)
                    if logs_month==10:
                        year['oct'].append(logs)
                    if logs_month==11:
                        year['nov'].append(logs)
                    if logs_month==12:
                        year['dec'].append(logs)
            elif end_date and start_date == None:
                if end_date >= logs.date:
                    if logs_month==1:
                        year['jan'].append(logs)
                    if logs_month==2:
                        year['feb'].append(logs)
                    if logs_month==3:
                        year['mar'].append(logs)
                    if logs_month==4:
                        year['apr'].append(logs)
                    if logs_month==5:
                        year['may'].append(logs)
                    if logs_month==6:
                        year['jun'].append(logs)
                    if logs_month==7:
                        year['jul'].append(logs)
                    if logs_month==8:
                        year['aug'].append(logs)
                    if logs_month==9:
                        year['sep'].append(logs)
                    if logs_month==10:
                        year['oct'].append(logs)
                    if logs_month==11:
                        year['nov'].append(logs)
                    if logs_month==12:
                        year['dec'].append(logs)
            elif start_date and end_date:
                if start_date > end_date:
                    return print("error dates")
                else:
                    if end_date >= logs.date and start_date <= logs.date:
                        if logs_month == 1:
                            year['jan'].append(logs)
                        if logs_month == 2:
                            year['feb'].append(logs)
                        if logs_month == 3:
                            year['mar'].append(logs)
                        if logs_month == 4:
                            year['apr'].append(logs)
                        if logs_month == 5:
                            year['may'].append(logs)
                        if logs_month == 6:
                            year['jun'].append(logs)
                        if logs_month == 7:
                            year['jul'].append(logs)
                        if logs_month == 8:
                            year['aug'].append(logs)
                        if logs_month == 9:
                            year['sep'].append(logs)
                        if logs_month == 10:
                            year['oct'].append(logs)
                        if logs_month == 11:
                            year['nov'].append(logs)
                        if logs_month == 12:
                            year['dec'].append(logs)
            else:
                if logs_month == 1:
                    year['jan'].append(logs)
                if logs_month == 2:
                    year['feb'].append(logs)
                if logs_month == 3:
                    year['mar'].append(logs)
                if logs_month == 4:
                    year['apr'].append(logs)
                if logs_month == 5:
                    year['may'].append(logs)
                if logs_month == 6:
                    year['jun'].append(logs)
                if logs_month == 7:
                    year['jul'].append(logs)
                if logs_month == 8:
                    year['aug'].append(logs)
                if logs_month == 9:
                    year['sep'].append(logs)
                if logs_month == 10:
                    year['oct'].append(logs)
                if logs_month == 11:
                    year['nov'].append(logs)
                if logs_month == 12:
                    year['dec'].append(logs)
        return year

if __name__ == '__main__':
    file_handler = FileHandler("data_files/logs.txt")
    log_reader = ProfilLoggerReader(handler=file_handler)

    print('find by text')
    find_text= log_reader.find_by_text("Some debug message", start_date="06/26/2021 18:26:09", end_date="07/26/2021 18:24:05")
    if find_text:
        for logentry in find_text:
            print(logentry.date, logentry.level, logentry.msg)

    print("\n")
    print('find by regex')
    log_regex= log_reader.find_by_regex(f"[a-z A-z]+ info", start_date="06/26/2021 18:23:56", end_date="06/26/2021 18:24:05")
    if log_regex:
        for logentry in log_regex:
            print(logentry.date, logentry.level, logentry.msg)

    print("\n")
    print('Group by level')
    group_level= log_reader.groupby_level(start_date="06/26/2021 18:24:05", end_date="06/26/2021 18:26:04")
    if group_level:
        print(group_level)
        for logentry in group_level['CRITICAL']:
            print("CRITICAL:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_level['ERROR']:
            print("ERROR:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_level['WARNING']:
            print("WARNING:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_level['INFO']:
            print("INFO:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_level['DEBUG']:
            print("DEBUG:", logentry.date, logentry.level, logentry.msg)

    print("\n")
    print('Group by month')
    group_month= log_reader.groupby_month(start_date="06/26/2021 18:24:05", end_date="06/26/2021 18:26:04")
    if group_month:
        print(group_month)
        for logentry in group_month['jan']:
            print("jan:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['feb']:
            print("feb:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['mar']:
            print("mar:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['apr']:
            print("apr:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['may']:
            print("may:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['jun']:
            print("jun:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['aug']:
            print("aug:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['sep']:
            print("sep:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['oct']:
            print("oct:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['nov']:
            print("nov:", logentry.date, logentry.level, logentry.msg)
        for logentry in group_month['dec']:
            print("dec:", logentry.date, logentry.level, logentry.msg)