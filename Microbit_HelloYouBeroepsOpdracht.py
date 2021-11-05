import speech

def on_gesture_tilt_left():
    radio.send_string(Alarm)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_received_string(receivedString):
    basic.show_string(receivedString)
    speech.say("Alarm Alarm Alarm")
radio.on_received_string(on_received_string)

def on_gesture_tilt_right():
    radio.send_string(Alarm)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

Alarm = ""
Alarm = "Alarm"
radio.set_group(21)