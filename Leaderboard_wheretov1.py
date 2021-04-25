
from collections import OrderedDict


import os
from time import sleep


# The screen clear function
def screen_clear ():
# for mac and linux(here, os.nam
    if os. name == 'posix' :
        _ = os. system( 'clear' )
    else :
# for windows platfrom
         _ = os. system( 'cls' )
# print out some text
         print ( "The platform is: " , os . name)
         print ( "big output\n" * 5 )
# wait for 5 seconds to clear scree
         sleep ( 0.3)
# now call function we defined above


screen_clear ()


print()
print("SCORE LEADERBOARD FOR 'WHERE TO?' ")
print()
print()



#Mood=input ("how far? ")
#TextFileDatabase=open("storage/sdcard0/LeaderboardGame/leaderboardDatabaseWT.txt", "a")
#TextFileDatabase.write(Mood)



d = {}#"rocket": 3, "Chinedu": 1, "precious": 4, "shegz": 2}
#for k, v in d.items():
		#print ("%s: %s" % (k, v))

with open("storage/sdcard0/LeaderboardGame/leaderboardDatabaseWT.txt") as f:
		for line in f:
				(key, val)=line.split()
				d[key]=val 


d_sorted_by_value = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
#The OrderedDict behaves like a normal dict:
Eindex =0
for k, v in d_sorted_by_value.items():
				Eindex+=1
				#for i, h in d_sorted_by_value.items():
				print ("%s. %s-------- %s" % (Eindex, k, v))







