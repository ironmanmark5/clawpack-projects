#!/bin/bash

if [ -z "$1" ]
  then
    echo "Erro: Digite o número da malha. Exemplo: ./rodar.sh 200"
    exit 1
fi

MALHA=$1
OUT="output_malha_$MALHA"
PLOT="plots_malha_$MALHA"

echo "--- Alterando a malha para $MALHA no setrun.py ---"

# Ajuste do SED para o seu arquivo específico:
# Ele procura por 'num_cells[0] = ' seguido de números e troca pelo novo valor
sed -i "s/num_cells\[0\] = [0-9]*/num_cells[0] = $MALHA/" setrun.py

echo "--- Iniciando simulação ---"
make .exe
make .output OUTDIR=$OUT
make .plots OUTDIR=$OUT PLOTDIR=$PLOT

echo "--- Finalizado! ---"
echo "Dados em: $OUT"
echo "Gráficos em: $PLOT"
