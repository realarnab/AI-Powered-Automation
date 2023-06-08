import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_hand= mp.solutions.hands

tipIds = [4,8,12,16,20]
video=cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
 min_tracking_confidence=0.5) as hands:
 while True:
  ret,image = video.read()
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  image.flags.writeable=False
  results = hands.process(image)
  image.flags.writeable=True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  lmlist=[]
  if results.multi_hand_landmarks:
      for hand_landmark in results.multi_hand_landmarks:
          myHands=results.multi_hand_landmarks[0]
          for id, lm in enumerate(myHands.landmark):
              h,w,c = image.shape
              cx,cy = int(lm.x*w), int(lm.y*h)
              lmlist.append([id,cx,cy])
          mp_draw.draw_landmarks(image,hand_landmark,
mp_hand.HAND_CONNECTIONS)
  fingers=[]
  if len(lmlist) != 0:
      if lmlist[tipIds[0]][1] > lmlist[tipIds[0]-1][1]:
          fingers.append(1)
      else:
          fingers.append(0)
      for id in range(1,5):
          if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-
2][2]:
              fingers.append(1)
          else:
              fingers.append(0)
      total = fingers.count(1)
      print(total)
  cv2.imshow("Frame",image)
  k = cv2.waitKey(1)
  if k == ord("q"):
      break
video.release()
cv2.destroyAllWindows()