# from adafruit_motorkit import MotorKit
# import RoboticsBotLib
import requests

# kit = MotorKit()
# bot = RoboticsBotLib.Robot()

# kit.motor1.throttle = 1.0
print(requests.get("http://api.evrythng.com/time").text)
