import socket

HOST = '127.0.0.1'
PORTA = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORTA))
        print("Conectado ao servidor.\n")

        while True:
            dados = cliente.recv(1024).decode()
            if not dados:
                break
            print(dados)
            if "Sua vez" in dados:
                jogada = input()
                cliente.sendall(jogada.encode())

if __name__ == "__main__":
    main()