import RPi.GPIO as GPIO
import time
import os

# os.system('aplay -r 48000 Tequila.wav')
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7,50) #pulse width modulation
p.start(20)

try:
	for x in range(10):
		p.ChangeDutyCycle(7.5)
		time.sleep(.2)
		p.ChangeDutyCycle(12.5)
		time.sleep(.2)
		#p.ChangeDutyCycle(2.5)
		#time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
	print('...Motor stopped')
