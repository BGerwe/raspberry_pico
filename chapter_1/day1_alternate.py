# The code in `day1.py` is adequate for lighting up a sequence of LEDs in the proper order, but it
# does use some bad coding habits. I'm writing this script as an alternative to achieve the same
# goal but with somewhat more pythonic approach to show how I would write the script in a more
# maintainable way.

# We import the same packages / modules
from machine import Pin
from utime import sleep

# Make a dictionary defining the pins so I don't have a to access each pin by its individual
# variable name in the future. The dictionary variable name is all in upper case to indicate it is
# a "global" variable within this script and I will not be modifying the variabe during execution
# of the script.
LED_PINS = {
    "blue": Pin(13, Pin.OUT),
    "red": Pin(14, Pin.OUT),
    "green": Pin(15, Pin.OUT),
}

# Since we want to repeat the same set of commands on each of the three pins, we should define a
#  function to call when we want to execute those commnads. The advantage is now we have a single
#  place to modify when we want to change something about the sequence of commands as opposed to
#  making the same modification in three separate places. This is a concept know as "DRY"ing your
# code. Don't Repeat Yourself (DRY).

# This function accepts a `Pin` object to be controlled, and has an optional keyword argument
# (aka kwarg) called `duration` that sets the length of time the LED is turned on. `duration` has a
# default of 1 second.


def led_blink_on_off(pin, duration=1):
    """
    This function turns on a GPIO pin attached to an LED for a set duration and then turns off the
    pin.

    :pin: machine.Pin object initialized to one of the board GPIO pins. The class must have methods
          `on` and `off` defined.
    :duration: int or float, number of seconds for the LED to be lit
    :return: None
    """
    pin.on()
    sleep(duration)
    pin.off()


# With these basic ingredients we can already do some more advanced sequencing. To demonstrate a
# few different idea I will have each sequence execute three times before going to the next, instead
# of running indefinitely as with the `day1.py` script.

# First we will have the red LED blink twice and the others blink once. I am choosing to use a `For`
# loop because it will be obvious that I want the sequence to execute a fixed number of times. We
# could use a `While` loop instead, but the intent is less obvious from the outset, so the code is
# considered less readable.
print("Blink sequence: G, R, R, B")
for i in range(0, 3):
    # NOTE: I am defining the variable `i` here, but we don't actually need to use it anywhere.

    # Call the function on LED pins defined in the dictionary above.
    led_blink_on_off(LED_PINS["green"])
    led_blink_on_off(LED_PINS["red"])
    # Need to add a delay between these to make the second blink. Otherwise the red LED just stays
    # on for two seconds because the time between `pin.off()` in the first function call and
    # `pin.on()` in the second function call is microseconds.
    sleep(1)
    led_blink_on_off(LED_PINS["red"])
    led_blink_on_off(LED_PINS["blue"])


# We can modify the length of time each LED blinks for. I will use a function called `zip` here that
# goes through two iterables (e.g. lists) and uses their values in the current loop execution. `zip`
# runs until one of the iterables is finished. Note I am just using the color name instead of
# accessing `LED_PINS` at this point.
print("Blink G for 0.5 seconds, R for 1 second, B for 2 seconds")
for i in range(0, 3):
    # Note that duration 10 is not actually used
    for color, duration in zip(["green", "blue", "red"], [0.5, 1, 2, 10]):
        led_blink_on_off(LED_PINS[color], duration)  # type: ignore

# Hopefully you can appreciate that the sequences above are a lot more concise and readable with
# these advanced techniques than if we had continued to used the basics in `day1.py`.

# This block accomplishes the same sequence produced in `day1.py`
print("Indefinite sequence G, R, B. Press Ctrl+C to stop")
while True:
    for color in ["green", "red", "blue"]:
        led_blink_on_off(LED_PINS[color])
