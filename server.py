import http.server
import socketserver
import time

# Configurando o diretório raiz do servidor
diretorio_raiz = '.'  # Pode ser alterado para o diretório desejado

# Configurando o número da porta
porta = 8000

# Criando o manipulador (handler) para o servidor
manipulador = http.server.SimpleHTTPRequestHandler

# Configurando o servidor
with socketserver.TCPServer(("", porta), manipulador) as httpd:
    print(f"Servidor iniciado na porta {porta}")

    # Aguarde alguns segundos antes de finalizar
    time.sleep(5)

# O servidor será encerrado após o temporizador
print("Servidor encerrado.")
