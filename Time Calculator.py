import time as t
import calendar

def add_time(start, duration,day=""):
    
    day_change=0
    
    start=start.split()
    time = start[0].split(':')
    timezone=start[1]
    
    duration=duration.split()
    add_time = duration[0].split(':')
    
    new_time = [int(time[0])+int(add_time[0]),int(time[1])+int(add_time[1])]
    
    #managing over minutes
    if(new_time[1]>=60):
        new_time[0]+=1
        new_time[1]-=60
    
    #managing over hours
    while(new_time[0]>=12):
        if(new_time[0]>=24):
            new_time[0]-=24
            day_change+=1
            continue;
        if timezone=="AM" and new_time[0]>=12:
            new_time[0]-=12
            timezone="PM"
        elif timezone=="PM" and new_time[0]>=12:
            new_time[0]-=12
            timezone="AM"
            day_change+=1
    
    if(new_time[1]<10):
        new_time[1]="0"+str(new_time[1])
    if(new_time[0]==0):
        new_time[0]=12
    formatted_time = new_time[0],":",new_time[1]," ",timezone
    formatted_time = list(formatted_time)
    formatted_time = ''.join(map(str, formatted_time))
    
    if day:
        day=day.lower()
        day_no = t.strptime(day, "%A").tm_wday
        day_no = day_no + day_change
        
        while(day_no>6):
            day_no-=7
        
        day = calendar.day_name[day_no]
        
        if(day_change == 0):
            print(formatted_time +", "+ day)
        elif(day_change==1):
             print(formatted_time+", "+ day +" (next day)")
        else: 
            print(formatted_time+", "+ day +" ("+str(day_change)+" days later)")
    
    else:
        if(day_change == 0):
            print(formatted_time)
        elif(day_change==1):
             print(formatted_time +" (next day)")
        else: 
            print(formatted_time +" ("+str(day_change)+" days later)")
    
    
add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
add_time("8:16 PM", "466:02", "tuesday")