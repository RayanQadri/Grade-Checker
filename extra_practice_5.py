m=input("Please enter your given marks.")
if m<25 and m>0:
  print "You have earned a F"
  print "Yikes! That's not a passing grade."
elif m>=25 and m<45:
  print "You have earned an E!"
  print "E isn't enough to pass..Keep working hard!"
elif m>=45 and m<50:
  print "You have earned a D!"
  print "Keep progressing you'll make it, D wouldn't unfortunately."
elif m>=50 and m<60:
  print "You have earned a C!"
  print "You have passed, but not by much! A little drop in your grade can make you fail.."
elif m>=60 and m<80:
  print "You have earned a B!"
  print "You've passed, Great! Just need to go above and beyond to achieve the greatest level."
elif m>80 and m<=100:
    print "You have earned an A!"
    print "You reached the master level of success! Keep it up!" 
else:
    print "You have entered an invalid Grade.."