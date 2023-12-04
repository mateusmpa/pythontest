#!/bin/bash

cd /app/data
python3 server.py > /dev/null 2>&1 &
echo "Server started"
sleep 5  # Aguardar 5 segundos
echo "Script concluído"
