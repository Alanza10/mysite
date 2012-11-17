import serial
import time


SYSTEM_RESET = 0xFF # reset from MIDI
START_SYSEX = 0xF0 # start a MIDI SysEx message

class myserial():
        
        
        def __init__ (self,port, baudrate, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, rtscts=True, xonxoff=False, timeout=1):
            try:
		        self.ser = serial.serial_for_url(port, baudrate, bytesize=serial.EIGHTBITS,  parity=parity, rtscts=rtscts, xonxoff=xonxoff, timeout=1)
        
            except serial.SerialException:
                print ("Error al abrir puerto: ")

        def reset(self):
                while self.ser.inWaiting() > 0:
		      readline()
                self.ser.setRTS(False)
		self.ser.setDTR(False)
                time.sleep(0.1)
                self.ser.setRTS(True)
		self.ser.setDTR(True)

        def parse(self):
		"""Preparing the data to be handled"""
		data = self.ser.read()
		if data != "":
		    self.__process(ord(data))		
        
        def __process(self, input_data):
		  """Handling input data"""
		  command = None		      
           
	def synctime(self):         
		  #T+10digitos epoch
                  command='T'+str(round(time.time())).rstrip('0').rstrip('.') 
		  self.ser.write(command)
                 # self.ser.flush()
                  return self.readline()
	
        def humedad(self):	   
 		  #HUM
		  command='HUM' 
		  self.ser.write(command)
                  #self.ser.flush()        
                  return self.readline()

        def readline(self):
                  time.sleep(0.1)
                  #while self.ser.inWaiting() > 0:
		  data=self.ser.readline()
		  return data 	 
        
        def date(self):
                  #DAT
		  command='DAT' 
		  self.ser.write(command) 
                  #self.ser.flush()       
                  return self.readline()

        def forcesynctime(self):         
		  time.sleep(1)
	# SYNC TIME COMMAND
	 	  self.ser.write('DAT')
		  
		     

                     		  
	def makesync(self):
               sync = self.issync()
	       if not(sync):
	           self.forcesynctime()           
	       time.sleep(1)      
		  #while ser.inWaiting() > 0:
	       self.synctime()
