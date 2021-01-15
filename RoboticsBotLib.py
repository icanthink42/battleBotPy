from adafruit_motorkit import MotorKit
import requests

server = "gamer.com"

class Robot:
    def __init__(self, left_front_motor=None, right_front_motor=None, left_back_motor=None, right_back_motor=None, game="default"):
        self.left_front = 0
        self.right_front = 0
        self.left_back = 0
        self.right_back = 0
        self.full_game_path = server + "/game/" + game

        if left_front_motor is not None:
            self.leftFrontMotor = left_front_motor
        else:
            self.leftFrontMotor = MotorKit().motor1

        if right_front_motor is not None:
            self.rightFrontMotor = right_front_motor
        else:
            self.rightFrontMotor = MotorKit().motor2

        if left_back_motor is not None:
            self.leftBackMotor = left_back_motor
        else:
            self.leftBackMotor = MotorKit().motor3

        if right_back_motor is not None:
            self.rightBackMotor = right_back_motor
        else:
            self.rightBackMotor = MotorKit().motor4

    def bot_tick(self):
        if self.full_game_path + "status.cfg" is "true":
            self.leftFrontMotor.throttle = self.left_front
            self.rightFrontMotor.throttle = self.right_front
            self.leftBackMotor.throttle = self.left_back
            self.rightBackMotor.throttle = self.right_back

    def move(self, speed):
        self.left_front = speed
        self.right_front = speed
        self.left_back = speed
        self.right_back = speed

    def turn(self, speed):
        self.left_front = -speed
        self.left_back = -speed
        self.right_front = speed
        self.right_back = speed

    def leftfront(self, speed):
        self.left_front = speed

    def rightfront(self, speed):
        self.right_front = speed

    def leftback(self, speed):
        self.left_back = speed

    def rightback(self, speed):
        self.right_back = speed
