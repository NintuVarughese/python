import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
x = datetime.datetime(2018, 6, 1)

print(x.strftime("%j"))