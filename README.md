# VillageGameAutoplay
Plays Village-Game-Telegram-Bot automatically.
## Required
telegram-cli:
https://github.com/vysheng/tg
## How to run
1. Goto your telegram-cli directory, for example:  
`cd Downloads/tg`
2. Create a directory "VillageGameAutoplay" and download all files there or just clone this Repository
3. Then start telegram-cli and execute the lua script file. Something like this:  
`bin/telegram-cli -k tg-server.pub -W -s VillageGameAutoplay/action.lua`
4. Message to yourself to change settings:
	- `pause` to pause automatic fight/quest 
	- `resume` to resume automatic fight/quest 
	- `/11` to set automatic quest:true  and fight:true
	- `/10` to set automatic quest:true  and fight:false
	- `/01` to set automatic quest:false and fight:true
	- `/00` to set automatic quest:false and fight:false (this will just auto /work and /harvest).

