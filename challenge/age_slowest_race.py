# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days
from datetime import date, timedelta
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
    

def get_age_slowest_times(timesAndAges):
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
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


def calculate_age(eventDate):
    rhinesBirthDay = date(1974, 7, 1)
    return (
        eventDate.year - rhinesBirthDay.year -
        ((rhinesBirthDay.month, rhinesBirthDay.day) 
            < (eventDate.month, eventDate.day))
    )


def main():
    data = get_data()
    timesAndAges = []
    for line in data.split('\n')[1:]:
        if 'Jennifer Rhines' in line:
            eventDateStr = get_event_date(line)
            day, month, year = eventDateStr.split()
            currentDate = date(day=day, month=month, year=year)
            timesAndAges.append((eventDateStr, calculate_age(currentDate)))

    slowest = get_age_slowest_times(timesAndAges)
    return slowest