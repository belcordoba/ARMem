import cv2
import numpy as np

# Tamaño del marcador
marker_size = 200

# Crear un diccionario de marcadores ARUCO
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)


# Crear una imagen en blanco
image_size = marker_size * 8
image = np.ones((image_size, image_size), dtype=np.uint8) * 255

# Crear y dibujar cada marcador en la imagen
for i in range(250):
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, i, marker_size)
    cv2.imshow("img", marker_image)
    cv2.imwrite(f"markers/marker_{i}.png", marker_image)