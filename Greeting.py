import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)
if(timestamp>=4 and timestamp<=12):
  print("Good Morning sir")
elif(timestamp>12 and timestamp<17):
  print("Good Afternoon sir")
elif(timestamp>17 and timestamp<20):
  print("Good Evening sir")
else:
  print("Good Night sir")
    