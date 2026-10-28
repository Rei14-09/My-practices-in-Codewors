from datetime import date

def age_in_days(year, month, day):
    
    birth = date(year, month, day)
    
    today = date.today()
    
    difference = today - birth
    
    sol = difference.days
    
    return f'You are {sol} days old'

    if __name__ in '__mine__':
        assert age_in_days(2024,11,11) == 2
        assert age_in_days(2014,11,11) == 12