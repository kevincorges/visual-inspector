# ============================================================
# utils.py — Visual Inspector
# Funções utilitárias de visão computacional
# ============================================================

import cv2
import numpy as np
import matplotlib.pyplot as plt


# Grupo 1: Carregamento e exibição
def carregar_imagem(caminho):
    imagem_bgr = cv2.imread(caminho)
    imagem_rgb = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2RGB)
    return imagem_rgb

def exibir_imagem(imagem, titulo = "Imagem", cmap=None):
    plt.figure(figsize=(6,6))
    plt.imshow(imagem, cmap=cmap)
    plt.title(titulo)
    plt.axis("off")
    plt.show()

def exibir_comparacao(imagem1, titulo1, imagem2, titulo2, cmap1=None, cmap2=None):
    fig, eixos = plt.subplots(1, 2, figsize=(12, 6))
    
    eixos[0].imshow(imagem1, cmap=cmap1)
    eixos[0].set_title(titulo1)
    eixos[0].axis("off")
    
    eixos[1].imshow(imagem2, cmap=cmap2)
    eixos[1].set_title(titulo2)
    eixos[1].axis("off")
    
    plt.tight_layout()
    plt.show()

# Grupo 2: Manipulação de pixels
def desenhar_quadrado_preto(imagem):
    resultado = imagem.copy()
    resultado[0:50, 0:50] = [0, 0, 0]
    return resultado

def explodir_canal_vermelho(imagem):
    resultado = imagem.copy()
    altura, largura, _ = resultado.shape
    cy, cx = altura // 2, largura // 2
    resultado[cy-50:cy+50, cx-50:cx+50, 0] = 255
    return resultado

def binarizar(imagem, limiar=127):
    cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    binaria = np.where(cinza > limiar, 255, 0).astype(np.uint8)
    return binaria

# Grupo 3: Aritmética de imagens
def somar_imagens_numpy(imagem, valor=100):
    matriz = np.ones(imagem.shape, dtype=np.uint8) * valor
    return imagem + matriz

def somar_imagens_opencv(imagem, valor=100):
    matriz = np.ones(imagem.shape, dtype=np.uint8) * valor
    return cv2.add(imagem, matriz)

# Grupo 4: Filtro por cor e composição
def detectar_mudanca(imagem1, imagem2, limiar=5.0):
    cinza1 = cv2.cvtColor(imagem1, cv2.COLOR_RGB2GRAY)
    cinza2 = cv2.cvtColor(imagem2, cv2.COLOR_RGB2GRAY)
    diferenca = cv2.absdiff(cinza1, cinza2)
    media = np.mean(diferenca)
    if media > limiar:
        print(f"ALERTA: Mudança detectada! (média: {media:.2f})")
    else:
        print(f"Cena estável. (média: {media:.2f})")
    return diferenca

def criar_mascara_hsv(imagem, limite_inferior, limite_superior):
    hsv = cv2.cvtColor(imagem, cv2.COLOR_RGB2HSV)
    limite_inferior = np.array(limite_inferior, dtype=np.uint8)
    limite_superior = np.array(limite_superior, dtype=np.uint8)
    mascara = cv2.inRange(hsv, limite_inferior, limite_superior)
    return mascara

def efeito_sin_city(imagem, limite_inferior, limite_superior):
    mascara = criar_mascara_hsv(imagem, limite_inferior, limite_superior)
    objeto_colorido = cv2.bitwise_and(imagem, imagem, mask=mascara)
    cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    fundo_pb = cv2.cvtColor(cinza, cv2.COLOR_GRAY2RGB)
    mascara_invertida = cv2.bitwise_not(mascara)
    fundo_final = cv2.bitwise_and(fundo_pb, fundo_pb, mask=mascara_invertida)
    resultado = cv2.add(objeto_colorido, fundo_final)
    return resultado

