#!/usr/bin/env python
from datetime import datetime

curDay=datetime.now().weekday()
if curDay==0:
    dayOfWeek='Monday'
elif curDay==1:
    dayOfWeek='Tuesday'
elif curDay==2:
    dayOfWeek='Wednesday'
elif curDay==3:
    dayOfWeek='Thursday'
elif curDay==4:
    dayOfWeek='Friday'
elif curDay==5:
    dayOfWeek='Saturday'
else:
    print "No school on Sunday lol"
    quit()

timetable = {
    'Monday' : [ '8:30-9:30 Physics/Chemistry Practicals', '9:30-10:10 Chemistry', '10:10-11:20 English', '11:20-11:35 Break', '11:35-2:30 SME Classes' ],
    'Tuesday' : [ '8:30-8:50 Assembly', '8:50-10:10 IP', '10:10-11:20 Maths', '11:20-11:35 Break', '11:35-2:30 SME Classes'],
    'Wednesday' : ['8:30-9:30 IP', '9:30-10:10 LSO/WE', '10:10-11:20 Physics/Chemistry Practicals', '11:20-11:35 Break', '11:35-2:30 SME Classes'],
    'Thursday' : ['8:30-9:30 Physics', '9:30-10:10 English', '10:10-11:20 IP', '11:20-11:35 Break', '11:35-2:30 SME Classes'],
    'Friday' : ['8:30-10:10 Balewadi/SKP/Whatever', '10:10-10:25 Break', '10:25-11:35 English', '11:35-2:30 SME Classes'],
    'Saturday': ['9:00-9:35 Physics', '9:35-10:10 IP', '10:10-10:45 Mathematics', '10:45-11:20 Chemistry', '11:20-11:35 Break', '11:35-2:30 SME Classes']
    }

for x in timetable[dayOfWeek]:
    print x
