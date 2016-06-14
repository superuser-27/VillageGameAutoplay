import sys
import os
import time
import random
def log(msg, err=""):
	os.popen('echo "#__'+err+'__######'+str(msg)+'##########" >> village_game.txt')
sys.argv.pop(0)
sys.argv=str(sys.argv)
sys.argv=sys.argv.replace("\\n","")
t=random.randrange(50,200)/100
if "Die Banditen sind starke Jungs —  sie haben deine Truppen in die Mangel genommen" in str(sys.argv):
	time.sleep(t)
	print("Senden Sie Verstärkungen! 🗡")
	log(sys.argv)
elif "Wähle eine Quest, sie durchzuführen wird etwas kosten" in str(sys.argv):
	time.sleep(t)
	print("⭐️⭐️⭐️Sparen Sie das Dorf")
	log(sys.argv)
elif "Banditen haben ein Dorf angegriffen. Der Bürgermeister hat um Hilfe gebeten" in str(sys.argv):
	time.sleep(t)
	print("Geführte Suche🗡")
	log(sys.argv)
elif "Die Arbeit ist beendet, Eure Lordschaft!" in str(sys.argv):
	time.sleep(t)
	print("🍞Arbeiten!")
	log(sys.argv)
elif "Deine Felder sind voll. Du musst die Ernte einfahren, sonst wird sie verrotten." in str(sys.argv):
	time.sleep(t)
	print("Verkaufen Sie Brot💰")
	log(sys.argv)
else:
	log(sys.argv,"ERROR")
