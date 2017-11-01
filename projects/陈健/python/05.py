#计算某年月日是该年的第几天

def Judgeyear(year):
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return 1
    else:
        return 0


def Calculatedays(year,month,day):

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daynum = 0
    monthnum = 1

    if(Judgeyear(year) == 1) :
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in months:
        if (monthnum < month):
            daynum += i
            monthnum += 1

    daynum = (day + daynum)
    print(daynum)


Calculatedays(2017,11,1)
