from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import math

def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop through the detected poses to visualize.
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Draw the pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image

# https://youtu.be/Ivummjqaaa8?t=3623
def find_angle(landmarks, p1, p2, p3):
  land = landmarks[0]
  
  x1, y1 = (land[p1].x, land[p1].y)
  x2, y2 = (land[p2].x, land[p2].y)
  x3, y3 = (land[p3].x, land[p3].y)
  
  angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
  
  return angle
      