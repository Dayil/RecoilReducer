# RecoilReducer
Este script em Python é um controlador de recuo automático para jogos FPS.

**Criei este script porque tenho dificuldade em controlar o movimento vertical do mouse devido minha doença degenerativa que limita meus movimentos. Este projeto é uma solução prática que me ajuda a superar essa limitação e aproveitar melhor os jogos.** Ele permite ajustar o movimento vertical do mouse enquanto o botão esquerdo está pressionado, simulando um controle de recuo. O usuário pode ajustar a intensidade do recuo usando as setas do teclado e o movimento é aplicado apenas enquanto o botão esquerdo está pressionado.

# Como Funciona

#### Interface Gráfica:
O script agora possui uma interface simples desenvolvida com **Tkinter**, facilitando seu uso sem depender de atalhos no teclado.

#### Ativação:
- O controle de recuo **só funciona quando ativado manualmente** através do botão “Ativar” na interface.
- Ao ativar, um som padrão do Windows é reproduzido para confirmar a ativação.
- Ao desativar, o recuo é desabilitado imediatamente.

#### Movimento Vertical do Mouse:
- Quando ativado e o botão esquerdo do mouse for pressionado, o cursor é movido para baixo de forma contínua.
- O movimento é simulado de forma relativa (como se o mouse estivesse sendo fisicamente movido), o que permite funcionar mesmo em jogos em modo de mira ou tela cheia.

#### Ajuste de Recuo:
- Os botões “+” e “-” da interface permitem aumentar ou diminuir o valor do recuo (intensidade do movimento).
- O valor atual do recuo é mostrado em tempo real na interface.
- Esses botões só ficam ativos após ativar o script.

#### Indicadores de Estado:
- A interface exibe dois estados:
  - Se o sistema está **ativado ou desativado**.
  - Se o botão esquerdo do mouse está sendo pressionado (exibindo “🟢 Clicando” ou “🔴 Não clicando”).

#### Parada do Movimento:
- O movimento cessa automaticamente assim que o botão do mouse é solto.
- Ou, se o sistema for desativado manualmente.

# Instruções para executar o script:

**1 - Instalar as bibliotecas necessárias:**

No terminal, execute:

*pip install pynput*

> Se você estiver usando Python 3 e o comando acima não funcionar, tente:

*pip3 install pynput*

**2 - Rodar o script**

Com o Python instalado, no terminal tente executar o código:

*python.exe recoil.py*

# Instruções para compilar para .exe:

**1 - Instale o PyInstaller** 

No terminal ou prompt de comando, execute:

*pip install pyinstaller*

**2 - Compile o script**

Execute no terminal (estando na pasta onde está o script):

*pyinstaller --onefile --windowed recoil.py*

- O executável será gerado dentro da pasta `dist/`.

---

Desenvolvido com acessibilidade e praticidade em mente. 💡
