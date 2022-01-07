import sys
def add_time(start, duration, day=False):

    time = start.split(":", 1)          
    time_dur = duration.split(":", 1)   
    h = int(time[0])                    
    h_d = int(time_dur[0])              
    days = int(h_d) // 24               
    days_a = days + 1                   
    days_2 = days * 24                  
    days_3 = int(h_d) - days_2          
    days_4 = int(h) + days_3            
    days_5 = days_4 - 12                
    time2 = time[1].split(" ")          
    time2_dur = time_dur[1].split(" ")  
    m = int(time2[0])                   
    m_d = int(time2_dur[0])            
    am_pm = time2[1]                    

    if day:
        ind = ["Sunday", "Monday", "tuesday", "Wednesday", "Thursday", "Friday", "saturDay"].index(day)
        count_start = ind
        
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        k = count_start
        lst1 = week[k:]
        lst2 = week[:k]
        final = lst1 + lst2

    if h_d == 0 and m_d == 0:
        if m < 10:
            return str(h) + ":" + "0" + str(m) + " " + am_pm
        else:
            return str(h) + ":" + str(m) + " " + am_pm
 
    if m + m_d < 59 and h + h_d < 12:
        if day:
            return str(h + h_d) + ":" + str(m + m_d) + " " + str(am_pm) + ", " + str(day)
        else:
            return str(h + h_d) + ":" + str(m + m_d) + " " + str(am_pm)

    if m + m_d < 59 and h + h_d > 12:
        h = (h + h_d) - 12
        if am_pm == "PM":
            am_pm = "AM"
        if h_d > 24:                
            if days_3 + h > 12:
                days = days + 1
                if day:
                    if days > 7:
                        new_end = days % 7
                        final = final[new_end]
                        return str(days_5) + ":" + str(m + m_d) + " " + str(am_pm) + ", " + str(final) + " (" + str(
                            days) + " days" + " later)"
                if m + m_d < 59:
                    return str(days_5) + ":" + str(m + m_d) + " " + str(am_pm) + " (" + str(days) + " days" + " later)"
        if m < 10:
            return str(h) + ":" + "0" + str(m + m_d) + " " + str(am_pm) + " (next day)"
        else:
            return str(h) + ":" + str(m + m_d) + " " + str(am_pm) + " (next day)"
            sys.exit(0)

    if m + m_d > 59 and h_d == 24:
        h = (h + h_d) + 1 - h_d
        m = (m + m_d) - 60
        if h + h_d == 12:
            if am_pm == "PM":
                am_pm = "AM"
            else:
                "AM"
            if m < 10:
                return str(h) + ":" + "0" + str(m) + " " + str(am_pm) + " (2 days later)"
            else:
                return str(h) + ":" + str(m) + " " + str(am_pm) + " (2 days later)"
    if m + m_d > 59 and h + h_d > 12:           
            h = (h + h_d) + 1 - 12
            m = (m + m_d) - 60
            if am_pm == "AM":
                am_pm = "PM"
            else:
                "AM"
            if m < 10:
                return str(h) + ":" + "0" + str(m) + " " + str(am_pm)
            else:
                return str(h) + ":" + str(m) + " " + str(am_pm)
    if m + m_d > 59 and h + h_d <= 12:       
            h = (h + h_d) + 1
            m = (m + m_d) - 60
            if am_pm == "AM":
                am_pm = "PM"
            else:
                "AM"
            if m < 10:
                return str(h) + ":" + "0" + str(m) + " " + str(am_pm)
            else:
                return str(h) + ":" + str(m) + " " + str(am_pm)

    if h_d == 24 and m_d == 00:         
        if day:
            if days < 7:
                final = final[days]
                return str(h) + ":" + str(m) + " " + str(am_pm) + ", " + str(final) + " (next day)"
        else:
            return str(h) + ":" + str(m) + " " + str(am_pm) + " (next day)"

    if h_d == 24 and m_d > 0:                   
        if am_pm == "PM":
            am_pm = "AM"
        else:
            "AM"
        if day:
            if days < 7:
                if m < 10:
                    final = final[days_a]
                    return str(h) + ":" + "0" + str(m) + " " + str(am_pm) + ", " + str(final) + " (2 days later)"
        if m < 10:
            return str(h) + ":" + "0" + str(m) + " " + str(am_pm) + " (2 days later)"
        else:
            return str(h) + ":" + str(m) + " " + str(am_pm) + " (2 days later)"

    if h_d > 24:                    
        if days_3 + h > 12:
            days = days + 1
            if m + m_d < 59:
                return str(days_5) + str(m + m_d) + am_pm + " (" + days + " later)"