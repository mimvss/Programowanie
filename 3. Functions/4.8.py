def time_string(hours, minutes, format):
    if format == '24':
        hour_str = f"{hours:02d}"
        minute_str = f"{minutes:02d}"
        return f"{hour_str}:{minute_str}"
    elif format == '12':
        # określamy godzinę i am/pm
        if hours == 0:
            hour_12 = 12
            suffix = "am"
        elif 1 <= hours <= 11:
            hour_12 = hours
            suffix = "am"
        elif hours == 12:
            hour_12 = 12
            suffix = "pm"
        else:  # 13-23
            hour_12 = hours - 12
            suffix = "pm"
        
        minute_str = f"{minutes:02d}"
        return f"{hour_12}:{minute_str}{suffix}"
    else:
        return "wrong format"

# Testy
print(time_string(15, 38, '24'))  
print(time_string(8, 3, '24'))    
print(time_string(0, 5, '24'))    
print(time_string(11, 15, '12'))  
print(time_string(0, 7, '12'))    
print(time_string(7, 30, '12'))   
print(time_string(12, 46, '12'))  
print(time_string(13, 10, '12'))  
print(time_string(19, 2, '12'))   
