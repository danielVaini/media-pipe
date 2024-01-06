from utils import find_angle

def flexao(pose_landmarks, status, direction, count):
    angle = find_angle(pose_landmarks, 12, 14, 16)
    # lógica flexão
    if angle > 150:
        status = 'ready'
        direction = 'down'
    
    if status == 'ready':
        if direction == "down" and angle < 50:
            direction = 'up'
            count += 0.5
            return [count, status, direction]
        elif direction == "up" and angle > 140:
            direction = 'down'
            count += 0.5
            return [count, status, direction]
        else:
            return [count, status, direction]
    else:
        return [count, status, direction]