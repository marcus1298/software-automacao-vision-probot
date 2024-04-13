import pyautogui
import time
import winsound
import tkinter as tk
import cv2
import numpy as np
import keyboard

# Função para fechar a janela popup e parar o beep
def fechar_popup():
    popup.destroy()
    winsound.Beep(0, 0)  # Para o beep

# Cores desejadas em formato hexadecimal
cores_desejadas = [(170, 74, 68), (65, 105, 225)]  # Cor verde em formato RGB

# Coordenadas do quadrado na tela
quadrado_x = 100
quadrado_y = 100

# Dimensões do quadrado a ser capturado
tamanho_quadrado = 15

# Flag para verificar se o beep está sendo reproduzido
beep_ativo = False

while True:
    # Verifica se a combinação de teclas Ctrl+M foi pressionada
    if keyboard.is_pressed('ctrl+m'):
        # Atualiza as coordenadas do quadrado para a posição atual do cursor
        quadrado_x, quadrado_y = pyautogui.position()

    # Captura a região da tela
    tela = pyautogui.screenshot(region=(quadrado_x, quadrado_y, tamanho_quadrado, tamanho_quadrado*6))

    # Converte a imagem para o formato esperado pelo OpenCV
    frame = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2BGR)

    # Exibe a imagem em uma janela do OpenCV
    cv2.imshow("Quadrado Verde", frame)

    # Inicializa a cor do último pixel como None
    ultima_cor_pixel = None

    # Verifica cada pixel da tela capturada
    for x_rel in range(tela.width):
        for y_rel in range(tela.height):
            # Obtém a cor do pixel
            cor_pixel = tela.getpixel((x_rel, y_rel))

            # Verifica se a cor do pixel corresponde à cor verde
            if cor_pixel in cores_desejadas:
                # Se a cor do último pixel for diferente da cor atual, aciona o sinal sonoro
                if ultima_cor_pixel != cores_desejadas:
                    # Verifica se o beep está ativo
                    if not beep_ativo:
                        # Aciona o sinal sonoro
                        winsound.Beep(1000, 500)  # Beep de 1000 Hz por 500 milissegundos
                        beep_ativo = True

                # Atualiza a cor do último pixel
                ultima_cor_pixel = cores_desejadas
            else:
                # Se a cor do último pixel for verde, atualiza a cor do último pixel e para o beep
                if ultima_cor_pixel == cores_desejadas:
                    ultima_cor_pixel = cor_pixel
                    beep_ativo = False

    # Aguarda um intervalo antes de verificar novamente
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)  # Verifica a tela a cada 100 milissegundos

# Liberando a captura de vídeo e fechando todas as janelas
cv2.destroyAllWindows()
