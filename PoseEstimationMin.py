import  cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

Camera_id = 0
cap = cv2.VideoCapture(Camera_id)

pTime = 0

while True:
    ret, farme = cap.read()
    imgRGB = cv2.cvtColor(farme,cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(farme,results.pose_landmarks,
                              mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = farme.shape
            print(id, lm)
            cx, cy = int(lm.x*w),int(lm.y*h)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(farme,str(int(fps)),(50,50),
                cv2.FONT_ITALIC,2,(0,0,255),3)

    cv2.imshow('video', farme)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()