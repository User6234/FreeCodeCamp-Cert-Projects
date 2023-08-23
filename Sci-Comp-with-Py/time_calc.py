from math import floor
from math import isclose

def add_time(start, duration, day="blank"):
    diw=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if duration=="0:00":
        return start
    if duration=="24:00":
        if day!="blank":
            if day.lower().title()=="Sunday":
                return f"{start}, Monday (next day)"
            else:
                return f"{start}, {diw[diw.index(day.lower().title())+1]} (next day)"
        else:
            return f"{start} (next day)"
    #hours in day/minutes in hour/days in week
    hid=12
    mih=60

    #formatting
    st=start.split(":")
    dr=duration.split(":")
    dr[1]=dr[1].lstrip("0")
    st[1]=st[1].lstrip("0")
    st[1]=st[1].replace(" AM","")
    st[1]=st[1].replace(" PM","")
    ampm=start.split(" ")[1]
    mn=eval(st[1])+eval(dr[1])
    hr=eval(st[0])+eval(dr[0])
    
    #make 24 hour clock proper if PM
    if ampm=="PM":
        fhd=hr+12
    else:
        fhd=hr
    #make overflow for minutes to hours
    if mn%mih!=mn:
        hr+=1
    #make overflow for hours to alter AM/PM state
    if hr%hid!=hr:
        if ampm=="PM":
            ampm="AM"
        elif ampm=="AM":
            ampm="PM"
    #overflow the hour and minute to get the correct time
    hr=hr%hid
    mn=mn%mih
    #format the minute with 0 padding
    if len(str(mn))==1:
        mn="0"+str(mn)
    #format the time string
    if hr==0:
        hr=12
    tm=str(hr)+":"+str(mn)+" "+ampm
    #calculate days
    if isclose((fhd/24)%7, 1.95, abs_tol=0.05):
        days=2
    else:
        days=floor(fhd/24)%14
    d2=floor(fhd/24)
    if day!="blank":
        dw=(diw.index(day.lower().title())+days)
        dw=diw[dw]
        tm=tm+", "+dw
    #determine if it's one or more days
    if days==1:
        tm=tm+" (next day)"
    if d2>=10:
        tm=tm+" ("+str(d2)+" days later)"
    elif days>1:
        tm=tm+" ("+str(days)+" days later)"

    #output
    return tm