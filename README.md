# software-automacao-vision-probot
Manual do Usuário para o Software de Automação de Mercado Financeiro
Requisitos do Sistema
Sistema operacional Windows, macOS ou Linux.
Python instalado na versão 3.x.
Bibliotecas Python necessárias: Pillow, pyautogui, pynput, tkinter. Estas podem ser instaladas através do pip com o comando: pip install pillow pyautogui pynput tkinter.
Instalação
Instalar Python: Certifique-se de que o Python está instalado em seu sistema. Você pode baixá-lo do site oficial do Python.
Instalar Bibliotecas: Abra o terminal ou prompt de comando e execute o seguinte comando para instalar as bibliotecas necessárias:
Copy code![image](https://github.com/marcus1298/software-automacao-vision-probot/assets/32516535/2c9c9c97-4ec4-489a-992a-6df6d84519c1)

pip install pillow pyautogui pynput tkinter
Execução do Programa
Iniciar o Programa: Abra um terminal ou prompt de comando na pasta onde o script está salvo e execute o comando:

Copy code
python nome_do_script.py
Substitua nome_do_script.py pelo nome do arquivo que contém o código.

Monitoramento Inicial: O programa começa com o monitoramento de um ponto pré-definido na tela para detectar mudanças de cor. Este ponto pode ser ajustado posteriormente.

Configuração de Coordenadas
Entrar no Modo de Configuração (Ctrl+M):

Pressione Ctrl+M para ativar o modo de configuração.
Uma janela gráfica aparecerá, permitindo que você clique nos pontos desejados na tela para configurar as coordenadas de ação para as cores Branco (clique do botão esquerdo do mouse), Vermelho (clique do botão do meio) e Azul (clique do botão direito).
Alterar o Ponto de Leitura (Ctrl+N):

Pressione Ctrl+N para ajustar a localização do ponto de leitura.
Clique em um novo ponto na tela para atualizar esta localização.
Visualização dos Pontos
Os pontos de ação e de leitura são visualizados na tela através de uma sobreposição gráfica, permitindo que você sempre veja e verifique as configurações atuais.
Execução de Ações
Após a configuração, o programa automaticamente moverá o mouse para as posições configuradas e realizará cliques esquerdos conforme as cores detectadas nos pontos especificados.
Loop Contínuo
O programa rodará em loop até ser interrompido manualmente, permitindo que a análise e as ações se repitam em intervalos regulares.
Interrupção do Programa
Para interromper o programa, simplesmente feche o terminal ou prompt de comando onde o programa está sendo executado.
Dicas de Uso
Certifique-se de que a tela não seja obstruída por outras janelas durante a execução do programa, pois isso pode afetar a detecção de cores.
Use as configurações com moderação para evitar ações não intencionais, especialmente em um ambiente de mercado financeiro onde decisões rápidas e precisas são críticas.
Este manual visa fornecer uma orientação clara sobre como operar o software de automação de mercado financeiro. Caso tenha dúvidas ou necessite de assistência adicional, não hesite em procurar suporte técnico.
