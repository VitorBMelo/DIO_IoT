# -*- coding: utf-8 -*-
"""Reconhecimento_Facial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hQnPO_PE8trrmfEOgteYPiHFG19lPcvS

### Preparação do Ambiente
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

"""### Carregamento de um Modelo de Detecção de Faces Pré-Treinado"""

import cv2

# Carregar o modelo Haar Cascade para detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

"""### Detecção de Faces em uma Imagem"""

# Carregar a imagem
image_path = 'images/harry_porter2.jpeg'
image = cv2.imread(image_path)

# Converter a imagem para escala de cinza (necessário para a detecção de faces)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar faces na imagem
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

"""### Visualização das Faces Detectadas"""

# Desenhar retângulos ao redor das faces detectadas na imagem original
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Converter a imagem OpenCV (BGR) para RGB (para exibição com matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Exibir a imagem com as faces detectadas
plt.imshow(image_rgb)
plt.axis('off')
plt.show()
