# RecoilReducer
Este script em Python é um controlador de recuo automático para jogos FPS.

**Criei este script porque tenho dificuldade em controlar o movimento vertical do mouse devido minha doença degenerativa que limita meus movimentos. Este projeto é uma solução prática que me ajuda a superar essa limitação e aproveitar melhor os jogos.** Ele permite ajustar o movimento vertical do mouse enquanto o botão esquerdo está pressionado, simulando um controle de recuo. O usuário pode ajustar a intensidade do recuo usando as setas do teclado e o movimento é aplicado apenas enquanto o botão esquerdo está pressionado.

# Como Funciona

#### Movimento Vertical do Mouse:
Enquanto o botão esquerdo do mouse está pressionado, o script move o cursor verticalmente para compensar o recuo.
O movimento é controlado pela variável recuo, que define a quantidade de pixels que o mouse se move por ciclo.

#### Ajuste do Recuo com o Teclado:
Pressione a seta para cima ↑ para aumentar a compensação do recuo (movimento mais leve para baixo).

Pressione a seta para baixo ↓ para diminuir a compensação do recuo (movimento mais forte para baixo).

O valor do recuo é exibido no console sempre que for alterado.

#### Parada do Movimento:
O movimento é interrompido assim que o botão esquerdo do mouse é solto.

# Instruções para executar o script: 
**1 - Instalar o pyautogui**

No terminal ou prompt de comando, execute:

*pip install pyautogui*

**2 - Rodar o script**

Com o Python instalado, no terminal tente executar o código:

*python.exe recoil.py*

# Instruções para compilar para .exe:

**1 - Instale o PyInstaller** 

No terminal ou prompt de comando, execute:

*pip install pyinstaller*

**2 - Instalar o pyautogui**

No terminal ou prompt de comando, execute:

*pip install pyautogui*

> Se você estiver usando Python 3 e o comando acima não funcionar, tente:

*pip3 install pyautogui*
