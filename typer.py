from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def split(words):
    return [char for char in words]

time.sleep(3)

# First input with a time interval of 2 seconds
for i in split("""One elder brother married and one younger sister married.Family setteled in Delhi.Father and mother
are now enjoying their retire life.
"""):
    keyboard.type(i)
    time.sleep(0.1)
time.sleep(2)  # Time interval between the first and second inputs

# Second input with a time interval of 1 second
for i in split("""YOUR TEXT """):
    keyboard.type(i)
    time.sleep(0.1)

time.sleep(2)
for i in split("""YOUR SECOND TEXT"""):
    keyboard.type(i)
    time.sleep(0.1)

time.sleep(2)
for i in split("1234"):
    keyboard.type(i)
    time.sleep(0.1)

time.sleep(2)
for i in split("1234"):
    keyboard.type(i)
    time.sleep(0.1)

time.sleep(2)
for i in split("Friend"):
    keyboard.type(i)
    time.sleep(0.1)