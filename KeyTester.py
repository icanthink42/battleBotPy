from inputs import get_gamepad

while True:
    events = get_gamepad()
    for event in events:
        print("Code: " + str(event.code))
        print("State: " + str(event.state))
