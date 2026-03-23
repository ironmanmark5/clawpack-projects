# Simulação de Advecção 1D com Clawpack

Este projeto contém exemplos de advecção unidimensional. Siga as instruções abaixo para testar diferentes resoluções de malha.

## Como Alterar a Malha
Para mudar o número de pontos da malha (resolução) e o domínio:
1. Abra o arquivo `setrun.py`.
2. Procure pela linha `rundata.clawdata.num_cells`.
3. Altere o valor (ex: de `100` para `500`).
4. (Opcional) Altere `rundata.clawdata.lower` e `upper` para mudar os limites do domínio.

## Como Executar
No terminal do Ubuntu/WSL, dentro desta pasta:
1. Compile o código: `make .exe`
2. Rode a simulação: `make .output`
3. Gere os gráficos: `make .plots`

Os resultados serão gerados na pasta `_output/` e as imagens em `_plots/`.

## Utilizar diferentes nomes de diretórios

Caso queira mudar o nome do diretório destino dos resultados e gráficos, o Clawpack utilizado a variável `OUTDIR` para definir a pasta de destino.

(Exemplo: `make .output OUTDIR=output_malha_100` e `make .plots PLOTDIR=plots_malha_200`)

**Importante!!!**

Quando utilizar um nome de pasta diferente do padrão (_output), lembre-se que ao rodar o comando de plotagem, você precisa avisar ao make onde os dados estão:
`make .plots OUTDIR=output_malha_200 PLOTDIR=plots_malha_200`

## 🚀 Automação de Testes (Script de Rodagem)

Para facilitar a vida e evitar ter que digitar comandos longos, criei um script de automação (`rodar.sh`). Ele compila, roda a simulação e gera os gráficos organizando tudo em pastas nomeadas pela malha.

### Como usar o script:
1. Primeiro, altere o valor da malha no `setrun.py`.
2. No terminal, execute o script passando o valor da malha como argumento:
   ```bash
   ./rodar.sh 200
    
(Isso criará automaticamente as pastas `output_malha_200` e `plots_malha_200`)