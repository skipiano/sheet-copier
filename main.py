import time
from pynput.keyboard import Key, Controller

delay = 0.25
rows = 454
cols = 13
control = Controller()


def dove():
    control.press(Key.cmd)
    time.sleep(delay)
    control.tap('5')
    time.sleep(delay)
    control.release(Key.cmd)


def sheet():
    control.press(Key.cmd)
    time.sleep(delay)
    control.tap('4')
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


if __name__ == "__main__":
    time.sleep(2)
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
