import Lib.Packet as Packet
#from Configuration import CONFIG
import Configuration as CONFIG
import ProbeDevice as PDevice
import CameraDevice as CDevice
from Lib.SocketClient import ClientCommand,SocketClientThread,ClientReply
from time import sleep
class DeviceService(object):
	def __init__(self):
		self.Socket = SocketClientThread()
		self.Camera = CDevice.Camera(CONFIG.IMAGE_DIRECTORY,CONFIG.IMAGE_FORMAT)
		self.Probe = PDevice.Probe(CONFIG.TOOL_ID,self.Camera,self.Socket)
		self.Socket.start()
		self.Socket.cmd_q.put(ClientCommand(ClientCommand.CONNECT, (CONFIG.SERVER_IP,CONFIG.SERVER_PORT)))
		self.thread()
		
	def start_socket_server(self):
		self.Socket.start()
		
	def stop_socket_server(self):
		self.Socket.cmd_q.put(ClientCommand(ClientCommand.CLOSE))		
		
	def thread(self):
		count = 0
		while True:
			sleep(0.1)
			self.Probe.send_packet()
			count = count +1
			if count > 30:
				self.Probe.current_packet.pretty_print()
				count = 0
	
if __name__ == "__main__":
	D = DeviceService()
	while (True):
		sleep(1)
		