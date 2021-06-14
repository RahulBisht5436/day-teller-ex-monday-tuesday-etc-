
def day(d,m,y):
  if m==1:
    u=d


  if m==2:
    u=31+d
    print("working")


  if m==3:
    if y%4==0:
      u=31+29+d
    else:
      u=31+28+d


  if m==4:
    if y%4==0:
      u=31+29+31+d
    else:
      u=31+28+31+d



  if m==5:
    if y%4==0:
      u=31+29+31+30+d
    else:
      u=31+28+31+30+d

  
  if m==6:
    if y%4==0:
      u=31+31+31+30+29+d
    else:
      u=31+28+31+31+30+d

  
  if m==7:
    if y%4==0:
      u=31+31+31+30+30+29+d
    else:
      u=31+28+d+31+31+30+30

  
  if m==8:
    if y%4==0:
      u=31+31+31+31+30+30+29+d
    else:
      u=31+28+d+31+31+31+30+30+30

  
  if m==9:
    if y%4==0:
      u=31+29+d+31+31+31+31+30+30+30
    else:
      u=31+28+d+31+31+31+31+30+30+30+30

  
  if m==10:
    if y%4==0:
      u=31+29+d+31+31+31+31+30+30+30+30+31
    else:
      u=31+28+d+31+31+31+31+30+30+30+30+31

  
  if m==11:
    if y%4==0:
      u=31+29+d+31+31+31+31+30+30+30+30+31+30
    else:
      u=31+28+d++31+31+31+31+30+30+30+30+31+30

  
  if m==12:
    if y%4==0:
      u=31+29+d+31+31+31+31+31+30+30+30+30+31+30
    else:
      u=31+28+d+31+31+31+31+30+30+30+30+31+30+31

  return u    

def day1(date_):
  z=4
  if (date_+z)%7==1:
    print("monady")
  elif (date_+z)%7==2:
    print("tuesday")  
  elif (date_+z)%7==3:
    print("wednesday")  
  elif (date_+z)%7==4:
    print("thusday")  
  elif (date_+z)%7==5:
    print("friday")  
  elif (date_+z)%7==6:
    print("saturday")  
  elif date_%7==0:
    print("sunday")  
    
d=int(input("enter date"))
m=int(input("enter month"))
y=int(input("enter year"))
ply=int(((y-1)-20)/4)
date_=day(d,m,y)
date_=date_+ply+(y-21)*365
day1(date_)


  
  
        


