import re

#  Getting the hour and the day by adding hours to a time 
def add_time(start, duration):
    time = int(start.split(" ")[0])
    days = 0
    if(re.search("PM",start)):
        time +=12
        output = time + duration
    else:
        output = time+duration

    days += output//24
    tim = output%24
    if tim > 12:
        print(f"{tim-12} PM in {days} days")
    else:
        print(f"{tim} AM in {days} days")
add_time("11 PM",1298)