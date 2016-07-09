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
t=random.randrange(30,100)/10
settings=json.loads(os.popen("cat VillageGameAutoplay/setting.json").read())
answ=0
fight=settings["fight"]
quest=settings["quest"]
pause=settings["pause"]
if pause == 1:
	fight=0
	quest=0
#quest
if "Wähle eine Quest, sie durchzuführen wird etwas kosten" in msg and quest:
	time.sleep(t)
	answ="⭐️⭐️⭐️Das Dorf retten"
	log(msg,answ)
elif "Banditen haben ein Dorf angegriffen. Der Bürgermeister hat um Hilfe gebeten" in msg:
	if not quest:
		t=0.3
	time.sleep(t)
	answ="Quest starten🗡"
	log(msg,answ)
elif "Die Banditen sind starke Jungs —  sie haben deine Truppen in die Mangel genommen" in msg \
    or "Die Karawane wurde angegriffen und ihre Beschützer konnten sie nur knapp verteidigen" in msg \
    or "Deine Truppen sind nicht Herr der Lage" in msg:
	if not quest:
		t=0.3
	time.sleep(t)
	answ="Verstärkung schicken! 🗡"
	log(msg,answ)
#fight
elif "Du kannst gegen andere Spieler kämpfen um Medailen" in msg and fight:
	time.sleep(t)
	answ="Gegner suchen!👁"
	log(msg,answ)
elif "Dein Gegner ist" in msg:
	if not fight:
		t=0.3
	time.sleep(t)
	answ="Angriff!⚔"
	log(msg,answ)
elif "Während der Schlacht kamen unsere Truppen in einen Hinterhalt" in msg:
	if not fight:
		t=0.3
	time.sleep(t)
	answ="Verstärkung senden!🗡"
	log(msg,answ)
#rest
elif "die Arbeit ist beendet" in msg:
	time.sleep(t)
	answ="/work"
	log(msg,answ)
elif "Deine Felder sind voll. Du musst die Ernte einfahren, sonst wird sie verrotten." in msg:
	time.sleep(t)
	answ="/harvest"
	log(msg,answ)
else:
	log(msg,answ,"ERROR")

if answ != 0:
	print(answ)
