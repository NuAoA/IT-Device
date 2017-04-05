import picamera

class Camera(object):
	def __init__(self,root_folder,image_format):
		self.Camera = picamera.PiCamera()
		self.RootDir = root_folder
		self.ImageFormat = image_format
		self.Image_ID = self.determine_initial_imageID()
		
	def determine_initial_imageID(self):
		#Look in root folder and find largest numbered file.
		return 1
	
	def gen_next_filename(self):
		self.Image_ID = self.Image_ID+1
		return "%s/%d%s"%(self.RootDir,self.Image_ID,self.ImageFormat)
	
	def capture(self):
		Camera.capture(gen_next_filename())
		return self.Image_ID
	
