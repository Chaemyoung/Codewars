import math

def make_readable(seconds):
    
    hours = int((seconds/3600))
    minutes = int((seconds - (hours*3600))/60) 
    seconds = int(seconds - (hours * 3600) - (minutes * 60))


    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
