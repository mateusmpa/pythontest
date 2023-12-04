#!/bin/bash

cd /app/data

# Verifica se o arquivo server_pid.txt existe
if [ -e server_pid.txt ]; then
    # Lê o PID do arquivo
    server_pid=$(cat server_pid.txt)

    # Verifica se o processo ainda está em execução
    if ps -p $server_pid > /dev/null; then
        echo "Server already running with PID $server_pid. Stopping..."
        # Encerra o processo
        kill -TERM $server_pid
        sleep 2  # Dê tempo para o processo encerrar completamente
    else
        echo "No server running with PID $server_pid."
    fi
fi

# Inicia o novo servidor e grava o PID no arquivo
python3 server.py > /dev/null 2>&1 &
echo $! > server_pid.txt

echo "Server started"
sleep 5  # Aguardar 5 segundos

echo "Script concluído"
