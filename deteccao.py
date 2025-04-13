import cv2  # Importa a biblioteca OpenCV para visão computacional

# Carrega o classificador pré-treinado para detecção de faces do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carrega o arquivo de vídeo (substitua 'video.mp4' pelo nome do seu vídeo, se diferente)
cap = cv2.VideoCapture('testei a base da virginia.mp4')

# Verifica se o arquivo de vídeo foi aberto com sucesso
if not cap.isOpened():
    print("Erro: Não foi possível abrir o arquivo de vídeo.")
    exit()  # Interrompe o programa se o vídeo não puder ser aberto

# Inicia um loop infinito para processar o vídeo
while True:
    # Lê um frame do vídeo
    ret, frame = cap.read()

    # Converte o frame para escala de cinza (a detecção de faces funciona melhor em escala de cinza)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta faces no frame em escala de cinza
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenha um retângulo azul ao redor de cada face detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Cor azul em BGR

    # Mostra o frame com as faces detectadas em uma janela
    cv2.imshow('Detecção de Faces', frame)

    # Espera por 1 milissegundo e verifica se 'q' foi pressionado para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Sai do loop se 'q' for pressionado

# Libera o arquivo de vídeo e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()