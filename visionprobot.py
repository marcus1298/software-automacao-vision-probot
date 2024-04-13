import tkinter as tk
from tkinter import simpledialog, Canvas
import pyautogui
from PIL import ImageGrab
from pynput import keyboard
import threading

# Cores de interesse e seus pontos
action_points = {}
read_point = (100, 100)  # Ponto inicial arbitrário

# Função para capturar o ponto de leitura e ação
def set_point(point_type, x, y):
    if point_type == 'read':
        global read_point
        read_point = (x, y)
        print(f"Ponto de leitura configurado para: {read_point}")
    else:
        action_points[point_type] = (x, y)
        print(f"Ponto de ação para {point_type} configurado para: {action_points[point_type]}")

# Detectar cor em um ponto específico
def get_color_at(x, y):
    screen = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    return screen.getpixel((0, 0))

# Executar ação baseada na cor
def execute_action():
    while True:
        color = get_color_at(*read_point)
        for color_name, point in action_points.items():
            if color == COLORS[color_name]:
                pyautogui.click(*point)
                print(f"Ação executada em {point} para a cor {color_name}")
        pyautogui.sleep(1)

# Thread de monitoramento
def start_monitoring():
    monitoring_thread = threading.Thread(target=execute_action)
    monitoring_thread.daemon = True
    monitoring_thread.start()

# Interface gráfica e configuração
def open_config_gui():
    def on_click(event, color):
        set_point(color, event.x_root, event.y_root)
        canvas.create_oval(event.x_root-5, event.y_root-5, event.x_root+5, event.y_root+5, fill=color, width=0)
        root.destroy()

    root = tk.Tk()
    root.title("Configuração do Bot")
    canvas = Canvas(root, width=pyautogui.size().width, height=pyautogui.size().height)
    canvas.pack()
    canvas.bind("<Button-1>", lambda event, col='Branco': on_click(event, col))
    canvas.bind("<Button-2>", lambda event, col='Vermelho': on_click(event, col))
    canvas.bind("<Button-3>", lambda event, col='Azul': on_click(event, col))
    root.mainloop()

# Hotkeys
def on_press(key):
    if key == keyboard.Key.ctrl_l:
        listener = keyboard.Listener(on_release=on_release)
        listener.start()

def on_release(key):
    if key == keyboard.Key.m:
        print("Modo de configuração ativado")
        open_config_gui()
    elif key == keyboard.Key.n:
        x, y = pyautogui.position()
        set_point('read', x, y)

# Iniciação
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

start_monitoring()

# Cores de interesse
COLORS = {'Branco': (255, 255, 255), 'Vermelho': (255, 0, 0), 'Azul': (0, 0, 255)}
