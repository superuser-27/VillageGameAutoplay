import sys
import os
import time
import random
import json

msg=sys.argv
msg.pop(0)
msg=str(msg).lower()
msg=msg.replace("\\n","")
answ=0

settings=json.loads(os.popen("cat VillageGameAutoplay/setting.json").read())
help="""You can use this commands: \\n\
get settings \\n\
toggle \\n\
start \\n\
stop \\n\
set fight [0/1] \\n\
set quest [0/1]"""

if "help" in msg:
	answ=help
elif "settings" in msg:
	answ=settings
elif "toggle" in msg:
	settings["fight"]=int(not settings["fight"])
	settings["quest"]=int(not settings["quest"])
	answ=settings
elif "start" in msg:
	settings["pause"]=0
	answ=settings
elif "stop" in msg:
	settings["pause"]=1
	answ=settings
elif "set fight" in msg:
	num=msg[len(msg)-3:len(msg)-2]
	if num == "0" or num == "1":
		settings["fight"]=int(num)
		answ=settings
	else:
		answ="Bitte geben Sie eine 0 oder 1 ein."
elif "set quest" in msg:
	num=msg[len(msg)-3:len(msg)-2]
	if num == "0" or num == "1":
		settings["quest"]=int(num)
		answ=settings
	else:
		answ="Bitte geben Sie eine 0 oder 1 ein."
	
if answ != 0:
	print(answ)

os.popen("echo '"+json.dumps(settings)+"' > VillageGameAutoplay/setting.json")
