def add_time(start, duration, optional=None):
    #split hour,mintues,period
    start_hour, start_minute, period = parse_time(start)

    hour_duration, minute_duration = duration.split(":")

    end_hour = int(start_hour)+int(hour_duration)
    end_minute = int(start_minute)+int(minute_duration)
    end_day = 0
    # Convert hour back to 12 hour time
    if end_minute > 60:
        end_minute = end_minute % 60
        end_hour = end_hour + 1
    
    if end_hour > 24:
        end_day = end_hour // 24
        end_hour = end_hour % 24
    
    if end_hour == 0 :
        end_hour =+ 12
    
    if 12 < end_hour < 24 :
        end_hour = end_hour -12
        period = "PM"
    else:
        period = "AM"

    
    
    new_time = "{}:{:02d} {}".format(end_hour, end_minute, period)
    
    day_in_week = {
        "Monday":0,
        "Tuesday":1,
        "Wednesday":2,
        "Thursday":3,
        "Friday":4,
        "Saturday":5,
        "Sunday":6
    }
    if optional:
        day_num = day_in_week[optional.title()]
        Day = {i for i in day_in_week if day_in_week[i] == ((day_num+end_day)%7)}
        new_time += ", " + " ".join(Day)
        if end_day == 1:
            new_time += " (next day)"
        elif end_day > 1:
            new_time += " ({} days later)".format(end_day)
    else:
        if end_day == 1:
            new_time += " (next day)"
        elif end_day > 1:
            new_time += " ({} days later)".format(end_day)
    return new_time
    # print(new_time)

def parse_time(t):
    start_hour, start_minute = t.split()[0].split(":")
    period = t.split()[1]
    if period != "AM":
        start_hour = str(int(start_hour) + 12)
    return start_hour, start_minute,period

# add_time("11:40 AM", "0:25")
