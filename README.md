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
    ``` 
(Isso criará automaticamente as pastas `output_malha_200` e `plots_malha_200`)

## ⚠️ Configuração Inicial (Permissões)

Se você estiver usando o Linux ou WSL pela primeira vez neste projeto, os scripts `.sh` podem apresentar o erro **"Permission denied"**. Para resolver isso e permitir que os scripts funcionem, execute o seguinte comando no terminal (apenas uma vez):

    ```bash
    chmod +x *.sh
    ```
    
## 🌐 Alterar o Domínio da Simulação (`set-domain.sh`)

Para testar o comportamento das equações em diferentes intervalos espaciais (ex: de -1 a 1, ou 0 a 5), utilize o script `set-domain.sh`. Ele formata automaticamente os valores para a notação científica exigida pelo Clawpack.

### Como usar o script de domínio:
No terminal, execute o script passando o **limite inferior** e o **limite superior** separados por espaço:
    ```bash
    ./set-domain.sh -1 1
    ``` 
(Isso atualizará os valores de `lower[0]` e `upper[0]` no arquivo `setrun.py` para -1.000000e+00 e 1.000000e+00)

**Observação Importante:**

Este script apenas altera a configuração no arquivo `setrun.py`. Após definir o novo domínio, você deve rodar a simulação manualmente com os comandos make ou utilizar o script `./rodar.sh [MALHA]` para gerar os novos resultados.

E também certifique-se de que a sua condição inicial (definida no `qinit.f90`) esteja dentro do intervalo de domínio escolhido, caso contrário, a onda poderá não aparecer no gráfico.
