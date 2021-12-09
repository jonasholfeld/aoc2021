import math

def countAfterDays(days):
    if(days < 2):
        return 1
    progeny = math.floor((days - 2)  / 6)
    



for i in range(0, 30):
    print(f'Nach {i} Tagen', countAfterDays(i))
