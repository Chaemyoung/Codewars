import math

def to_industrial(time_for_in):
    time_str = str(time_for_in)
    if ':' in time_str:
        parts = time_str.split(':')
        minutes = int(parts[0])
        seconds = int(parts[1])
        total_seconds = minutes * 60 + seconds
        in_answer = round(total_seconds / 60, 2)
    else:
        in_answer = round(int(time_str) / 60, 2)
    return in_answer

def to_normal(time):
    s,m = math.modf(time)
    mm = math.trunc(m)
    ss = s*60
    sss = round(ss,0)
    ssss = math.trunc(sss)
    no_time = f"{mm}:{ssss:02d}"
    return str(no_time)
