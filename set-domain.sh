#!/bin/bash

# Verifica se você passou os dois argumentos (ex: ./set-domain.sh -2 2)
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Erro: Digite o limite inferior e o superior. Exemplo: ./set-domain.sh -1 1"
    exit 1
fi

INF=$1
SUP=$2

# Formata os números para notação científica (0.000000e+00)
# O comando 'printf' faz essa conversão automática
INF_FORM=$(printf "%.6e" $INF)
SUP_FORM=$(printf "%.6e" $SUP)

echo "--- Alterando Domínio para [$INF_FORM : $SUP_FORM] no setrun.py ---"

# SED para o limite Inferior
sed -i "s/lower\[0\] = .*/lower\[0\] = $INF_FORM/" setrun.py

# SED para o limite Superior
sed -i "s/upper\[0\] = .*/upper\[0\] = $SUP_FORM/" setrun.py

echo "--- Finalizado! ---"
