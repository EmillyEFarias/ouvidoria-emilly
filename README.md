Sistema de Ouvidoria
Projeto desenvolvido em Python para simular um sistema simples de
ouvidoria, permitindo cadastrar e gerenciar reclamações por meio de um
menu interativo no terminal.
Funcionalidades
O sistema oferece as seguintes opções:
1. Listar reclamações: exibe todas as reclamações cadastradas, com
   seus respectivos códigos.
2. Adicionar reclamação: permite cadastrar uma nova reclamação.
3. Pesquisar reclamação: procura uma palavra ou expressão dentro
   das reclamações cadastradas. A pesquisa não diferencia letras
   maiúsculas de minúsculas.
4. Remover reclamação: exclui uma reclamação a partir do código
   informado.
5. Quantidade de reclamações: informa quantas reclamações estão
   cadastradas.
6. Substituir reclamação: permite editar uma reclamação existente,
   informando seu código.
7. Sair do programa: encerra a execução do sistema.
Tecnologias e recursos utilizados
- Python 3
- Listas para armazenar as reclamações durante a execução.
- Estruturas condicionais (if, elif e else) para controlar as
  opções do menu.
- Laços de repetição (while e for) para manter o menu em
  funcionamento e percorrer a lista.
- Entrada e saída de dados com input() e print().
- Métodos de lista, como append() e pop().
- Funções úteis, como len() e range().
Como executar
1. Certifique-se de ter o Python 3 instalado.
2. Salve o código em um arquivo com extensão .py, por exemplo,
   sistema_ouvidoria.py.
3. Abra o terminal na pasta em que o arquivo foi salvo.
4. Execute o comando:
python sistema_ouvidoria.py
Em alguns ambientes, pode ser necessário utilizar python3 no lugar de
python.
Como utilizar
Ao iniciar o programa, será apresentado o menu principal. Digite o
número correspondente à funcionalidade desejada e siga as instruções
exibidas no terminal.

As reclamações são armazenadas em uma lista na memória do programa.
Portanto, os dados não são salvos permanentemente: ao encerrar a
execução, as reclamações cadastradas são perdidas.
Objetivo do projeto
Praticar os fundamentos da linguagem Python por meio da construção de um
sistema interativo, aplicando listas, condicionais, laços de repetição,
entrada e saída de dados e manipulação de elementos de uma lista.
