# 3️⃣ Dates & Times ✌️
import datetime as dt
import time as tm

tm.time()  # returns the current time in seconds since the Epoch

dateTimeNow = dt.datetime.fromtimestamp(tm.time())  # 2022-01-31 03:35:04.443987
formatDate = dateTimeNow.day, dateTimeNow.month, dateTimeNow.year  # 31 1 2022

# Compare dates
delta = dt.timedelta(days=100)  # create day from 100 days !, That's all
today = dt.date.today()
print(today > today + delta)
