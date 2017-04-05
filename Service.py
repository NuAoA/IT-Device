import Lib.Packet as Packet
#from Configuration import CONFIG
import Configuration as CONFIG
import ProbeDevice as PDevice
import CameraDevice as CDevice
from Lib.SocketClient import ClientCommand,SocketClientThread,ClientReply

class DeviceService(object):
	def __init__(self):
		self.Socket = SocketClientThread()
		self.Camera = CDevice.Camera(CONFIG.IMAGE_DIRECTORY,CONFIG.IMAGE_FORMAT)
		self.Probe = PDevice.Probe(CONFIG.TOOL_ID,self.Camera,self.Socket)
		
	def start_socket_server(self):
		self.Socket.start()
		
	def stop_socket_server(self):
		self.client.cmd_q.put(ClientCommand(ClientCommand.CLOSE))		
		

	
	