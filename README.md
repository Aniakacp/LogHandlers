LogHandles aplication reads and logs LogEntries from specific format of files (txt, csv, json)

Files:
- logentry.py - LogEntry structure 
- profillogger.py - ProfilLogger can set minimal level and create object LogEntries ready to save
- handlers.py - Handlers read LogEntries form different format files and save LogEntries created in ProfilLogger (all have the same format)
- profilogerreader.py - ProfilLoggerReader searches for logs that meet different criterias (find in text, find by regex, group by month, group by level

Log Levels:
DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL

Example usage:
csv_handler = CSVHandler("data_files/logs.csv")
file_handler = FileHandler("data_files/logs.txt")
json_handler = JsonHandler("data_files/logs.json")

logger = ProfilLogger(handlers=[file_handler, csv_handler])
logger.set_log_level(level="INFO")
a = logger.info( msg="Some info message")
file_handler.write(a)
json_handler.write(a)

file_handler = FileHandler("data_files/logs.txt")
log_reader = ProfilLoggerReader(handler=file_handler)

find_text= log_reader.find_by_text("Some debug message", start_date="06/26/2021 18:26:09", end_date="07/26/2021 18:24:05")
log_regex= log_reader.find_by_regex(f"[a-z A-z]+ info", start_date="06/26/2021 18:23:56", end_date="06/26/2021 18:24:05")
group_level= log_reader.groupby_level(start_date="06/26/2021 18:24:05", end_date="06/26/2021 18:26:04")
group_month= log_reader.groupby_month(start_date="06/26/2021 18:24:05", end_date="06/26/2021 18:26:04")
