year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
list1 = [31,29,31,30,31,30,31,31,30,31,30,31]
list2 = [31,28,31,30,31,30,31,31,30,31,30,31]
#pansuan
if (year % 400 == 0)  or (year % 4 ==0 ) and (year %100 !=0 ):
    for i in range(1,12):
        if month > i:
            day += list2[i]
else:
    for i in range(1,12):
        if month > i:
            day += list2[i]
print(day)