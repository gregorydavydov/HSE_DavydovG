import ics
import pytz
import json
from datetime import datetime

with open('meetings.ics','r', encoding='utf-8') as f:
    calendar = f.read()
    calendar = ics.Calendar(calendar)
    events = calendar.events
    events_dict = {}
    data = []
    for event in events:
        events_dict = {
        'name': event.name,
        'begin': event.begin.datetime,
        'end': event.end.datetime,
        'location': event.location,
        'description': event.description,
        }
        name_value = events_dict['name'][18:33]# Определяем количество выводимых символов из 'name'
        start_time = event.begin.datetime
        end_time = event.end.datetime
        location = event.location
        if start_time == datetime(1, 1, 1, 0, 0, tzinfo=pytz.utc):
            if end_time == datetime(1, 1, 2, 0, 0, tzinfo=pytz.utc):
                if location == None:
                    continue

        data.append({
            'case_number': name_value,
            'start': str(start_time),
            'end': str(end_time),
            'location': location,
            'description': event.description
        })

with open('meetings.json','w') as meets2write:
    json.dump(data, meets2write)














