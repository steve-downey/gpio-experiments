import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
seconds = 2.0
delta = 0.25
upper_limit = 2

GPIO.output(27, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

try:
	while True:
		GPIO.output(27, GPIO.HIGH)
		time.sleep(seconds)
		GPIO.output(27, GPIO.LOW)
		GPIO.output(17, GPIO.LOW)
		time.sleep(seconds)
		seconds = seconds - delta
		print "seconds: %f delta: %f upper_limit: %f" % (seconds, delta, upper_limit)
		if seconds < 0.01:
			GPIO.output(17, GPIO.HIGH)
			delta = -0.25
			upper_limit = upper_limit - 0.5
			if upper_limit <= 0 : 
				upper_limit = 0
				GPIO.output(6, GPIO.HIGH)
		elif seconds >= upper_limit:
			delta = 0.25

except KeyboardInterrupt:
	print "Stopping"


finally:
	GPIO.cleanup()
