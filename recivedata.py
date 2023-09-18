import pyrebase
from cvzone.SerialModule import SerialObject


mySerial = SerialObject("/dev/cu.usbmodem14101", 9600, 1)

# Configure your Firebase project using the provided Firebase config
firebase_config = {

}

firebase = pyrebase.initialize_app(firebase_config)

# Get a reference to the Firebase Realtime Database
db = firebase.database()

# Retrieve data under the "HAND GESTURE" node
while 1:
    hand_gesture_data = db.child("HAND GESTURE").get()

    # Convert the data to a string
    hand_gesture_data_str = ' '.join(map(str, hand_gesture_data))
    # Print the retrieved data
    mySerial.sendData(hand_gesture_data.val())

    print(hand_gesture_data.val())  # .val() returns the data as a Python dictionary
