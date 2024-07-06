from collections import namedtuple

with open('olympics.txt', 'rt', encoding='utf-8') as file:    
    olympics = file.read()

medal = namedtuple('medal', ['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'])

medals = [] #Complete this - medals is a list of medal namedtuples
for entry in olympics.split('\n')[:-1]:
    entry_list = entry.split(';')
    new_entry = medal(*entry_list)
    medals.append(new_entry)


def get_medals(**kwargs):
    '''Return a list of medal namedtuples '''
    result = []
    
    for entry in medals:
        count = 0
        for col, val in kwargs.items():
            if getattr(entry, col) == val:
                count += 1
        if count == len(kwargs):
            result.append(entry)
    
    return result