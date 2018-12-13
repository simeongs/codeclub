import datetime 

def how_many_days(month, day):

  now = datetime.datetime.now()
  current_year = now.year
  birthday = datetime.datetime(current_year, month, day)

  if birthday < now:
    current_year += 1
    birthday = datetime.datetime(current_year, month, day)
  
  return birthday - now


print(how_many_days(11, 17))