import serial
import time



def read():         
          #T+10digitos epoch
          command='T'+str(round(time.time())).rstrip('0').rstrip('.') 
	  try: 
	  	ser = serial.Serial('/dev/ttyUSB0', 9600)
	  except SerialException: 
	  	print "Doh, you need to define 'a' before you can print it!" 
	  
          time.sleep(1)
	  while ser.inWaiting() > 0:
		  data=ser.readline()
                  print data
          ser.write(command)
          time.sleep(1)
	  while ser.inWaiting() > 0:
		  data=ser.readline()
                  print data
          
          ser.close()
