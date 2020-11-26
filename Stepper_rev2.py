import RPi.GPIO as GPIO
import time


# [dirX, pulseX], [dirY, pulseY]
stepper_pin = [[1,2],[3,4]]


def stepper(axis, direc, kecepatan) {
	GPIO.output(stepper_pin[axis][0], direc)
	GPIO.output(stepper_pin[axis][1], 1)
	time.sleep(kecepatan/1000)
	GPIO.output(stepper_pin[axis][1], 0)
	time.sleep(kecepatan/1000)
	

def main():    
    GPIO.setmode(GPIO.BOARD)    
	GPIO.setwarnings(False)
	GPIO.cleanup()
	
    GPIO.setup(stepper_pin[0][0], GPIO.OUT, initial=0)
	GPIO.setup(stepper_pin[0][1], GPIO.OUT, initial=0)
	GPIO.setup(stepper_pin[1][0], GPIO.OUT, initial=0)
	GPIO.setup(stepper_pin[1][1], GPIO.OUT, initial=0)
	
    
    try:
        while True:
			# stepper(axis, direction, kecepatan(microsec))			
			# axis 0 = x, 1 = y
			# direction 1 = -axis, direction 0 = +axis
			stepper(0, 1, 5); # -x
			stepper(1, 0, 5); # +Y
			time.sleep(1)			
			
    finally:		
        GPIO.cleanup()

		
if __name__ == '__main__':
    main()
