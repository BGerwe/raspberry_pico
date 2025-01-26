# micropython documentation: https://docs.micropython.org/en/v1.23.0/library/machine.html
from machine import Pin
from utime import sleep


# Assigning GPIO (general purpose input/output) pins on the board to Python variables.
# We imported the `Pin` class above. Each time we call this and pass parameters it creates
# a new object of the `Pin` class. Each object inhereits all of the attributes (values associated
# to the object) and methods (functions called by the object). The first parameter passed is `id`,
# the address of the physical GPIO pin. The second parameter passed is `mode`, in this case
# defining the pins as output
led_blue = Pin(13, Pin.OUT)
led_red = Pin(14, Pin.OUT)
led_green = Pin(15, Pin.OUT)

# `while` is control logic that continuously executes the code below it if a condition is true.
# The general syntax is `while <condition>:`.
# Here we are explicitly setting that condition to `True` so the code will execute indefinitely.
while True:
    # Here we access the `on` method of the `Pin` class, to set its value to 1.
    led_green.on()
    # We want the light to remain on for a certain amount of time. We imported this function
    # `sleep` that causes code execution to wait a specified amount of time before proceeding. The
    # input of this function is the number of seconds to wait.
    sleep(1)
    # Access the `off` method of `Pin` to set its value to 0.
    led_green.off()

    # Repeat the above logic for the other two LEDs.
    led_red.on()
    sleep(1)
    led_red.off()
    led_blue.on()
    sleep(1)
    led_blue.off()
