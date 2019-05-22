#!/usr/local/bin/python
import RPi.GPIO as GPIO
import time
import math
import bme680

sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

fire = 21
buzzer = 15

def setup():

    GPIO.setup(fire, GPIO.IN)
    GPIO.setup(15, GPIO.OUT)


def beep(number_of_times):

        beep_time = 0.5
        time_in_between_beeps = 0.2

        for i in range(number_of_times):
                GPIO.output(15, GPIO.HIGH)
                time.sleep(beep_time)
                GPIO.output(15, GPIO.LOW)
                time.sleep(time_in_between_beeps)


def loop():
    while True:

        global digFire
        digFire = GPIO.input(fire)

        if sensor.get_sensor_data():
           temp = sensor.data.temperature
           print(temp, "Degree C.")

        if digFire == 0 and temp > 35:
           warning = 'FIRE DETECTED!\n'
           print(warning)
           beep(5)
           execfile("/usr/src/app/scripts/smsconfig.py")

        else:
           safe = 'No fire detected\n'
           print(safe)

        time.sleep(1)
if __name__ == '__main__':
       try:
               setup()
               loop()
       except KeyboardInterrupt:
              pass
              GPIO.cleanup()
GPIO.cleanup()
