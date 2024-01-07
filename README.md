<h1 align="center"> Mediapipe - Pose Landmark Detection </h1>

## Executar

Clonar repositório:
```
git clone https://github.com/danielVaini/media-pipe.git
```

Entrar no diretório:

```
cd media-pipe
```

Executar o arquivo:
```
python pose_detection.py
```

## Adicionar novos exercícios

Buscar os pontos necessários representativos do corpo [aqui](https://developers.google.com/mediapipe/solutions/vision/pose_landmarker) e criar uma nova função no arquivo `exercices.py`:

```
def flexao(pose_landmarks, status, direction, count):
    angle = find_angle(pose_landmarks, 12, 14, 16) -> 12 , 14, 16 são os pontos necessários para calcular o ângulo do cotovelo
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
```

