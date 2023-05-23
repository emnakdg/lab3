day = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year (e.g. 2023): "))


a = (14 - month) // 12
y = year - a
m = month + 12 * a - 2
d = (day + y + y//4 - y//100 + y//400 + (31*m)//12) % 7


weekday = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')

print("The date %d/%d/%d falls on a %s." % (day, month, year, weekday[d])) 