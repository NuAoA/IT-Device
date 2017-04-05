import Lib.Packet as Packet
from Lib.SocketClient import ClientCommand,SocketClientThread,ClientReply
import GPIOInterface

class Probe(object):
	def __init__(self, ToolID,Camera,SocketComm):
		self.ToolID = ToolID
		self.Socket = SocketComm
		self.Camera = Camera
		self.GPIO = GPIOInterface.MyGPIO(self.button_pressed,self.button_released)
		self.build_initial_packet()
		
	def build_initial_packet(self):
		self.current_packet = Packet.Packet()
		self.current_packet.set_tool_id(self.ToolID)
				
	def send_packet(self):
		self.Socket.cmd_q.put(ClientCommand(ClientCommand.SEND, self.current_packet.pack()))
	
	def receive_packet(self):
		pass
	
	def button_pressed(self, ButtonNum):
		if (ButtonNum == GPIOInterface.PIN_GREEN):
			self.current_packet.set_output_state(0,True)
		elif (ButtonNum == GPIOInterface.PIN_YELLOW):
			self.current_packet.set_output_state(1,True)
		elif (ButtonNum == GPIOInterface.PIN_RED):
			self.current_packet.set_output_state(2,True)
		elif (ButtonNum == GPIOInterface.PIN_BLUE):
			pass;
			#self.current_packet.set_output_state(3,True)
			
			
	def button_released(self, ButtonNum):
		if (ButtonNum == GPIOInterface.PIN_GREEN):
			self.current_packet.set_output_state(0,False)
		elif (ButtonNum == GPIOInterface.PIN_YELLOW):
			self.current_packet.set_output_state(1,False)
		elif (ButtonNum == GPIOInterface.PIN_RED):
			self.current_packet.set_output_state(2,False)
		elif (ButtonNum == GPIOInterface.PIN_BLUE):
			#self.current_packet.set_output_state(3,False)
			self.acquire_image() #THREAD THIS, causes missed events
			
		
	def acquire_image(self):
		self.current_packet.set_image_ID(self.Camera.capture())
		
	def turn_on_led(self, LedNum):
		pass
		
