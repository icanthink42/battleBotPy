from inputs import get_gamepad


class Input:
    left_x = 0
    left_y = 0

    right_x = 0
    right_y = 0

    left_trigger = 0
    right_trigger = 0

    left_up = 0
    left_down = 0
    left_left = 0
    left_right = 0

    right_up = 0
    right_down = 0
    right_left = 0
    right_right = 0


    left_x_axis = open("controllerconfig/leftXAxis.cfg").read()
    left_y_axis = open("controllerconfig/leftYAxis.cfg").read()

    right_x_axis = open("controllerconfig/rightXAxis.cfg").read()
    right_y_axis = open("controllerconfig/rightYAxis.cfg").read()

    left_trigger_axis = open("controllerconfig/leftTriggerAxis.cfg").read()
    right_trigger_axis = open("controllerconfig/rightTriggerAxis.cfg").read()

    left_up_button = open("controllerconfig/leftUpButton.cfg").read()
    left_down_button = open("controllerconfig/leftDownButton.cfg").read()
    left_left_button = open("controllerconfig/leftLeftButton.cfg").read()
    left_right_button = open("controllerconfig/leftRightButton.cfg").read()

    right_up_button = open("controllerconfig/rightUpButton.cfg").read()
    right_down_button = open("controllerconfig/rightDownButton.cfg").read()
    right_left_button = open("controllerconfig/rightLeftButton.cfg").read()
    right_right_button = open("controllerconfig/rightRightButton.cfg").read()

    @staticmethod
    def update_inputs():
        events = get_gamepad()
        for event in events:
            # Left joystick X and Y
            if event.code == Input.left_y_axis.strip():
                if event.state == -1:
                    Input.left_y = 0
                else:
                    Input.left_y = event.state / 32768
            if event.code == Input.left_x_axis.strip():
                if event.state == -1:
                    Input.left_x = 0
                else:
                    Input.left_x = event.state / 32768

            # Right joystick X and Y
            if event.code == Input.right_y_axis.strip():
                if event.state == -1:
                    Input.right_y = 0
                else:
                    Input.right_y = event.state / 32768
            if event.code == Input.right_x_axis.strip():
                if event.state == -1:
                    Input.right_x = 0
                else:
                    Input.right_x = event.state / 32768

            # Left and right trigger
            if event.code == Input.right_trigger_axis.strip():
                if event.state == -1:
                    Input.right_trigger = 0
                else:
                    Input.right_trigger = event.state / 255
            if event.code == Input.left_trigger_axis.strip():
                if event.state == -1:
                    Input.left_trigger = 0
                else:
                    Input.left_trigger = event.state / 255

            # Left buttons
            if event.code == Input.left_up_button.strip():
                Input.left_up = event.state
            if event.code == Input.left_down_button.strip():
                Input.left_down = event.state
            if event.code == Input.left_left_button.strip():
                Input.left_left = event.state
            if event.code == Input.left_right_button.strip():
                Input.left_right = event.state

            # Right buttons
            if event.code == Input.right_up_button.strip():
                Input.right_up = event.state
            if event.code == Input.right_down_button.strip():
                Input.right_down = event.state
            if event.code == Input.right_left_button.strip():
                Input.right_left = event.state
            if event.code == Input.left_right_button.strip():
                Input.right_right = event.state
