import pyautogui
import time
import winsound
import tkinter as tk
import cv2
import numpy as np
import keyboard

# Função para fechar a janela popup
def fechar_popup():
    popup.destroy()

# Cores desejadas em formato hexadecimal
cor_verde = (170, 74, 68)  # Cor verde em formato RGB

# Coordenadas do quadrado na tela
quadrado_x = 100
quadrado_y = 100

# Dimensões do quadrado a ser capturado
tamanho_quadrado = 15

while True:
    # Verifica se a combinação de teclas Ctrl+M foi pressionada
    if keyboard.is_pressed('ctrl+m'):
        # Atualiza as coordenadas do quadrado para a posição atual do cursor
        quadrado_x, quadrado_y = pyautogui.position()

    # Captura a região da tela
    tela = pyautogui.screenshot(region=(quadrado_x, quadrado_y, tamanho_quadrado, tamanho_quadrado))

    # Desenha um quadrado verde na tela
    for x in range(quadrado_x, quadrado_x + tamanho_quadrado):
        for y in range(quadrado_y, quadrado_y + tamanho_quadrado):
            # Verifica se as coordenadas estão dentro dos limites da imagem
            if x < tela.width and y < tela.height:
                tela.putpixel((x - quadrado_x, y - quadrado_y), cor_verde)

    # Converte a imagem para o formato esperado pelo OpenCV
    frame = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2BGR)

    # Exibe a imagem em uma janela do OpenCV
    cv2.imshow("Quadrado Verde", frame)

    # Verifica cada pixel da tela capturada
    for x_rel in range(tela.width):
        for y_rel in range(tela.height):
            # Obtém a cor do pixel
            cor_pixel = tela.getpixel((x_rel, y_rel))

            # Verifica se a cor do pixel corresponde à cor verde
            if cor_pixel == cor_verde:
                # Aciona o sinal sonoro
                winsound.Beep(1000, 500)  # Beep de 1000 Hz por 500 milissegundos

                # Cria um popup para indicar que o sinal foi ativado
                popup = tk.Tk()
                popup.title("Sinal Ativado")
                popup.geometry("300x100")

                label = tk.Label(popup, text="Sinal Ativado!", font=("Arial", 14))
                label.pack(pady=10)

                btn_fechar = tk.Button(popup, text="Fechar", command=fechar_popup)
                btn_fechar.pack()

                popup.mainloop()

    # Aguarda um intervalo antes de verificar novamente
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)  # Verifica a tela a cada 100 milissegundos

# Liberando a captura de vídeo e fechando todas as janelas
cv2.destroyAllWindows()
