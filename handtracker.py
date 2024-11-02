import cv2 
import mediapipe as mp 

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

fingerIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    lmList = []

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            if len(lmList) == 21:  
                fingerList = []
                if lmList[fingerIds[0]][1] < lmList[fingerIds[0]-2][1]:
                    fingerList.append(1)
                else:
                    fingerList.append(0)
                for i in range(1, 5):
                    if lmList[fingerIds[i]][2] < lmList[fingerIds[i] - 2][2]:
                        fingerList.append(1)  
                    else:
                        fingerList.append(0)  
                totalFingers = sum(fingerList)
                cv2.putText(img,f'{totalFingers}',(30,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,0,255),3)
    cv2.imshow('Hand Tracker', img)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
