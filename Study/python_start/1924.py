m, d = map(int, input().split(' '))
total_day = 0 
day31 = [1,3,5,7,8,10,12]
day30 = [4,6,9,11]
day28 = [2]
day = ['SUN','MON', 'TUE', 'WED', 'THU','FRI','SAT']
if m == 1:
    print(day[d%7])
else:
    m-=1
    while m != 0:
        if m in day30:
            total_day += 30 
        elif m in day31:
            total_day += 31 
        elif m in day28:
            total_day += 28 
        m -=1 
    total_day += d

    print(day[total_day%7])

    