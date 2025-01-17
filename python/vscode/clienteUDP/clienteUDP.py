from services.connection import connectSocket

s = connectSocket.connectUDP()

print("Cliente socket UDP criado com sucesso.")

host = "localhost"
porta = 5433
mensagem = "Olá servidor"

try:
    print(f"Cliente: {mensagem}")
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")
finally:
    print("Cliente: Fechando a conexão")
    s.close()
