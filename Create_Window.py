import cv2
import mediapipe as mp
mp_draw = mp.solutions.drawing_utils
mp_hand= mp.solutions.hands

video=cv2.VideoCapture(0)
with mp_hand.Hands(min_detection_confidence=0.5,
 min_tracking_confidence=0.5) as hands:
  while True:
   ret,image = video.read()
   cv2.imshow("Frame",image)
   k = cv2.waitKey(1)
   if k == ord("q"):
       break
video.release()
cv2.destroyAllWindows()