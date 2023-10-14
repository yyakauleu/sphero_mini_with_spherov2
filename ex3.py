
import time
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color

toy = scanner.find_toy()
with SpheroEduAPI(toy) as droid:
    print("Connected")
    print(droid.__dict__)
    droid.set_main_led(Color(r=0, g=0, b=255))
    droid.set_speed(60)
    time.sleep(2)
    droid.set_speed(0)

    print("Done")
