import cv2
import numpy as np

src = cv2.imread("roi.jpg")
cinza = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
bw = cv2.adaptiveThreshold(~cinza, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, -1)

# Cria imagens para linhas horizontais e verticais
horizontal = np.copy(bw)
vertical = np.copy(bw)
cv2.imshow("imagem binaria", bw)

# Criação do elemento estruturante e remoção das linhas usando processos de erosão e dilatação
horizontalsize = horizontal.shape[1] // 1000
estruturaHorizontal = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize, 1))
horizontal = cv2.erode(horizontal, estruturaHorizontal, anchor=(-1, -1))
horizontal = cv2.dilate(horizontal, estruturaHorizontal, anchor=(-1, -1))

verticalsize = vertical.shape[0] // 1000
estruturaVertical = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))
vertical = cv2.erode(vertical, estruturaVertical, anchor=(-1, -1))
vertical = cv2.dilate(vertical, estruturaVertical, anchor=(-1, -1))
vertical = cv2.bitwise_not(vertical)

cv2.imshow("resultado", vertical)
cv2.imwrite("sem-linhas.jpg", vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()