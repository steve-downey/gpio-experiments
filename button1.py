import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.OUT)

while True:
	if GPIO.input(17) == False:
		GPIO.output(27,GPIO.HIGH)
	elif GPIO.input(17) == True:
		GPIO.output(27,GPIO.LOW)
