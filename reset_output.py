import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(11, True)
GPIO.output(13, True)

GPIO.cleanup((11, 13))