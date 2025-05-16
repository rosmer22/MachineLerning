# Importación de librerías necesarias
import cv2

# ------------------------------------------
# 1. Carga y visualización de imagen en color y escala de grises
# ------------------------------------------
imagen = cv2.imread('Imagenes/lenna.png')
imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('Lenna Original', imagen)
cv2.imshow('Lenna Escala grises', imagen_grises)
cv2.imwrite('Imagenes/lenna_gray_2024.png', imagen_grises)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------
# 2. Imagen binarizada
# ------------------------------------------
imagen = cv2.imread('Imagenes/cat_gray.png', cv2.IMREAD_GRAYSCALE)
ret, binary = cv2.threshold(imagen, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('Gato en escala Grises', imagen)
cv2.imshow('Gato en binario', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------
# 3. Video en tiempo real desde webcam
# ------------------------------------------
camara = cv2.VideoCapture(0)
while True:
    success, img = camara.read()
    if not success:
        break
    cv2.imshow("Video de camara", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Tecla ESC para salir
        break
cv2.destroyAllWindows()
camara.release()

# ------------------------------------------
# 4. Video desde una cámara IP
# ------------------------------------------
ip_url = 'http://162.191.11.144:8000/-wvhttp-01-/GetOneShot?image_size=640x480&frame_count=1000000000'
cap = cv2.VideoCapture(ip_url)
while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow("Video de camara IP", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
cap.release()

# ------------------------------------------
# 5. Video desde archivo
# ------------------------------------------
cap = cv2.VideoCapture('Videos/600_final.mp4')
while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
cap.release()

# ------------------------------------------
# 6. Video en escala de grises en vivo
# ------------------------------------------
cap = cv2.VideoCapture('http://10.107.136.149:8080/video')
while True:
    success, img = cap.read()
    if not success:
        break
    imagen_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video", imagen_grises)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
cap.release()

# ------------------------------------------
# 7. Mostrar tres tipos de video en tiempo real
# ------------------------------------------
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    if not success:
        break
    imagen_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, imagen_binaria = cv2.threshold(imagen_grises, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Video RGB", img)
    cv2.imshow("Video Escala Grises", imagen_grises)
    cv2.imshow("Video Binarizado", imagen_binaria)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
cap.release()

# ------------------------------------------
# 8. Detección de rostros con DLIB (requiere modelo)
# ------------------------------------------
try:
    from imutils import face_utils
    import dlib

    detector_rostro = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("Modelos/shape_predictor_68_face_landmarks.dat")

    cap = cv2.VideoCapture(0)
    while True:
        success, image = cap.read()
        if not success:
            break
        imagen_grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rects = detector_rostro(imagen_grises, 0)

        for rect in rects:
            shape = predictor(imagen_grises, rect)
            shape = face_utils.shape_to_np(shape)
            for (x, y) in shape:
                cv2.circle(image, (x, y), 2, (255, 255, 0), -1)

        cv2.imshow("Video local", image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
except ModuleNotFoundError as e:
    print("Error:", e)
    print("Por favor instala el módulo faltante con: pip install dlib imutils")
