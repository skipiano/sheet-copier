import time
import sys
from pynput.keyboard import Key, Controller, Listener

delay = 0.25
rows = 0
cols = 13
control = Controller()


def dove():
    control.press(Key.cmd)
    time.sleep(delay)
    control.tap('1')
    time.sleep(delay)
    control.release(Key.cmd)


def sheet():
    control.press(Key.cmd)
    time.sleep(delay)
    control.tap('2')
    time.sleep(delay)
    control.release(Key.cmd)


def c():
    control.press(Key.cmd)
    time.sleep(delay)
    control.tap('c')
    time.sleep(delay)
    control.release(Key.cmd)


def v():
    control.press(Key.cmd)
    time.sleep(delay)
    control.tap('v')
    time.sleep(delay)
    control.release(Key.cmd)


def move_down():
    control.press(Key.down)
    for i in range(cols-1):
        time.sleep(0.05)
        control.press(Key.left)


def on_press(key):
    if key == 'q':
        print("Terminating program")
        sys.exit()


if __name__ == "__main__":
    while(True):
        try:
            rows = int(input("Enter the number of rows you want to copy: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        else:
            print("Input received.")
            result_time = 35*rows
            h = result_time//3600
            m = (result_time % 3600)//60
            s = result_time % 60
            print(
                "Approximately {} hours, {} minutes, {} seconds to finish execution".format(h, m, s))
            print(
                "Please click back to your browser onto your source sheet to allow the program to start copying")
            break

    time.sleep(5)
    print("Starting")
    for i in range(rows):
        for j in range(cols-1):
            time.sleep(delay)
            c()
            control.tap(Key.right)
            sheet()
            time.sleep(delay)
            v()
            control.tap(Key.right)
            dove()
        c()
        move_down()
        time.sleep(0.5)
        sheet()
        v()
        move_down()
        time.sleep(0.5)
        dove()
