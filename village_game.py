import sys
import os
import time
import random
import json
def log(msg, answ, err=""):
	os.popen('echo "#__'+str(err)+'__######'+str(msg)+',[\''+str(answ)+',\']'+'##########" >> VillageGameAutoplay/village_game.log')
msg=sys.argv
msg.pop(0)
msg=str(msg)
msg=msg.replace("\\n","")
t=random.randrange(30,100)/15
settings=json.loads(os.popen("cat VillageGameAutoplay/setting.json").read())
answ=0
fight=settings["fight"]
quest=settings["quest"]
pause=settings["pause"]
if pause == 1:
	fight=0
	quest=0
#quest
if "Completa le missioni, vinci e guadagnarai" in msg and quest:
	time.sleep(t)
	answ="⭐️⭐️⭐️Difendi il villaggio"
	log(msg,answ)
elif "I banditi hanno attaccato il villaggio" in msg and quest:
	if not quest:
		t=0.3
	time.sleep(t)
	answ="Inizia missione🗡"
	log(msg,answ)
elif "I banditi sono dei tipacci davvero cattivi" in msg and quest:
	if not quest:
		t=0.3
	time.sleep(t)
	answ="Manda rinforzi! 🗡"
	log(msg,answ)
#fight
elif "Puoi combattere con altri giocatori" in msg and fight:
	time.sleep(t)
	answ="Cerca avversario👁"
	log(msg,answ)
elif "Per attaccare, hai bisogno di" in msg and fight:
	if not fight:
		t=0.3
	time.sleep(t)
	answ="Attacca!⚔"
	log(msg,answ)
elif "Durante la battaglia, il nemico ha circondato" in msg and fight:
	if not fight:
		t=0.3
	time.sleep(t)
	answ="Manda rinforzi!🗡"
	log(msg,answ)
#rest
elif "Lavoro completato, mio signore" in msg:
	time.sleep(t)
	answ="/work"
	log(msg,answ)
elif "I tuoi campi sono pieni." in msg:
	time.sleep(t)
	answ="/harvest"
	log(msg,answ)
else:
	log(msg,answ,"ERROR")

if answ != 0:
	print(answ)
