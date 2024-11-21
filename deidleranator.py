"""
deidleranator

A simple Python script to move the mouse every 10 seconds to prevent the screen saver from kicking in.

"""

import pyautogui
import time


def move_mouse():
    """Move mouse to the right and back to the original position."""
    x, y = pyautogui.position()
    pyautogui.moveTo(x + 100, y, duration=0.5)
    time.sleep(1)
    pyautogui.moveTo(x, y, duration=0.5)


if __name__ == "__main__":
    try:
        while True:
            move_mouse()
            time.sleep(10)
    except KeyboardInterrupt:
        pass


