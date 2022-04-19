import time
import RPi.GPIO as GPIO

# setup variables
degrees_85_pin = 16  # 4'th GPIO pin in BCM mode
degrees_5_pin = 15  # Same as above
trigger_pin = 11  # Same as above
rotation_pin = 13  # Same as above

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(degrees_5_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(degrees_85_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(rotation_pin, GPIO.OUT)

# state of pins
# print('State of trigger_pin:', GPIO.input(trigger_pin))
# print('State of rotation_pin (1 - rotating clockwise, 0 - counter clockwise):', GPIO.input(rotation_pin))
# print('State of degrees_5_pin:', GPIO.input(degrees_5_pin))
# print('State of degrees_85_pin:', GPIO.input(degrees_85_pin))

# set rotation
rotate_clockwise = True
GPIO.output(rotation_pin, rotate_clockwise)

# start engine
engine_off = False
GPIO.output(trigger_pin, engine_off)


def change_direction():
    if GPIO.input(degrees_85_pin) == GPIO.input(degrees_5_pin):
        if GPIO.input(degrees_85_pin) == GPIO.LOW:
            rotate_clockwise = False
        elif GPIO.input(degrees_85_pin) == GPIO.HIGH:
            rotate_clockwise = True
        GPIO.output(rotation_pin, rotate_clockwise)

# event listener
GPIO.add_event_detect(degrees_85_pin, GPIO.FALLING, callback=lambda x: change_direction(), bouncetime=300)
GPIO.add_event_detect(degrees_5_pin, GPIO.RISING, callback=lambda x: change_direction(), bouncetime=300)

try:
    while True: pass
except:
    GPIO.remove_event_detect(degrees_5_pin)
    GPIO.remove_event_detect(degrees_85_pin)
    GPIO.output(rotation_pin, False)
    GPIO.output(trigger_pin, False)
    GPIO.wait_for_edge(degrees_5_pin, GPIO.RISING)
    GPIO.output(rotation_pin, True)
    GPIO.output(trigger_pin, True)
    GPIO.cleanup((degrees_5_pin, degrees_85_pin, trigger_pin, rotation_pin))
