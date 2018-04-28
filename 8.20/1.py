#!usr/bin/python
import datetime
Today=datetime.date.today()
Today-datetime.date(Today.year,1,1)+datetime.timedelta(days=1)
Today.timetuple().tm_yday
Today.replace(year=2017)
Today.replace(month=1)
now=datetime.datetime.now()
now.replace(second=30)
now+datetime.timedelta(days=5)
now+datetime.timedelta(weeks=-5)
#标准库calendar操作方法
import calendar
print(calendar.calendar(2017))
print(calendar.month(2017.8))
calendar.isleap(2017)
calendar.weekday(2017.9)
#模拟
from datetime import date
daysofMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
def myCalendar(year,month):
    #获取year年month月1日是周几
    start=date(year,month,1),timetuple().tm_wday
    #打印头部信息
    print('{0}年{1}月日历'.format(year,month).center(56))
    print('\t'.join('日一二三四五六'.split()))
    #获取该月有多少天，如果是二月并且是闰年，适当调整
    day=daysofMonth[month-1]
    if month==2:
        if year%400==0 or(year%100!=0):
            day+=1
    #生成数据，根据需要在前方填充空白
    result=[''*8 for i in range(start+1)]
    result+=list(map(lambda d: str(d).ljust(8),range(1,day+1)))
    #打印数据
    for i,day in enumerate(result):
        if i!=0 and i%7==0:
            print()
        print(day,end='')
    print()
def main(year,month=-1):
    if type(year)!=int or year<1000 or year>10000:
        print('year error')
        return
    if type(month)==int:
    #如果未指定月那就全年日历
        if month==-1:
              for m in range(1,13):
                  myCalendar (year,m)
    #如果指定了月，那就打印月历
        elif month in range(1,13):
              myCalendar (year,month)
        else:
              print('Month error')
              return
    else:
       print('Month error')
       return
main(2017)
