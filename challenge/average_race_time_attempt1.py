# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k
# runners from the Association of Road Racing Statisticians

import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    result = []
    for row in races.split('\n'):
        if 'Jennifer Rhines' in row:
            time = row[3:12].strip()
            result.append(time)
    
    return result


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding)"""
    racetimes = get_rhines_times()
    total = datetime.timedelta()
    for racetime in racetimes: 
        minute, second, milli_sec = getTimeValues(racetime)
        total += datetime.timedelta(
            minutes=int(minute),
            seconds=int(second),
            milliseconds=int(milli_sec)
        )
            
    return f'{total / len(racetimes)}'[2:-5]


def getTimeValues(racetime, milli_sec=0):
    minute = racetime.split(':')[0]
    second = racetime.split(':')[1].split('.')[0]
    if len(racetime) > 5:
        milli_sec = racetime.split(':')[1].split('.')[0]

    return minute, second, milli_sec


print(get_average())