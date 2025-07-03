import ctypes
import threading
import time
import tkinter as tk
from tkinter import ttk
from pynput import mouse, keyboard
import winsound

# ==== Configurações ====
SOM_SISTEMA = winsound.MB_ICONASTERISK

# ==== Variáveis globais ====
recuo = 0
clicando = False
thread_ativa = False
ativo = False

MOUSEEVENTF_MOVE = 0x0001

# Tecla de atalho para toggle (default None)
tecla_atalho = None
capturando_tecla = False

def tocar_som_ativado():
    try:
        winsound.MessageBeep(SOM_SISTEMA)
    except:
        pass

def mover_mouse_relativo(x, y):
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, x, y, 0, 0)

def atualizar_status_ativo():
    status = "✅ Ativo" if ativo else "❌ Inativo"
    status_label.config(text=status)
    overlay_label.config(text=f"{status} | Recuo: {recuo}")

def atualizar_status_clicando():
    clicando_texto = "🟢 Clicando" if clicando else "🔴 Não clicando"
    clicando_label.config(text=clicando_texto)

def movimentar_mouse():
    global thread_ativa
    while clicando and ativo:
        mover_mouse_relativo(0, recuo)
        time.sleep(0.02)
    thread_ativa = False
    atualizar_status_clicando()

def ao_clicar(x, y, button, pressed):
    global clicando, thread_ativa
    if not ativo:
        return
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
    if ativo:
        overlay_label.config(text=f"✅ Ativo | Recuo: {recuo}")
    else:
        overlay_label.config(text=f"❌ Inativo | Recuo: {recuo}")

def diminuir_recuo():
    global recuo
    recuo -= 1
    recuo_label.config(text=f"Recuo atual: {recuo}")
    if ativo:
        overlay_label.config(text=f"✅ Ativo | Recuo: {recuo}")
    else:
        overlay_label.config(text=f"❌ Inativo | Recuo: {recuo}")

def sair():
    global clicando, ativo
    clicando = False
    ativo = False
    overlay.destroy()
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

def atualizar_entry_tecla():
    if tecla_atalho is None:
        tecla_entry_var.set("Clique aqui e pressione a tecla")
    else:
        tecla_entry_var.set(f"Tecla: {tecla_atalho}")

def on_tecla_press_captura(key):
    global tecla_atalho, capturando_tecla
    try:
        tecla_str = None
        if hasattr(key, 'char') and key.char is not None:
            tecla_str = key.char.lower()
        else:
            tecla_str = str(key).replace('Key.', '').lower()
        
        tecla_atalho = tecla_str
        capturando_tecla = False
        atualizar_entry_tecla()
        return False  # para parar a captura
    except Exception:
        return False

def iniciar_captura_tecla(event):
    global capturando_tecla
    if not capturando_tecla:
        capturando_tecla = True
        tecla_entry_var.set("Pressione a tecla desejada...")
        listener_tecla = keyboard.Listener(on_press=on_tecla_press_captura)
        listener_tecla.start()

def on_tecla_global_press(key):
    global tecla_atalho
    try:
        tecla_str = None
        if hasattr(key, 'char') and key.char is not None:
            tecla_str = key.char.lower()
        else:
            tecla_str = str(key).replace('Key.', '').lower()
        if tecla_str == tecla_atalho:
            toggle_ativo()
    except Exception:
        pass

# ==== Interface principal ====
root = tk.Tk()
root.title("Recuo Assistivo (RecoilReducer)")
root.geometry("300x320")
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

# Campo para capturar tecla
tecla_entry_var = tk.StringVar()
tecla_entry = ttk.Entry(frame, textvariable=tecla_entry_var, font=("Arial", 11), justify="center", state="readonly", width=25)
tecla_entry.pack(pady=10)
tecla_entry.bind("<Button-1>", iniciar_captura_tecla)
atualizar_entry_tecla()

sair_btn = ttk.Button(frame, text="Sair", command=sair)
sair_btn.pack(pady=10)

# ==== Overlay flutuante ====
overlay = tk.Toplevel(root)
overlay.overrideredirect(True)
overlay.attributes('-topmost', True)
overlay.attributes('-alpha', 0.8)

screen_width = overlay.winfo_screenwidth()
screen_height = overlay.winfo_screenheight()
overlay.geometry(f"100x25+10+{screen_height - 60}")

overlay_label = tk.Label(overlay, text="❌ Inativo | Recuo: 0", font=("Arial", 7), bg="black", fg="white")
overlay_label.pack(fill="both", expand=True)

# ==== Listeners ====
mouse_listener = mouse.Listener(on_click=ao_clicar)
mouse_listener.start()

keyboard_listener = keyboard.Listener(on_press=on_tecla_global_press)
keyboard_listener.start()

root.mainloop()