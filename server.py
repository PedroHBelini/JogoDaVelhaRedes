import socket
import threading

HOST = '127.0.0.1'
PORTA = 65432

tabuleiro = [' '] * 9
jogadores = []
trava = threading.Lock()

def imprimir_tabuleiro():
    return f"""
 {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}
-----------
 {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}
-----------
 {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
"""

def verificar_vencedor():
    combinacoes = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != ' ':
            return tabuleiro[a]
    if ' ' not in tabuleiro:
        return 'Empate'
    return None

def lidar_com_jogador(conexao, id_jogador):
    simbolo = 'X' if id_jogador == 0 else 'O'
    conexao.sendall(f"Você é o jogador {simbolo}\n".encode())

    while True:
        with trava:
            if verificar_vencedor():
                break
            if id_jogador == 0 and tabuleiro.count('X') == tabuleiro.count('O') or \
               id_jogador == 1 and tabuleiro.count('X') > tabuleiro.count('O'):
                conexao.sendall(imprimir_tabuleiro().encode())
                conexao.sendall("Sua vez (0-8): ".encode())
                try:
                    jogada = int(conexao.recv(1024).decode().strip())
                except:
                    continue

                if 0 <= jogada < 9 and tabuleiro[jogada] == ' ':
                    tabuleiro[jogada] = simbolo
                else:
                    conexao.sendall("Movimento inválido. Tente novamente.\n".encode())
            else:
                conexao.sendall("Aguarde sua vez...\n".encode())

    resultado = verificar_vencedor()
    with trava:
        for jogador in jogadores:
            try:
                if resultado == 'Empate':
                    jogador.sendall("O jogo empatou!\n".encode())
                else:
                    jogador.sendall(f"O jogador {resultado} venceu!\n".encode())
                jogador.sendall(imprimir_tabuleiro().encode())
            except:
                pass
    conexao.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORTA))
        servidor.listen()
        print("Servidor esperando jogadores...")

        while len(jogadores) < 2:
            conexao, endereco = servidor.accept()
            print(f"Conectado a {endereco}")
            jogadores.append(conexao)
            threading.Thread(target=lidar_com_jogador, args=(conexao, len(jogadores)-1)).start()

if __name__ == "__main__":
    main()