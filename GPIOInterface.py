import RPi.GPIO as GPIO
import Configuration as CONFIG
from time import sleep

PIN_YELLOW = CONFIG.PIN_YELLOW
PIN_GREEN = CONFIG.PIN_GREEN
PIN_BLUE = CONFIG.PIN_BLUE
PIN_RED = CONFIG.PIN_RED
BOUNCE_TIME = 300

class MyGPIO(object):
	def __init__(self,pressedCallback,releasedCallback):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(PIN_YELLOW, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
		GPIO.setup(PIN_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
		GPIO.setup(PIN_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
		GPIO.setup(PIN_BLUE, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
		self.pressedCallback = pressedCallback
		self.releasedCallback = releasedCallback
		self.subscribe()
		
	def subscribe(self):
		#Note, this functionality assumes that the pins are configured as pullup.
		GPIO.add_event_detect(PIN_YELLOW, GPIO.FALLING, callback=self.GPIO_pressed_callback, bouncetime=BOUNCE_TIME)
		GPIO.add_event_detect(PIN_GREEN, GPIO.FALLING, callback=self.GPIO_pressed_callback, bouncetime=BOUNCE_TIME)
		GPIO.add_event_detect(PIN_RED, GPIO.FALLING, callback=self.GPIO_pressed_callback, bouncetime=BOUNCE_TIME)
		GPIO.add_event_detect(PIN_BLUE, GPIO.FALLING, callback=self.GPIO_pressed_callback, bouncetime=BOUNCE_TIME)		

	def GPIO_pressed_callback(self,PinNum):
		print(str(PinNum) + "pressed")
		GPIO.remove_event_detect(PinNum)
		GPIO.add_event_detect(PinNum, GPIO.RISING, callback=self.GPIO_released_callback, bouncetime=BOUNCE_TIME)
		self.pressedCallback(PinNum)
		
	def GPIO_released_callback(self,PinNum):
		print(str(PinNum) + "released")
		GPIO.remove_event_detect(PinNum)
		GPIO.add_event_detect(PinNum, GPIO.FALLING, callback=self.GPIO_pressed_callback, bouncetime=BOUNCE_TIME)
		self.releasedCallback(PinNum)
	
if __name__ == "__main__":
	G = MyGPIO()
	while (True):
		sleep(1)
	