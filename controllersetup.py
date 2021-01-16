from inputs import get_gamepad
import time


def get_input():
    events = get_gamepad()
    for event in events:
        return event.code


print("Left Joystick X: 0")
print("Left Joystick Y: 1")
print("Right Joystick X: 2")
print("Right Joystick Y: 3")
print("Left trigger: 4")
print("Right trigger Y: 5")
print("Left side up button (up arrow): 6")
print("Left side down button (down arrow): 7")
print("Left side left button (left arrow): 8")
print("Left side right button (right arrow): 9")
print("Right side up button (Y/Triangle): y")
print("Right side down button (A/Cross): a")
print("Right side left button (X/Square): x")
print("Right side right button (B/Circle): b")
prompt = input("Select a button/axis to edit: ")
if prompt == "0":
    print("Press left on your left joystick")
    f = open("controllerconfig/leftXAxis.cfg", "w")
if prompt == "1":
    print("Press up on your left joystick")
    f = open("controllerconfig/leftYAxis.cfg", "w")
if prompt == "2":
    print("Press left on your right joystick")
    f = open("controllerconfig/rightXAxis.cfg", "w")
if prompt == "3":
    print("Press up on your right joystick")
    f = open("controllerconfig/rightYAxis.cfg", "w")
if prompt == "4":
    print("Press your left trigger")
    f = open("controllerconfig/leftTriggerAxis.cfg", "w")
if prompt == "5":
    print("Press your right trigger")
    f = open("controllerconfig/rightTriggerAxis.cfg", "w")
if prompt == "6":
    print("Press the left side up button (up arrow)")
    f = open("controllerconfig/leftUpButton.cfg", "w")
if prompt == "7":
    print("Press the left side down button (down arrow)")
    f = open("controllerconfig/leftDownButton.cfg", "w")
if prompt == "8":
    print("Press the left side left button (left arrow)")
    f = open("controllerconfig/leftLeftButton.cfg", "w")
if prompt == "9":
    print("Press the right side right button (right arrow)")
    f = open("controllerconfig/leftRightButton.cfg", "w")
if prompt == "y":
    print("Press the right side up button (Y/Triangle)")
    f = open("controllerconfig/rightUpButton.cfg", "w")
if prompt == "a":
    print("Press the right side down button (A/Cross)")
    f = open("controllerconfig/rightDownButton.cfg", "w")
if prompt == "x":
    print("Press the right side left button (X/Square)")
    f = open("controllerconfig/rightLeftButton.cfg", "w")
if prompt == "b":
    print("Press the right side right button (B/Circle)")
    f = open("controllerconfig/rightRightButton.cfg", "w")

f.write(get_input())
f.close()
