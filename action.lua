function on_msg_receive (msg)
      if msg.out or msg.from.print_name==msg.to.print_name then
          if(msg.text=="pause" or msg.text=="Pause")then
		file=io.open("VillageGameAutoplay/setting.json","w")
		io.output(file)
		io.write('{"quest": 1, "fight": 1, "pause": 1}')
		io.close(file)
	 	send_msg(msg.from.print_name,"Auto quest/fight paused.",ok_cb,false)
	elseif(msg.text=="resume" or msg.text=="Resume")then
		file=io.open("VillageGameAutoplay/setting.json","w")
		io.output(file)
		io.write('{"quest": 1, "fight": 1, "pause": 0}')
		io.close(file)
	 	send_msg(msg.from.print_name,"Auto quest/fight resumed.",ok_cb,false)
	elseif(msg.text=="/11")then
		file=io.open("VillageGameAutoplay/setting.json","w")
		io.output(file)
		io.write('{"quest": 1, "fight": 1, "pause": 0}')
		io.close(file)
	 	send_msg(msg.from.print_name,"Quest = true    Fight = true",ok_cb,false)
	elseif(msg.text=="/10")then
		file=io.open("VillageGameAutoplay/setting.json","w")
		io.output(file)
		io.write('{"quest": 1, "fight": 0, "pause": 0}')
		io.close(file)
	 	send_msg(msg.from.print_name,"Quest = true    Fight = false",ok_cb,false)
	elseif(msg.text=="/01")then
		file=io.open("VillageGameAutoplay/setting.json","w")
		io.output(file)
		io.write('{"quest": 0, "fight": 1, "pause": 0}')
		io.close(file)
	 	send_msg(msg.from.print_name,"Quest = false    Fight = true",ok_cb,false)
	elseif(msg.text=="/00")then
		file=io.open("VillageGameAutoplay/setting.json","w")
		io.output(file)
		io.write('{"quest": 0, "fight": 0, "pause": 0}')
		io.close(file)
	 	send_msg(msg.from.print_name,"Quest = false    Fight = false",ok_cb,false)
	elseif(msg.text=="/settings" or msg.text=="/Settings")then
		file=io.open("VillageGameAutoplay/setting.json","w")
		settings=read(file)
		io.close(file)
	 	send_msg(msg.from.print_name,settings,ok_cb,false)
	end
      end
	

      if (msg.from.print_name == "Village_Game" )then
--	send_msg("InventoryBot","/avventura",ok_cb,false)
	if (msg.text==nil) then
		msg.text="Banditen haben ein Dorf angegriffen. Der Bürgermeister hat um Hilfe gebeten"
	end
	msg.text=string.gsub(msg.text, "'", "#")
	tmp=string.format("%s",msg.text)
	tmp2=io.popen('python3 VillageGameAutoplay/village_game.py "'..tmp..'"'):read()
      	r=string.format("%s",tmp2)

      	if ( r ~= "nil" ) then
	 	send_msg(msg.from.print_name,r,ok_cb,false)
	end
      end
      if (msg.from.print_name == "USERNAME" )then
--      	print(msg.text)
	msg.text=string.gsub(msg.text, "'", "#")
      	r=string.format("%s",io.popen('python3 VillageGameAutoplay/setting.py "'..string.format("%s",msg.text)..'"'):read())
      	if ( r ~= "nil" ) then
	 	print(msg.from.print_name..": "..r)
	 	r=string.gsub(r, "\\n", "\n")
	 	send_msg(msg.from.print_name,r,ok_cb,false)
      	end
      end
  end
   
  function on_our_id (id)
  end
   
  function on_secret_chat_created (peer)
  end
   
  function on_user_update (user)
  end
   
  function on_chat_update (user)
  end
   
  function on_get_difference_end ()
  end
   
  function on_binlog_replay_end ()
  end
