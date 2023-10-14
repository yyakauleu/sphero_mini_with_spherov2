import asyncio
from bleak import BleakScanner

# Device: SM-CE90, Address: DA:47:EC:10:CE:90

# async def run():
#     devices = await BleakScanner.discover()
#     for device in devices:
#         print(f"Device: {device.name}, Address: {device.address}")
#
# # Run the asynchronous function
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())

import asyncio
from bleak import BleakClient

async def connect(address):
    async with BleakClient(address) as client:
        if client.is_connected:
            print(f"Connected to {address}")
            # You can add more code here to interact with the device

# Replace 'YOUR_DEVICE_ADDRESS' with the actual Bluetooth address of your Sphero device
device_address = 'DA:47:EC:10:CE:90'

# Run the asynchronous function
loop = asyncio.get_event_loop()
loop.run_until_complete(connect(device_address))
