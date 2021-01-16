# from RoboticsBotLib import Robot
import asyncio
from EasyControllerInput import Input
import time
from inputs import get_gamepad
# bot = Robot()


while True:
    Input.update_inputs()
    print("Y button: " + str(Input.right_up))
    print("X button: " + str(Input.right_left))
    print("B button: " + str(Input.right_right))
    print("A button: " + str(Input.right_down))
