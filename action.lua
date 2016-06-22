function on_msg_receive (msg)
      if msg.out then
          return
      end
      if (msg.from.print_name == "Village_Game" )then
	if (msg.text==nil) then
		msg.text="Banditen haben ein Dorf angegriffen. Der Bürgermeister hat um Hilfe gebeten"
	end
	print(msg.text)
	msg.text=string.gsub(msg.text, "'", "#")
      	r=string.format("%s",io.popen('python3 VillageGameAutoplay/village_game.py "'..string.format("%s",msg.text)..'"'):read())
      	if ( r ~= "nil" ) then
	 	print(msg.from.print_name..": "..r)
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
