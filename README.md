# VillageGameAutoplay
Plays Village-Game-Telegram-Bot automatically.
## Required
telegram-cli:
https://github.com/vysheng/tg
## How to run
1. Goto your telegram-cli directory, for example:  
`cd Downloads/tg`
2. Create a subdirectory "VillageGameAutoplay" and download all files there or just clone this Repository:  
`git clone https://github.com/superuser-27/VillageGameAutoplay VillageGameAutoplay`
3. Then start telegram-cli and execute the lua script file. Something like this:  
`bin/telegram-cli -k tg-server.pub -W -s VillageGameAutoplay/action.lua`

	- For multiple profiles, just specify the profile you want to start the script with:  
	`bin/telegram-cli -p profile1 -W -s VillageGameAutoplay/action.lua`

	- Support for different profiles running at the same time will be added in future.

4. Message to **yourself** to change settings:
	- `pause` to pause automatic fight/quest 
	- `resume` to resume automatic fight/quest 
	- `/11` to set automatic quest: :white_check_mark:  and fight: :white_check_mark:
	- `/10` to set automatic quest: :white_check_mark:  and fight: :x:
	- `/01` to set automatic quest: :x: and fight: :white_check_mark:
	- `/00` to set automatic quest: :x: and fight: :x: (this will just auto /work and /harvest).

5. To change language:
	- `/setlang_it` or `/italiano` to change to Italian :it:
	- `/setlang_de` or `/deutsch` to change to German :de:
	- `/setlang_en` or `/english` to change to English :uk:

6. To start questing/fighting send the command to Village_Game and the script will continue on its own.
