def add_time(start, duration,day=""):
    
    day_change=0
    
    start=start.split()
    time = start[0].split(':')
    timezone=start[1]
    
    duration=duration.split()
    add_time = duration[0].split(':')
    
    new_time = [int(time[0])+int(add_time[0]),int(time[1])+int(add_time[1])]
    
    print(new_time)
    
    #managing over minutes
    if(new_time[1]>=60):
        new_time[0]+=1
        new_time[1]-=60
    
    if(new_time[1]<10):
        new_time[1]="0"+str(new_time[1])
    formatted_time = new_time[0],":",new_time[1]," ",timezone
    formatted_time = list(formatted_time)
    formatted_time = ''.join(map(str, formatted_time))
    
    print(formatted_time)
    
    
    
    
    
    
    
    #return new_time

add_time("11:43 AM", "00:20")

