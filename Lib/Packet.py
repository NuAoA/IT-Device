import struct
SIZE = 11

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)
	
def read_bit(value,bit):
	return value&bit

class Packet(object):
	def __init__(self):
		self.status = 0b0000
		self.battery_status = 0b0000
		self.deviceID = 0b00000000
		self.toolID = 0b00000000
		self.inputBits = 0b0000000000000000
		self.outputBits = 0b0000000000000000
		self.ImageID = 0b00000000000000000000000000000000

	def deconstruct_packet(self,packet_data):
		try:
			statusByte,self.deviceID,self.toolID,self.inputBits,self.outputBits,self.ImageID = struct.unpack("<BBBHHI",packet_data)
			self.battery_status = k&0b00001111
			self.status = k>>4
			return True
		except:
			return False
		#Method for parsing a freshly recieved packet

		
	def is_packet_server(self):
		return self.status>>3
		
	def set_tool_id(self,ID):
		self.toolID = ID
		
	def set_battery_level(self,battery_state):
		#set the batter level bits to the correct values
		if (battery_state > 15 or battery_state < 0):
			raise Exception('InputError', 'Battery state must be within 0-15')
			return
		self.battery_status = battery_state

		
	def get_input_state(self,input_num):
		#Get the state of the bit within the specified byte
		return read_bit(self.inputBits,input_num)
		
	def set_output_state(self,output_num,state):
		#Set the output number to state
		if (output_num > 15 or output_num < 0):
			raise Exception('InputError', 'Attempted to edit a bit that is not contained in the output array')
			return
		if (state):
			self.outputBits = set_bit(self.outputBits,output_num)
		else:
			self.outputBits = clear_bit(self.outputBits,output_num)
		
	def set_image_ID(self,ID):
		#Sets the uniq ID of the image file name
		if (ID < 0):
			raise Exception('InputError', 'Image ID must be greater than zero')
			return
		self.ImageID = ID
		
	def pack(self):
		#return the packet as required for tcp/ip communication	
		statusByte = (self.status<<4) | (self.battery_status)
		return struct.pack("<BBBHHI",statusByte,self.deviceID,self.toolID,self.inputBits,self.outputBits,self.ImageID)
		pass
		
	def pretty_print(self):
		#Prints the packet to the console
		print(bin((self.status<<4) | (self.battery_status>>4)))
		print(bin(self.deviceID))
		print(bin(self.toolID))
		print(bin(self.inputBits))
		print(bin(self.outputBits))
		print(bin(self.ImageID))
	
	