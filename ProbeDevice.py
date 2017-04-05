import Lib.Packet as Packet
from Lib.SocketClient import ClientCommand,SocketClientThread,ClientReply

class Probe(object):
	def __init__(self, ToolID,Camera,SocketComm):
		self.ToolID = ToolID
		self.Socket = SocketComm
		self.Camera = Camera
		self.build_initial_packet()
		
	def build_initial_packet(self):
		self.current_packet = Packet.Packet()
				
	def send_packet(self):
		self.Socket.cmd_q.put(ClientCommand(ClientCommand.SEND, self.current_packet.pack()))
	
	def receive_packet(self):
		pass
	
	def button_pressed(self, ButtonNum):
		pass
		
	def turn_on_led(self, LedNum):
		pass
		
	