import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour =int(input("Enter the time:1"))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning Mayank")

elif(hour>=12 and hour<17):
        print("Good Afternoon sir!")

if(hour>17 and hour<0):
      print("Good Night Mayank")
