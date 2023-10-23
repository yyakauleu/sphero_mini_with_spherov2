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

def get_droid_info(droid)->dict:
    d_ = dict( heading = droid.get_heading(),
               location=droid.get_location(),
              gyro=droid.get_gyroscope(),
              # compass=droid.get_compass_direction(),
              distaince=droid.get_distance())
    return d_
def while_one_loop(droid,n_loops):
    d_ = get_droid_info(droid)
    heading = d_["heading"]
    print(d_,n_loops)
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


def one_loop_random_dir(droid,n_loops:int,
                        max_loops = 20,
                        speed = 30,
                        duration = 5):

    d_ = get_droid_info(droid)

    print(d_,n_loops)
    #rando c
    def v1():
        heading = d_["heading"]
        dir = 1 if random.random() > 0.5 else -1
        heading = heading + HEADING_ADJUST * dir
        droid.roll(speed=speed, heading=heading, duration=duration)

    def v2():
        heading = int(360 / random.random())
        droid.roll(speed=speed, heading=heading, duration=duration)

    v2()

    n_loops = n_loops+1
    if n_loops >=max_loops:
        return False
    else: return True