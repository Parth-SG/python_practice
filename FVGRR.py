command =''

while command!='exit':
    is_stopped=True
    command=input('Command:')
    if command=='start':
      if is_stopped:
        print('started')
        is_stopped=False
      else:
         print("already started")
    elif command=='stop':
     if is_stopped:
        print('already stopped')
     else:
        print('stopped')
        is_stopped=True
    elif command=='exit':
        break
    elif command=='help':
        print('djskguwhfg')
    else:
       print('invalid command')
    
     

 
 
 