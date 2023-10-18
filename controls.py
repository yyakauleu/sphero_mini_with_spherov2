import keyboard
import time

axes = []

def old_while_one_loop(droid):
    # print("Inside while_one_loop")
    if keyboard.is_pressed('up'):
        print("Moving Forward")
        droid.set_speed(60)
        time.sleep(0.1)
        droid.set_speed(0)

    elif keyboard.is_pressed('down'):
        print("Moving Backward")
        droid.set_speed(-60)
        time.sleep(0.1)
        droid.set_speed(0)

    elif keyboard.is_pressed('left'):
        print("Turning Left")
        droid.set_heading(270)

    elif keyboard.is_pressed('right'):
        print("Turning Right")
        droid.set_heading(90)

    elif keyboard.is_pressed('esc'):
        print("Exiting")
        return False

    time.sleep(0.1)

    return True
HEADING_ADJUST = 45

def while_one_loop(droid):
    d_ = dict()
    print(droid.get_location())
    print(droid.get_gyroscope())
    print(droid.get_compass_direction())
    print(droid.get_distance())
    heading = droid.get_heading()
    print(heading)
    duration = 0.1  # 100 milliseconds
    if keyboard.is_pressed('w'):  # Forward
        # droid.roll(speed=50, heading=heading, duration=duration)
        droid.set_speed(60)
    elif keyboard.is_pressed('s'):  # slowdown - Stop
        # droid.roll(speed=50, heading=heading-180, duration=duration)
        droid.set_speed(0)
    elif keyboard.is_pressed('a'):  # Left
        heading=heading -HEADING_ADJUST
        # droid.roll(speed=50, heading=heading, duration=duration)
        droid.set_heading(heading)
    elif keyboard.is_pressed('d'):  # Right
        heading = heading +HEADING_ADJUST
        # droid.roll(speed=50, heading=heading, duration=duration)
        droid.set_heading(heading)
    elif keyboard.is_pressed('q'):  # Quit
        return False
    print(heading)

    return True

import random
def one_loop_random_dir(droid):
    print(droid.get_location())
    print(droid.get_gyroscope())
    print(droid.get_compass_direction())
    print(droid.get_distance())
    heading = droid.get_heading()
    duration = 1.5
    #rando c
    dir = 1 if random.random() > 0.5 else -1

    heading = heading + HEADING_ADJUST * dir

    droid.roll(speed=50, heading=heading, duration=duration)
