import ctypes
import threading
import time
import tkinter as tk
from tkinter import ttk
from pynput import mouse
import winsound

# ==== Configurações ====
SOM_SISTEMA = winsound.MB_ICONASTERISK

# ==== Variáveis globais ====
recuo = 0
clicando = False
thread_ativa = False
ativo = False  # controle se recuo está ativado via botão

MOUSEEVENTF_MOVE = 0x0001

def tocar_som_ativado():
    try:
        winsound.MessageBeep(SOM_SISTEMA)
    except Exception as e:
        print(f"[Erro ao tocar som do sistema]: {e}")

def mover_mouse_relativo(x, y):
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, x, y, 0, 0)

def atualizar_status_ativo():
    status = "✅ Ativo" if ativo else "❌ Inativo"
    status_label.config(text=status)

def atualizar_status_clicando():
    clicando_texto = "🟢 Clicando" if clicando else "🔴 Não clicando"
    clicando_label.config(text=clicando_texto)

def movimentar_mouse():
    global thread_ativa
    while clicando and ativo:
        mover_mouse_relativo(0, recuo)
        time.sleep(0.02)
    thread_ativa = False
    # Quando parar de clicar, atualiza status clicando
    atualizar_status_clicando()

def ao_clicar(x, y, button, pressed):
    global clicando, thread_ativa
    if not ativo:
        return  # se não ativado, ignora clique
    if button == mouse.Button.left:
        clicando = pressed
        atualizar_status_clicando()
        if clicando and not thread_ativa:
            thread_ativa = True
            threading.Thread(target=movimentar_mouse, daemon=True).start()

def aumentar_recuo():
    global recuo
    recuo += 1
    recuo_label.config(text=f"Recuo atual: {recuo}")

def diminuir_recuo():
    global recuo
    recuo -= 1
    recuo_label.config(text=f"Recuo atual: {recuo}")

def sair():
    global clicando, ativo
    clicando = False
    ativo = False
    root.destroy()

def toggle_ativo():
    global ativo
    ativo = not ativo
    tocar_som_ativado()
    atualizar_status_ativo()
    atualizar_status_clicando()
    if ativo:
        ativar_btn.config(text="Desativar")
        menos_btn.config(state="normal")
        mais_btn.config(state="normal")
    else:
        ativar_btn.config(text="Ativar")
        menos_btn.config(state="disabled")
        mais_btn.config(state="disabled")

root = tk.Tk()
root.title("Recuo Assistivo (RecoilReducer)")
root.geometry("250x250")
root.resizable(False, False)

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

recuo_label = ttk.Label(frame, text=f"Recuo atual: {recuo}", font=("Arial", 12))
recuo_label.pack(pady=10)

btn_frame = ttk.Frame(frame)
btn_frame.pack(pady=5)

menos_btn = ttk.Button(btn_frame, text=" - ", command=diminuir_recuo, width=5, state="disabled")
menos_btn.pack(side="left", padx=10)

mais_btn = ttk.Button(btn_frame, text=" + ", command=aumentar_recuo, width=5, state="disabled")
mais_btn.pack(side="left", padx=10)

status_label = ttk.Label(frame, text="❌ Inativo", font=("Arial", 11))
status_label.pack(pady=5)

clicando_label = ttk.Label(frame, text="🔴 Não clicando", font=("Arial", 11))
clicando_label.pack(pady=5)

ativar_btn = ttk.Button(frame, text="Ativar", command=toggle_ativo)
ativar_btn.pack(pady=10)

sair_btn = ttk.Button(frame, text="Sair", command=sair)
sair_btn.pack(pady=10)

mouse_listener = mouse.Listener(on_click=ao_clicar)
mouse_listener.start()

root.mainloop()