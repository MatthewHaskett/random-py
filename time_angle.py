import time
 
min = int(time.strftime("%M"))
hour = int(time.strftime("%H")) % 12
 
min_angle = min * 6
hour_angle = int((hour * 30) + (30 * (min/60)))
 
between = abs(min_angle - hour_angle)
 
if min_angle > 180:
    between = 360 - between
    
print(str(between) + "°")
