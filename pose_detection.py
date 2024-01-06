import cv2
import mediapipe as mp
from utils import draw_landmarks_on_image
from exercices import flexao

# model_path = 'pose_landmarker_lite.task'
model_path = 'pose_landmarker_heavy.task'

cap = cv2.VideoCapture(0)

# https://developers.google.com/mediapipe/solutions/vision/pose_landmarker/python
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a pose landmarker instance with the video mode:
options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE)

with PoseLandmarker.create_from_options(options) as landmarker:
  # The landmarker is initialized. Use it here.
  fps = cap.get(cv2.CAP_PROP_FPS) 
  calc_ts = 0   
  
  status = ''
  direction = ''
  count = 0
  while cap.isOpened():

    ret, frame = cap.read()
      
    # Image convert to MP formate
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    
    detection_result = landmarker.detect(mp_image)
    
    annotated_image = draw_landmarks_on_image(frame, detection_result)
    
    if len(detection_result.pose_landmarks) > 0:
      count, status, direction = flexao(detection_result.pose_landmarks, status, direction, count)
  
    cv2.imshow('frame', annotated_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      

cap.release()

cv2.destroyAllWindows()