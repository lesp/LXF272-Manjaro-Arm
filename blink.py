import RPi.GPIO as GPIO
import time

ledpin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin, GPIO.OUT)

try:
    while True:
        GPIO.output(ledpin, GPIO.HIGH)
        print("LED ON")
        time.sleep(0.5)
        GPIO.output(ledpin, GPIO.LOW)
        print("LED OFF")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
