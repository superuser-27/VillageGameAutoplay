import sys
import os
import time
import random
import json
def log(msg, answ, err=""):
	os.popen('echo "#__'+str(err)+'__######'+str(msg)+',[\''+str(answ)+',\']'+'##########" >> VillageGameAutoplay/village_game.log')
msg=sys.argv[1]
usr=sys.argv[2]
msg=str(msg)
usr=str(usr)
msg=msg.replace("\\n","")
t=random.randrange(30,100)/15
settings=json.loads(os.popen("cat VillageGameAutoplay/setting_"+usr+".json").read())
answ=0
fight=settings["fight"]
quest=settings["quest"]
pause=settings["pause"]
if pause == 1:
	fight=0
	quest=0
#quest
if "You can choose a quest, which performing" in msg and quest:
	time.sleep(t)
	answ="⭐️⭐️⭐️Save the village"
	log(msg,answ)
elif "Bandits attacked a village" in msg and quest:
	if not quest:
		t=0.3
	time.sleep(t)
	answ="Run quest🗡"
	log(msg,answ)
elif "The bandits were some strong guys" in msg and quest:
	if not quest:
		t=0.3
	time.sleep(t)
	answ="Send reinforcements! 🗡"
	log(msg,answ)
#fight
elif "You can fight against other players and win medals" in msg and fight:
	time.sleep(t)
	answ="Search opponent👁"
	log(msg,answ)
elif "Your opponent is" in msg and fight:
	val=[int(s) for s in msg.split() if s.isdigit()]
	if not fight:
		t=0.3
	time.sleep(t)
	if val[len(val)-4]>val[len(val)-5]:
		answ="Attack!⚔"
	else:
		answ="Search opponent👁"
	log(msg,answ)
elif "During the battle, the enemy raised a militia" in msg and fight:
	if not fight:
		t=0.3
	time.sleep(t)
	answ="Send reinforcement!🗡"
	log(msg,answ)
#rest
elif "Work is finished" in msg:
	time.sleep(t)
	answ="/work"
	log(msg,answ)
elif "Your fields are filled." in msg:
	time.sleep(t)
	answ="/harvest"
	log(msg,answ)
elif "you have no money" in msg and quest:
	time.sleep(t)
	answ="/quests"
else:
	log(msg,answ,"ERROR")

if answ != 0:
	print(answ)
