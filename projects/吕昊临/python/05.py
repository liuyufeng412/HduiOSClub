if __name__=="__main__":
    tmp_str="2008/3/1"
    year,month,day = list(map(int,tmp_str.split("/")))
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    result=day
    for i in range(month-1):
        result+=days[i]
    if ((year%400==0) or (year%4==0 and year%100!=0)) and month>2:
        result+=1
    print(result)

