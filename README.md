Descrição da aplicação

Este é um jogo da velha (tic-tac-toe) jogado por dois jogadores em terminais distintos via rede, usando comunicação com sockets TCP.

O servidor gerencia o tabuleiro e a lógica do jogo, enquanto cada cliente representa um jogador conectado ao servidor. A comunicação é feita por meio de conexão TCP, garantindo que as jogadas sejam transmitidas de forma confiável.

Arquivos do projeto

server.py - Código-fonte do servidor que gerencia o jogo.

client.py - Código-fonte do cliente que se conecta ao servidor para jogar.

README.md - Este manual.

Como executar

1. Requisitos

Python 3 instalado

Três terminais (ou três abas)

2. Executando o servidor

Em um terminal, execute:

python3 server.py

Isso iniciará o servidor e o deixará pronto para aceitar dois jogadores.

3. Executando os clientes

Em dois outros terminais, execute:

python3 client.py

Repita o comando em um segundo terminal para o segundo jogador.

Como jogar

Cada jogador é identificado como X ou O.

Os jogadores são instruídos sobre quando é sua vez.

Quando for sua vez, digite um número de 0 a 8 que representa a posição no tabuleiro:

 0 | 1 | 2
-----------
 3 | 4 | 5
-----------
 6 | 7 | 8

O jogo termina quando um jogador vence ou ocorre um empate.

Exemplo de saída

Você é o jogador X

 X |   |  
-----------
   |   |  
-----------
   |   |  
Sua vez (0-8): 0

O jogador X venceu!
 X | O | O
-----------
 X | X |  
-----------
 X |   |  

Informações adicionais

Protocolo: TCP/IP

Porta usada: 65432

IP padrão: 127.0.0.1 (localhost)

Modo de execução: terminal (linha de comando)

Variáveis principais no código:

porta, tabuleiro, jogadores, simbolo, jogada, conexao, cliente, trava, verificar_vencedor, imprimir_tabuleiro

---

Feito por: Pedro Belini e Pedro Bonelli

GitHub: https://github.com/PedroHBelini/JogoDaVelhaRedes

Youtube: https://youtu.be/xhag7y9MhX8?si=LqPB4mr2FXDwJzxr