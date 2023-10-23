
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
import keyboard
import controls
from importlib import reload

droid_ = None

def main():
    global droid_
    toy = scanner.find_toy()
    with SpheroEduAPI(toy) as droid:
        print("Connected")
        droid_ = droid

        print(droid.__dict__)
        # {'_SpheroEduAPI__toy': SM-CE90 (DA:47:EC:10:CE:90),
        # '_SpheroEduAPI__heading': 0,
        # '_SpheroEduAPI__speed': 0, '_SpheroEduAPI__stabilization': True,
        # '_SpheroEduAPI__raw_motor': rawMotor(left=0, right=0),
        # '_SpheroEduAPI__leds': <spherov2.sphero_edu.LedManager object at 0x000001CD80343C10>,
        # '_SpheroEduAPI__frame_index': 0,
        # '_SpheroEduAPI__animation_index': 0,
        # '_SpheroEduAPI__fps_override': 0,
        # '_SpheroEduAPI__fade_override': <FadeOverrideOptions.NONE: 0>,
        # '_SpheroEduAPI__sensor_data': {'distance': 0.0, 'color_index': -1},
        # '_SpheroEduAPI__sensor_name_mapping': {},
        # '_SpheroEduAPI__last_location': (0.0, 0.0),
        # '_SpheroEduAPI__last_non_fall': 1697307934.9029546,
        # '_SpheroEduAPI__falling_v': 1.0,
        # '_SpheroEduAPI__last_message': None,
        # '_SpheroEduAPI__should_land': False,
        # '_SpheroEduAPI__free_falling': False,
        # '_SpheroEduAPI__compass_zero': None,
        # '_SpheroEduAPI__listeners': defaultdict(<class 'set'>, {}),
        # '_SpheroEduAPI__stopped': <threading.Event object at 0x000001CD80343CD0>,
        # '_SpheroEduAPI__updating': <unlocked _thread.lock object at 0x000001CD802A6C60>,
        # '_SpheroEduAPI__thread': <Thread(Thread-1, started 27096)>}

        print(list(droid.__dict__))
        n_loops = 0
        while True:
            reload(controls)
            ret_ = controls.while_one_loop(droid,n_loops)
            # ret_ = controls.one_loop_random_dir(droid,n_loops)

            n_loops = n_loops + 1

            if not ret_:
                break

if __name__ == "__main__":
    main()
