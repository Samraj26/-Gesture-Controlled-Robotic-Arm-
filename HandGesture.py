from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=1)
mySerial = SerialObject("/dev/cu.usbmodem14101", 9600, 1)

while True:
# Get image frame
   success, img = cap.read()
# Find the hand and its landmarks
   hands, img = detector.findHands(img)# with draw
#hands = detector.findHands(img, draw=False) # without draw

   if hands:
    # Hand 1
    hand1 = hands[0]
    lmList1 = hand1["lmList"]  # List of 21 Landmark points
    bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
    centerPoint1 = hand1['center']  # center of the hand cx,cy
    handType1 = hand1["type"]  # Handtype Left or Right
    if hands:
       fingers1 = detector.fingersUp(hand1)
       print(fingers1)
       mySerial.sendData(fingers1)
# Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
