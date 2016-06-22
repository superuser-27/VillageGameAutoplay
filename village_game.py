import sys
import os
import time
import random
def log(msg, err=""):
	os.popen('echo "#__'+err+'__######'+str(msg)+'##########" >> VillageGameAutoplay/village_game.txt')
sys.argv.pop(0)
sys.argv=str(sys.argv)
sys.argv=sys.argv.replace("\\n","")
t=random.randrange(50,200)/100
if "Die Banditen sind starke Jungs —  sie haben deine Truppen in die Mangel genommen" in str(sys.argv):
	time.sleep(t)
	print("Verstärkung schicken! 🗡")
	log(sys.argv)
elif "Wähle eine Quest, sie durchzuführen wird etwas kosten" in str(sys.argv):
	time.sleep(t)
	print("⭐️⭐️⭐️Das Dorf retten")
	log(sys.argv)
elif "Banditen haben ein Dorf angegriffen. Der Bürgermeister hat um Hilfe gebeten" in str(sys.argv):
	time.sleep(t)
	print("Quest starten🗡")
	log(sys.argv)
elif "Herr, die Arbeit ist beendet." in str(sys.argv):
	time.sleep(t)
	print("/work")
	log(sys.argv)
elif "Deine Felder sind voll. Du musst die Ernte einfahren, sonst wird sie verrotten." in str(sys.argv):
	time.sleep(t)
	print("/harvest")
	log(sys.argv)
else:
	log(sys.argv,"ERROR")
