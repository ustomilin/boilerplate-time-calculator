week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, weekday = 0):
  # find start end duration hh and mm
  time_start, letters_start = start.split()
  h_start, m_start = time_start.split(':')
  h_dur, m_dur = duration.split(':')

  # calculate target hh and mm
  m_new = int(m_start) + int(m_dur)
  h_new = int(h_start) + int(h_dur)

  days = 0 # how many days passed
  letters_new = letters_start # AM - PM
  day_new = weekday # new name of weekday

  # if new minutes > 60 add additional hour
  if m_new > 60:
    m_new -= 60
    h_new += 1

  # if days > 0
  if h_new//24 > 0:
    days = h_new//24
    h_new = h_new - h_new//24*24

  #if hours > 12
  if h_new > 12 or (h_new == 12 and h_start != 12):
    h_new -= 12
    if h_new == 0:
      h_new = 12
    
    #change letters
    if letters_start == 'AM':
      letters_new = 'PM'
    else:
      letters_new = 'AM'
      days += 1 # add day if PM -> AM

  # add leading zero to minutes
  if m_new < 10:
    m_new = '0' + str(m_new)
    
  # built the answer 
  new_time = f"{h_new}:{m_new} {letters_new}"
  if weekday != 0:
    if days > 0:
      week_num = week.index(weekday.capitalize())
      day_new = week[(week_num+days)%7] 
    new_time += f", {day_new}"
  
  if days == 1:
    new_time += f" (next day)"
  elif days > 1:
    new_time += f" ({days} days later)"

  return new_time
