import pyautogui
import time
import winsound
import tkinter as tk
import keyboard

# Função para fechar a janela popup e parar o beep
def fechar_popup():
    popup.destroy()
    winsound.Beep(0, 0)  # Para o beep

# Função para ativar/desativar a leitura
def toggle_leitura():
    global leitura_ativa
    leitura_ativa = not leitura_ativa
    if leitura_ativa:
        btn_leitura.config(text="Desativar Leitura")
        lbl_estado.config(text="Leitura Ativada")
    else:
        btn_leitura.config(text="Ativar Leitura")
        lbl_estado.config(text="Leitura Desativada")

# Cores desejadas em formato hexadecimal
cores_desejadas = [(170, 74, 68), (65, 105, 225)]  # Cores desejadas em formato RGB

# Coordenadas do quadrado na tela
quadrado_x = 100
quadrado_y = 100

# Dimensões do quadrado a ser capturado
tamanho_quadrado = 15

# Flag para verificar se a leitura está ativa
leitura_ativa = False

# Inicializando a interface gráfica
root = tk.Tk()
root.title("Leitura de Cores")
root.geometry("300x150")

# Botão para ativar/desativar a leitura
btn_leitura = tk.Button(root, text="Ativar Leitura", command=toggle_leitura)
btn_leitura.pack(pady=10)

# Label para indicar o estado atual da leitura
lbl_estado = tk.Label(root, text="Leitura Desativada", font=("Arial", 12))
lbl_estado.pack()

# Loop principal
while True:
    # Verifica se a combinação de teclas Ctrl+M foi pressionada para atualizar as coordenadas do quadrado
    if keyboard.is_pressed('ctrl+m'):
        quadrado_x, quadrado_y = pyautogui.position()

    if leitura_ativa:
        # Captura a região da tela
        tela = pyautogui.screenshot(region=(quadrado_x, quadrado_y, tamanho_quadrado, tamanho_quadrado * 6))

        # Exibe o quadrado verde na tela
        for x in range(tamanho_quadrado):
            for y in range(tamanho_quadrado * 6):
                pyautogui.pixel(quadrado_x + x, quadrado_y + y, (0, 255, 0))

        # Verifica cada pixel da tela capturada
        for x_rel in range(tamanho_quadrado):
            for y_rel in range(tamanho_quadrado * 6):
                # Obtém a cor do pixel
                cor_pixel = tela.getpixel((x_rel, y_rel))

                # Verifica se a cor do pixel corresponde a uma das cores desejadas
                if cor_pixel in cores_desejadas:
                    # Se a cor do último pixel for diferente da cor atual, aciona o sinal sonoro
                    if ultima_cor_pixel != cor_pixel:
                        # Aciona o sinal sonoro
                        winsound.Beep(1000, 500)  # Beep de 1000 Hz por 500 milissegundos

                    # Atualiza a cor do último pixel
                    ultima_cor_pixel = cor_pixel

    # Aguarda um intervalo antes de verificar novamente
    time.sleep(0.1)  # Verifica a tela a cada 100 milissegundos

    # Atualiza a interface gráfica
    root.update()

    # Verifica se a janela foi fechada
    if not root.winfo_exists():
        break

# Liberando a captura de vídeo e fechando todas as janelas
root.destroy()
