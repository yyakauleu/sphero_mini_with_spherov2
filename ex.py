# Import required modules
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
import asyncio
from bleak import BleakScanner
import bleak

async def run():
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")

# Run the asynchronous function
loop = asyncio.get_event_loop()
loop.run_until_complete(run())


# Find the Sphero toy
toy = scanner.find_toy()

# Initialize the high-level API and control the toy
with SpheroEduAPI(toy) as api:

    api.spin(360, 1)  # Spin the Sphero 360 degrees at speed 1
