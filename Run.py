
import Queue
import Packet
from SocketClient import ClientCommand,SocketClientThread,ClientReply
from time import sleep

class SocketClient(object):
	def __init__(self,IP,Port):
		self.client = SocketClientThread()
		self.IP = IP
		self.Port = Port
		
	def Connect(self):
		self.client.start()
		self.client.cmd_q.put(ClientCommand(ClientCommand.CONNECT, (self.IP,self.Port)))
		#self.Handshake()
		
	def Handshake(self):
		self.SendMessage("Hello!!!")
		self.client.cmd_q.put(ClientCommand(ClientCommand.RECEIVE))
		
	def SendMessage(self,Message):
		self.client.cmd_q.put(ClientCommand(ClientCommand.SEND, Message))
		
	def Close(self):
		self.client.cmd_q.put(ClientCommand(ClientCommand.CLOSE))
		
	def RecvMessage(self):
		self.client.cmd_q.put(ClientCommand(ClientCommand.RECEIVE))
		try:
			reply = self.client.reply_q.get(block=True)
			status = "SUCCESS" if reply.type == ClientReply.SUCCESS else "ERROR"
			return reply.data
		except Queue.Empty:
			pass

S = SocketClient('192.168.0.106',5555)

S.Connect()
i = 0
while (True):
	P = Packet.Packet()	
	P.pretty_print()
	
	print("packet:"+str(P.get_packet()))
	S.SendMessage(P.get_packet())
	sleep(10)
	print(S.RecvMessage())

	
