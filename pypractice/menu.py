from PyQt5.QtCore import *

now = QDate.currentDate()
time = QTime.currentTime()
datetime = QDateTime.currentDateTime()
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString())
print('Local datetime: ', datetime.toString())
print('Universal datetime: ', datetime.toUTC().toString())

xmas1 = QDate(2018, 12, 24)
xmas2 = QDate(2019, 12, 24)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print("{0} days have passed since last XMas".format(dayspassed))

nofdays = now.daysTo(xmas2)
print("There are {0} days until next XMas".format(nofdays))
