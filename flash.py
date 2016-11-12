import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

try:
	while True:
		GPIO.output(17, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(17, GPIO.LOW)
		time.sleep(0.5)

except KeyboardInterrupt:
	print "Stopping"


finally:
	GPIO.cleanup()
