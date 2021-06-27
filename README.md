LogHandles aplication reads and logs LogEntries from specific format of files (txt, csv, json)

Files:
- logentry.py - LogEntry structure 
- profillogger.py - ProfilLogger can set minimal level and create object LogEntries ready to save
- handlers.py - Handlers read LogEntries form different format files and save LogEntries created in ProfilLogger (all have the same format)
- profilogerreader.py - ProfilLoggerReader searches for logs that meet different criterias (find in text, find by regex, group by month, group by level

Log Levels:
DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
