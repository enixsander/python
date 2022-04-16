import asyncio
import random

import serial
from matplotlib import pyplot as plt

serial_port = 'COM4'
baud_rate = 9600

plt.ion()   # set plot to animated
fig, ax = plt.subplots()
x = range(20)  # [i for i in range(20)]
y = [0]*20
line, = ax.plot([], [])
ax.set_xlim([0, 20])
ax.set_ylim([0, 260])
line.set_xdata(x)

line2, = ax.plot([], [])
line2.set_xdata(x)
y2 = [0]*20


def plot_task(data, data2):
    if len(y) >= 20:
        y.pop(0)
        y2.pop(0)
    y.append(data)
    y2.append(data2)
    line.set_ydata(y)
    line2.set_ydata(y2)
    line.figure.canvas.draw_idle()
    line.figure.canvas.flush_events()


async def read_task(port, speed):
    try:
        # set up the serial line, change COM# if necessary
        ser = serial.Serial(port, speed)
        while True:
            if ser.inWaiting() > 0:
                msg = ser.read()
                print(msg)
                plot_task(int.from_bytes(msg, "big"), 0)
            else:
                await asyncio.sleep(0.0001)
    except serial.SerialException:
        print("could not open port %s" % port)


async def test_task():
    while True:
        await asyncio.sleep(2.0)
        print("2 sec")


async def random_task():
    while True:
        plot_task(random.random() * 250, random.random() * 250)
        await asyncio.sleep(0.2)


async def main_task():
    # asyncio.create_task(read_serial("COM3", 9600))

    await asyncio.gather(
        test_task(),
        read_task(serial_port, baud_rate),
        random_task()
    )


if __name__ == '__main__':
    try:
        asyncio.run(main_task())
    except KeyboardInterrupt:
        print("halt program by using the Ctrl + C or Ctrl + Z")
