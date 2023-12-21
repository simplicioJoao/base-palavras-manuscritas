import cv2
image = cv2.imread('base/Christine aula 1.png')

# Corte da imagem para extração da região com as palavras manuscritas
inicio_x, inicio_y = 900, 500
largura, altura = 1200, 3400
fim_x, fim_y = inicio_x + largura, inicio_y + altura
roi = image[inicio_y:fim_y, inicio_x:fim_x]

# Conversão da imagem para tons de cinza e limiarização
cinza = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
_, limiarizada = cv2.threshold(cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Imagem binarizada", limiarizada)
cv2.imwrite("roi.jpg", limiarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()