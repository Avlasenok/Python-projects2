from datetime import date, timedelta
import datetime

CurrentDate = datetime.datetime.strptime(input(), "%Y %m %d")
CurrentDate += timedelta(days=int(input()))
print(CurrentDate.strftime("%Y %-m %-d"))