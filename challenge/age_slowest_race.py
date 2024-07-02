""" Source of data: https://www.arrs.run/
 This dataset has race times for women 10k runners
 from the Association of Road Racing Statisticians
 Assume a year has 365.25 days
 """
from datetime import date, timedelta, datetime
from time import strptime


def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    return (line[0], calculate_age(get_event_date(line)))
    

def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    data = get_data()
    timesAndAges = []
    for line in data.split('\n')[1:]:
        if 'Rhines' in line:
            eventDateStr = get_event_date(line)
            currentDate = datetime.strptime(eventDateStr, '%d %b %Y')
            timesAndAges.append(
                (get_duration(line), calculate_age(currentDate)))
    s = strptime('00:00', '%M:%S')
    slowest = timedelta(minutes=s.tm_min, seconds=s.tm_sec)
    result = None
    
    for time, age in timesAndAges:
        t = strptime(time, '%M:%S')
        current = timedelta(minutes=t.tm_min, seconds=t.tm_sec)
        if current > slowest:
            slowest = current
            result = (age, time)
    return result


def get_event_date(line):
    day = line.split()[4][:5]
    month = line.split()[5][:5]
    year = line.split()[6][:5]

    return ' '.join([day, month, year])


def get_duration(line):
    return line.split()[0][:5]


def calculate_age(eventDate):
    rhinesBirthDay = date(1974, 7, 1)
    eventBeforeBirthday = (
        (rhinesBirthDay.month, rhinesBirthDay.day)
        > (eventDate.month, eventDate.day))
    
    year = eventDate.year - rhinesBirthDay.year + eventBeforeBirthday
    temp = datetime(
        year=rhinesBirthDay.year + year,
        day=rhinesBirthDay.day, month=rhinesBirthDay.month
    )

    if eventBeforeBirthday:
        daysDiff = abs(eventDate - temp)
    else:
        daysDiff = abs(temp - eventDate)

    age = str(year) + 'y' + str(daysDiff.days) + 'd'
    return age
    

