# RecoilReducer  
Este script em Python é um controlador de recuo automático para jogos FPS.

**Criei este script porque tenho dificuldade em controlar o movimento vertical do mouse devido minha doença degenerativa que limita meus movimentos. Este projeto é uma solução prática que me ajuda a superar essa limitação e aproveitar melhor os jogos.** Ele permite ajustar o movimento vertical do mouse enquanto o botão esquerdo está pressionado, simulando um controle de recuo. O usuário pode ajustar a intensidade do recuo usando a interface gráfica, ativar ou desativar o sistema manualmente e usar uma te...

# Como Funciona

#### Interface Gráfica:  
O script agora possui uma interface simples desenvolvida com **Tkinter**, facilitando seu uso sem depender de atalhos fixos no teclado.

#### Ativação:  
- O controle de recuo **só funciona quando ativado manualmente** pelo botão “Ativar” na interface ou via tecla de atalho configurada pelo usuário.  
- Ao ativar, um som padrão do Windows é reproduzido para confirmar a ativação.  
- Ao desativar, o recuo é desabilitado imediatamente.

#### Movimento Vertical do Mouse:  
- Quando ativado e o botão esquerdo do mouse é pressionado, o cursor é movido para baixo de forma contínua.  
- O movimento é feito via API do Windows (`mouse_event`), simulando o movimento físico do mouse para garantir funcionamento em jogos em tela cheia e modo mira.

#### Ajuste de Recuo:  
- Os botões “+” e “-” na interface aumentam ou diminuem o valor do recuo (intensidade do movimento).  
- O valor atual do recuo é mostrado em tempo real na interface e também na overlay flutuante na tela do usuário.  
- Esses botões só ficam ativos quando o script estiver ativado.

#### Overlay Flutuante:  
- Um pequeno texto transparente aparece no canto inferior esquerdo da tela, mostrando o status “Ativo” ou “Inativo” e o valor atual do recuo.  
- A overlay fica sempre no topo, mesmo sobre jogos em tela cheia, sem injetar nada no jogo.

#### Indicadores de Estado na Interface:  
- Exibe se o sistema está ativado ou desativado.  
- Exibe se o botão esquerdo do mouse está sendo pressionado (“🟢 Clicando” ou “🔴 Não clicando”).

#### Tecla de Atalho Personalizável:  
- O usuário pode clicar no campo de texto e pressionar qualquer tecla para configurar um atalho de teclado para ativar/desativar o recuo.  
- Isso permite alternar o recuo sem precisar minimizar o jogo ou interagir diretamente com a interface.

#### Parada do Movimento:  
- O movimento cessa automaticamente assim que o botão esquerdo do mouse é solto.  
- Ou imediatamente quando o sistema for desativado manualmente.

# Instruções para executar o script:

**1 - Instalar as bibliotecas necessárias:**  

No terminal, execute:

```bash
pip install pynput
```

> Se estiver usando Python 3 e o comando acima não funcionar, tente:

```bash
pip3 install pynput
```

**2 - Rodar o script**

Com o Python instalado, execute:

```bash
python.exe recoil.py
```

# Instruções para compilar para .exe:

**1 - Instale o PyInstaller**

No terminal ou prompt de comando, execute:

```bash
pip install pyinstaller
```

**2 - Compile o script**

Execute no terminal (na pasta onde está o script):

```bash
pyinstaller --onefile --windowed recoil.py
```

- O executável será gerado dentro da pasta `dist/`.

---

Desenvolvido com acessibilidade e praticidade em mente. 💡

---
