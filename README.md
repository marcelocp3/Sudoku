# Sudoku Solver Pro

Aplicação desktop em Python para resolver tabuleiros de Sudoku por meio de uma interface gráfica simples feita com `tkinter`.

O projeto permite preencher um tabuleiro 9x9 manualmente, navegar entre as células com as setas do teclado e pedir para o programa encontrar uma solução usando backtracking.

## Funcionalidades

- Interface gráfica com grade `9x9`.
- Separação visual dos blocos `3x3`.
- Resolução automática do Sudoku com backtracking.
- Validação de entrada para aceitar apenas números de `1` a `9`.
- Navegação entre células com as teclas de seta.
- Mensagem quando o tabuleiro não possui solução.

## Requisitos

- Python 3
- `tkinter` disponível no ambiente

## Como executar

```bash
python3 sudoku_gui.py
```

## Como usar

1. Execute o programa.
2. Preencha as células conhecidas do Sudoku.
3. Deixe vazias as posições que devem ser resolvidas.
4. Clique em `Resolver`.

Os números informados pelo usuário permanecem em preto. As células originalmente vazias são preparadas para receber a solução calculada pelo algoritmo.

## Estrutura

- [sudoku_gui.py](/home/cuzo/Sudoku/sudoku_gui.py): interface gráfica, captura de entradas e algoritmo de resolução.

## Como funciona

O resolvedor usa backtracking:

- procura a próxima célula vazia;
- tenta números de `1` a `9`;
- valida linha, coluna e bloco `3x3`;
- avança recursivamente quando encontra uma opção válida;
- volta atrás quando uma tentativa leva a um estado inválido.


