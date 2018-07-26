#Program to calculate age in years,months,days,hours,minutes,seconds,miliseconds
import time, datetime

date_of_birth = input('Enter Date of birth in this format "YYYY-MM-DD" :-')

def calc_age(date_of_birth):
    birth_date = date_of_birth.split('-')
    time_now = datetime.datetime.now()
    time_birth = datetime.datetime(int(birth_date[0]),int(birth_date[1]), int(birth_date[2]))
    age = time_now - time_birth 

    years = age.days//365
    days = age.days%365
    months = days//31
    daysleft= days%31 -7
    age_in_days= age.days
    hours = age.seconds//3600
    age_in_hours=age_in_days*24
    minutes = (age.seconds//60)%60
    age_in_minutes = age_in_hours*60
    age_in_seconds = age_in_minutes*60
    seconds = age.seconds%60
    agemon = age.days//365*12 + months
    ageweek = age.days//7
    ageweek1 = age.days%7
    age_in_miliseconds = age_in_seconds*100
    return agemon,years,ageweek,ageweek1, days,daysleft,months, hours, minutes, seconds,age_in_days,age_in_hours,age_in_minutes,age_in_seconds,age_in_miliseconds
 
def Printage():
    agemon,years,ageweek,ageweek1, days,daysleft,months, hours, minutes, seconds,age_in_days,age_in_hours,age_in_minutes,age_in_seconds,age_in_miliseconds = calc_age(date_of_birth)
    print (years, 'Years',months,'Months', daysleft, 'Days', hours, 'Hours', minutes, 'Minutes', seconds, 'Seconds')
    print (agemon, 'months',months,'Months', daysleft, 'Days', hours, 'Hours', minutes, 'Minutes', seconds, 'Seconds')
    print(ageweek,'Weeks',ageweek1,'days')
    print ("",years, 'Years\n', age_in_days, 'Days\n', age_in_hours, 'Hours\n', age_in_minutes, 'Minutes\n', age_in_seconds, 'Seconds\n',age_in_miliseconds,'Miliseconds')
    time.sleep(1)
Printage()