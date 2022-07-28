import cv2
import mediapipe as mp
import time
import math

class poseDetector():

    def __init__(self, mode=True, upBody=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle3(self, img, p7, p8, p9, draw=True):

        x7, y7 = self.lmList[p7][1:]
        x8, y8 = self.lmList[p8][1:]
        x9, y9 = self.lmList[p9][1:]

        angle3 = math.degrees(math.atan2(y8 - y7, x8 - x7) -
                              math.atan2(y8 - y9, x8 - x9))

        if angle3 > 180:
            angle3 = 200

        cv2.line(img, (x7, y7), (x8, y8), (255, 255, 255), 3)
        cv2.line(img, (x8, y8), (x9, y9), (255, 255, 255), 3)
        cv2.circle(img, (x7, y7), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x7, y7), 15, (0, 0, 255), 2)
        cv2.circle(img, (x8, y8), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x8, y8), 15, (0, 0, 255), 2)
        cv2.circle(img, (x9, y9), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x9, y9), 15, (0, 0, 255), 2)
        cv2.putText(img, str(int(angle3)), (x8 - 50, y8 + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle3

    def findAngle2(self, img, p4, p5, p6, draw=True):


        # Get the landmarks
        x4, y4 = self.lmList[p4][1:]
        x5, y5 = self.lmList[p5][1:]
        x6, y6 = self.lmList[p6][1:]


        # Calculate the Angle
        angle2 = math.degrees(math.atan2(y4 - y6, x4 - x6) -
                              math.atan2(y6 - y5, x6 - x5))



        if angle2 > 200:
            angle2 = 180



        cv2.line(img, (x4, y4), (x5, y5), (255, 255, 255), 3)
        cv2.line(img, (x5, y5), (x6, y6), (255, 255, 255), 3)
        cv2.circle(img, (x4, y4), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x4, y4), 15, (0, 0, 255), 2)
        cv2.circle(img, (x5, y5), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x5, y5), 15, (0, 0, 255), 2)
        cv2.circle(img, (x6, y6), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(img, (x6, y6), 15, (0, 0, 255), 2)
        cv2.putText(img, str(int(angle2)), (x5 - 50, y5 + 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


        return angle2

    def findAngle1(self, img, p1, p2, p3, draw=True):

        # Get the landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        # Calculate the Angle
        angle1 = math.degrees(math.atan2(y2 - y3, x2 - x3) -
                             math.atan2(y1 - y2, x1 - x2))

        if angle1 > 180:
            angle1 = 200

        # Draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)

            cv2.putText(img, str(int(angle1)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        return angle1

if __name__ == "__main__":
    main()