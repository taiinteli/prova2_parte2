

# Classificador aplicado ao conceito de cascata de cassificadores dado na documentação como exemplo junto com a exemplificação da questão, com esses matérias tentei usar no desenvolvimento da solução. 

import numpy as np
import cv2

input_video = cv2.VideoCapture('../assets/arsene.mp4')
output_video = cv2.VideoWriter( './saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height)) 

# após identificar os rostos nos frames do vídeos, usando a base do Cascata de Classificadores: 

face_cascade  =  cv2 . CascadeClassifier ( 'haarcascade_frontalface_default.xml' ) 

# seria interessante exibir o frame

while True:
 
    # exibe o frame
    cv2.imshow('Video Playback', frame)
    
    # escreve o frame no output
    output_video.write(frame)

    # se o usuario apertar q, encerra o playback
    # o valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


output_video.release()
input_video.release()
cv2.destroyAllWindows()


# a ideia seria implementar um for bem parecido com esse que pega o resultado do classificador das faces e localiza elas em cada frame do vídeo, desenlhando um retângulo vermelho quando for encontrada por RGB, ou seja "255, 0, 0" 
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
 
