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

def while_one_loop(droid):
    duration = 0.1  # 100 milliseconds
    if keyboard.is_pressed('w'):  # Forward
        droid.roll(speed=50, heading=0, duration=duration)
    elif keyboard.is_pressed('s'):  # Backward
        droid.roll(speed=-50, heading=0, duration=duration)
    elif keyboard.is_pressed('a'):  # Left
        droid.roll(speed=50, heading=270, duration=duration)
    elif keyboard.is_pressed('d'):  # Right
        droid.roll(speed=50, heading=90, duration=duration)
    elif keyboard.is_pressed('q'):  # Quit
        return False
    return True
