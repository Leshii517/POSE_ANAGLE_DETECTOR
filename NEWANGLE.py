import cv2
import numpy as np
import PoseModule as pm
import serial #Serial imported for Serial communication
import time #Required to use delay functions

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = pm.poseDetector(cap)
com_port = serial.Serial('COM8', 115200, timeout=.1)


def write_read(angle):
    print('Text to send: {0}'.format(angle))
    com_port.write(bytes(angle + '\n', 'ascii'))

    #time.sleep(0.1)
    # a = com_port.in_waiting
    while not com_port.in_waiting:
        pass

    data = com_port.readline()
    print('Received text: {0}'.format(data.decode()))#декодим для вывода значений в питон

time.sleep(2)

while True:
    success, img = cap.read()
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:

        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        write_read(str(angle))


    cv2.imshow("Image", img)
    cv2.waitKey(1)
