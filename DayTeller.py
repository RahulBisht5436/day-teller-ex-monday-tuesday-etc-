def day(y,x):
  
  if x%7==y:
    print("wednesday")
  elif x%7==y+1:
    print("thusday")
  elif x%7==y+2:
    print("friday")
  elif x%7==y+3:
    print("saturday")
  elif x%7==y+4:
    print("sunday")
  elif x%7==y+5:
    print("monady")
  else:
    print("tuesday")      

def month(z,x):
  y=z
  if y ==1:
    day(6,x)
  elif  y==2:
    day(3,x)
  elif  y==3:
    day(3,x)
  elif  y==4:
    day(0,x)
  elif  y==5:
    day(5,x)
  elif  y==6:
    day(2,x)
  elif  y==7:
    day(0,x)
  elif  y==8:
    day(4,x)
  elif  y==9:
    day(1,x)
  elif  y==10:
    day(6,x)
  elif  y==11:
    day(3,x)
  else:
    day(1,x)      

z=int(input("whats is month" ))
x=int(input("whats is  date" ))
month(z,x)                
