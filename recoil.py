import pyautogui
from pynput import mouse, keyboard
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
import time
import threading

# Variável global para ajustar o recuo
recuo = 0
clicando = False
thread_ativa = False  # Evita criar múltiplas threads

def ajustar_recuo(key):
    global recuo
    if key == Key.up:
        recuo += 1  # Aumenta o recuo (sobe menos)
        print(f"Recuo ajustado para: {recuo}")
    elif key == Key.down:
        recuo -= 1  # Diminui o recuo (sobe mais)
        print(f"Recuo ajustado para: {recuo}")

def movimentar_mouse():
    global recuo, clicando, thread_ativa
    while clicando:
        pyautogui.move(0, recuo)  # Move o mouse verticalmente
        time.sleep(0.02)  # Intervalo para reduzir o consumo de recursos
    thread_ativa = False  # Marca a thread como inativa

def ao_clicar(x, y, button, pressed):
    global clicando, thread_ativa
    if button == mouse.Button.left:
        clicando = pressed
        if clicando and not thread_ativa:  # Inicia uma thread apenas se não houver outra ativa
            thread_ativa = True
            threading.Thread(target=movimentar_mouse, daemon=True).start()

def ao_teclar(key):
    try:
        ajustar_recuo(key)
    except Exception as e:
        print(f"Erro ao ajustar recuo: {e}")

def main():
    print("Iniciando controle de recuo.")
    print("Use as setas para ajustar o nível e clique esquerdo para ativar o recuo.")
    print("Pressione 'ESC' para sair.")
    
    with MouseListener(on_click=ao_clicar) as mouse_listener, KeyboardListener(on_press=ao_teclar) as keyboard_listener:
        keyboard_listener.join()
        mouse_listener.join()

if __name__ == "__main__":
    main()